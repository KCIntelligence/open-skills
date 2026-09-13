#!/usr/bin/env python3
"""Read-only single-SKU daily projection. Standard-library JSON in/out; no forecast fitting."""
import json
import sys
from datetime import date, timedelta
from decimal import Decimal, Inexact, localcontext
from pathlib import Path


def number(value, nonnegative=True):
    if isinstance(value, bool) or not isinstance(value, (str, int, Decimal)):
        raise ValueError("Quantities must be decimal strings or JSON numbers")
    result = Decimal(value)
    if not result.is_finite() or len(result.as_tuple().digits) > 100 or abs(result.adjusted()) > 100:
        raise ValueError("Quantity outside supported precision")
    if nonnegative and result < 0:
        raise ValueError("Negative quantity")
    return result


def day(value):
    if not isinstance(value, str):
        raise ValueError("Date must be ISO text")
    parsed = date.fromisoformat(value)
    if parsed.isoformat() != value:
        raise ValueError("Date must use YYYY-MM-DD")
    return parsed


def analyze(data):
    with localcontext() as context:
        context.prec = 400
        context.traps[Inexact] = True
        return _analyze(data)


def _analyze(data):
    for key in ("sku", "warehouse", "unit"):
        if not isinstance(data[key], str) or not data[key].strip():
            raise ValueError("SKU, warehouse and unit are required")
    start, end = day(data["as_of"]), day(data["horizon_end"])
    if not 1 <= (end - start).days <= 3660:
        raise ValueError("Planning horizon must be 1 to 3660 days")
    lead = data["lead_days"]
    if type(lead) is not int or not 0 <= lead <= 3660:
        raise ValueError("lead_days must be an integer from 0 to 3660")
    opening = number(data["opening_net_qty"], False)
    safety, moq, pack = (number(data[k]) for k in ("safety_qty", "moq", "pack_multiple"))
    if pack <= 0:
        raise ValueError("pack_multiple must be positive")
    demands, receipts, ids, uncertain = {}, {}, set(), []
    for row in data["demand"]:
        when = day(row["date"])
        if not start < when <= end or when in demands:
            raise ValueError("Demand date outside horizon or duplicated")
        demands[when] = number(row["qty"])
    for row in data["receipts"]:
        when = day(row["date"])
        identifier = row["id"]
        if not isinstance(identifier, str) or not identifier or identifier in ids:
            raise ValueError("Receipt batch IDs must be unique nonempty text")
        ids.add(identifier)
        if not start < when <= end:
            raise ValueError("Receipt date outside horizon")
        qty = number(row["qty"])
        if row["status"] == "unconfirmed":
            uncertain.append(identifier)
        elif row["status"] == "confirmed":
            receipts[when] = receipts.get(when, Decimal(0)) + qty
        else:
            raise ValueError("Receipt status must be confirmed or unconfirmed")

    def project(extra=Decimal(0), arrival=None):
        current = opening + (extra if arrival is not None and arrival <= start else Decimal(0))
        first = start.isoformat() if current < 0 else None
        worst = max(Decimal(0), -current)
        rows = []
        for offset in range(1, (end - start).days + 1):
            when = start + timedelta(days=offset)
            inflow = receipts.get(when, Decimal(0)) + (extra if when == arrival else Decimal(0))
            demand = demands.get(when, Decimal(0))
            before = current
            current += inflow - demand
            if current < 0 and first is None:
                first = when.isoformat()
            worst = max(worst, -current)
            rows.append({"date": when.isoformat(), "opening_net_qty": str(before),
                         "confirmed_receipt_qty": str(inflow), "demand_qty": str(demand),
                         "projected_net_qty": str(current)})
        return current, first, worst, rows

    closing, first, worst, rows = project()
    net = max(Decimal(0), safety - closing)
    if net:
        # Decimal division can repeat: use exact integer-scaled ceiling instead.
        target = max(net, moq)
        scale = max(0, -target.as_tuple().exponent, -pack.as_tuple().exponent)
        ti, pi = int(target.scaleb(scale)), int(pack.scaleb(scale))
        qty = Decimal((ti + pi - 1) // pi) * pack
    else:
        qty = Decimal(0)
    arrival = start + timedelta(days=lead)
    projected_end, projected_first, projected_worst, extra_rows = project(qty, arrival)
    timing = (projected_first is None and projected_end >= safety)
    return {"sku": data["sku"], "warehouse": data["warehouse"], "unit": data["unit"],
            "as_of": start.isoformat(), "horizon_end": end.isoformat(),
            "first_shortage_date": first, "maximum_uncovered_qty": str(worst),
            "closing_net_qty": str(closing), "net_replenishment_qty": str(net),
            "order_qty": str(qty), "regular_order_available_date": arrival.isoformat(),
            "regular_order_covers_timing": timing,
            "unconfirmed_receipt_ids": uncertain, "daily": rows,
            "regular_order_projection": {"closing_net_qty": str(projected_end),
                "first_shortage_date": projected_first, "maximum_uncovered_qty": str(projected_worst),
                "daily": extra_rows},
            "limitations": ["Single SKU/warehouse; no shared budget or transfer constraints",
                            "Receipts before same-day demand; no intraday guarantee",
                            "Negative net inventory is unmet demand, not physical stock"]}


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: inventory_plan.py INPUT.json")
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"), parse_float=Decimal)
        print(json.dumps(analyze(data), ensure_ascii=False, indent=2))
    except (KeyError, TypeError, ValueError, ArithmeticError, OSError) as exc:
        raise SystemExit("Input cannot be analyzed: " + str(exc)) from exc


if __name__ == "__main__":
    main()
