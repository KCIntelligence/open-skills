# Open Skills

KCIntelligence 的技能组仓库，持续收录多组分析与业务技能。每个技能组独立可用，按业务场景选择对应技能。

## 技能组一览

| 技能组 | 技能数 | 定位 | 入口 |
| --- | --- | --- | --- |
| 评估、排名与对比结果交付技能组 | 6 | 把已有业务资料整理成能核对的数据、能理解的评价结果和能沟通的报告 | 见下文 |
| 小型贸易商运营技能组 | 15 | 面向中小型贸易企业的采购、库存、供应商、交付、结算现金与经营改善闭环 | [trade-operations/README.md](trade-operations/README.md) |

## 评估、排名与对比结果交付技能组

源码可见、有限授权的精简版。本项目使用自定义限制性许可，**不是标准开源许可项目**。

把已有业务资料整理成能核对的数据、能理解的评价结果和能用于沟通的报告。

本系列提供六项可独立使用的轻量技能。适用于一次活动、一个项目阶段、一周、一月或其他业务区间；不限定行业、对象数量或指标数量。企业自己的数据、指标含义和业务规则在实际任务中使用，不由示例代替。

### 按需下载安装

1.0.0 版本提供六个独立 ZIP。只下载需要的技能，不必安装整套；各项技能都能读取用户已有资料，没有必须先安装另一项技能的要求。

| 技能 | 用途 | 独立安装包 |
| --- | --- | --- |
| [data-consolidation](evaluation-skills/data-consolidation/SKILL.md) | 汇总数据、对齐口径 | [下载 ZIP](packages/data-consolidation-1.0.0.zip) |
| [evaluation-ranking](evaluation-skills/evaluation-ranking/SKILL.md) | 按既定规则评价排名 | [下载 ZIP](packages/evaluation-ranking-1.0.0.zip) |
| [organization-brief](evaluation-skills/organization-brief/SKILL.md) | 制作组织管理简报 | [下载 ZIP](packages/organization-brief-1.0.0.zip) |
| [group-comparison](evaluation-skills/group-comparison/SKILL.md) | 对比指定业务分组 | [下载 ZIP](packages/group-comparison-1.0.0.zip) |
| [object-diagnosis](evaluation-skills/object-diagnosis/SKILL.md) | 诊断单个对象的表现差距 | [下载 ZIP](packages/object-diagnosis-1.0.0.zip) |
| [results-publication](evaluation-skills/results-publication/SKILL.md) | 制作已确认结果的公示材料 | [下载 ZIP](packages/results-publication-1.0.0.zip) |

安装方式见 [Codex / WorkBuddy 安装指南](INSTALL.md)。下载完整性校验值见 [SHA256SUMS](packages/SHA256SUMS)。每个 ZIP 只包含一项技能及其配套文件。

### 怎样开始

安装所需技能后，把手头资料交给Agent，再用一句话说清想做什么。不清楚的地方由Agent结合实际资料具体询问。

| 你想做的事 | 可以这样说 |
| --- | --- |
| 把多份表整理到一起 | “使用data-consolidation，把这些表整理成能核对的底表。” |
| 按现有办法算分和排名 | “使用evaluation-ranking，按这份评价办法核对得分和排名。” |
| 向管理层汇报重点 | “使用organization-brief，把这次结果整理成给管理层看的简报。” |
| 看某个组的差距 | “使用group-comparison，帮我看南组有哪些共同关注项。” |
| 看一个对象的问题线索 | “使用object-diagnosis，帮我看对象C与基准的差距，下一步先查什么。” |
| 整理已确认的公示内容 | “使用results-publication，把已确认名单和要求写进这个公示模板。” |

### 业务如何流转

业务负责人提出待决策的问题，数据提供方交付记录；分析者整理和比较事实，提出需要核查或采取行动的事项；决策者确认取舍，执行岗位实施，复核岗位读取新证据判断结果。数据不完整、规则不明确和执行未发生，分别停在不同环节，不能用一篇流畅报告把它们补成已完成。

| 业务环节 | 需要回答的问题 | 技能 | 结果交给谁、用于什么 |
| --- | --- | --- | --- |
| 形成可用事实 | 多个来源讲的是不是同一件事，哪些数能一起使用？ | [data-consolidation](evaluation-skills/data-consolidation/SKILL.md) | 数据负责人补数；分析者取得同口径底表 |
| 执行评价规则 | 按既定标准谁符合评价资格、分数和名次如何形成？ | [evaluation-ranking](evaluation-skills/evaluation-ranking/SKILL.md) | 经办人与专业负责人核验结果，提供统一评价依据 |
| 提炼组织议题 | 哪些发现需要管理层协调或确认？ | [organization-brief](evaluation-skills/organization-brief/SKILL.md) | 管理层审阅证据、选择待决策事项 |
| 支持分组管理 | 组内哪些对象存在差距，是否有共同关注项？ | [group-comparison](evaluation-skills/group-comparison/SKILL.md) | 分组负责人组织核查与协同 |
| 诊断对象表现 | 指定对象与可比基准差在哪，下一步应核查什么？ | [object-diagnosis](evaluation-skills/object-diagnosis/SKILL.md) | 对象负责人核对问题及补充证据，不越级推断根因 |
| 准确表达确认结果 | 哪些已确认结果和要求可以向指定范围公示？ | [results-publication](evaluation-skills/results-publication/SKILL.md) | 获准读者查阅正式结果；不重新评奖或追加任务 |

常见衔接为：数据汇总 → 评价排名 → 组织简报／分组对比／单对象诊断；结果公示另读已确认名单、要求与模板。已有可用数据或评价结果时，可直接使用对应技能，不要求每次全部运行。

### 适用范围

本系列覆盖上述评估、排名与对比结果交付任务，不提供客户自动分群、预测、独立因素分析、异常检测或行动管理系统。简报和诊断可以提出核查建议，但不自动实施处置。

“本周”“本月”“某次活动”“一个项目阶段”只是时间范围。读者和交付用途仍然决定每项技能的工作重点；不把页数、表头或脚本参数当作全部业务逻辑。

每次调用只需补足当前判断所需的上下文：要作的决定、对象与记录粒度、指标定义、比较基准、时间及截止口径、已知业务规则、读者与行动权限。已有材料能够回答的，不重复询问；不足以支持某项结论的，只暂停该结论。

### 示例

```text
使用 data-consolidation。我要比较这次促销中各门店的已支付销售额和退款情况。
订单、支付、退款来自三个文件，日期字段含义不同。
请先判断表的粒度和关联方式，整理不重复计数的底表，列出需要业务确认的问题。
```

```text
使用 object-diagnosis。根据这次评价结果分析指定对象的表现差距，
列清比较基准、事实和待核查信息，不把低分直接当作具体问题根因。
```

### 目录与使用边界

每项技能目录包含SKILL.md、一个按需阅读的合成业务示例及完整LICENSE，可以在许可范围内单独取用，不依赖其他技能目录。安装或免费分享单项技能时，请保留整个技能目录及其中的LICENSE。六项技能内的许可证与根目录LICENSE一致。示例用于解释判断方法，不代表任何企业现行的制度或实际数据。

技能直接读取用户现有资料，不要求用户先手工拼出某个脚本的JSON输入。数据读取、计算和文件生成使用当前Agent可用的工具；本目录不自带办公软件或通用计算引擎。具体文件格式、模板和篇幅按任务处理，不强制月度文件命名。无法完成指定格式时会明确说明限制。

安装技能不会同时安装模型、办公软件或数据处理工具。使用者需自行提供业务资料和适用规则；可处理的格式及可生成的文件取决于当前Agent的工具与权限。平台入口和版本差异见安装指南。

### 许可与商业授权

Copyright (c) 2026 [KCIntelligence](https://github.com/KCIntelligence)。

采用 [KCIntelligence Source-Available License 1.0](LICENSE)。以下是用途摘要，完整条件以许可证为准：

| 使用方式 | 是否需要另行商业授权 |
| --- | --- |
| 个人学习、自用；企业或其他组织内部自用 | 不需要，遵守许可即可免费使用 |
| 修改后内部自用 | 不需要，也不要求公开内部修改或业务数据 |
| 免费分享原版或修改版 | 不需要，但须保留署名、完整许可、修改说明，并继续遵守相同限制 |
| 销售技能或修改版，打包进收费产品、平台或订阅服务 | 需要事先取得书面商业授权 |
| 利用技能向客户提供收费分析、咨询、报告或其他服务 | 需要事先取得书面商业授权，即使不单独收取“技能费” |

企业自身营利不等于禁止内部使用。在收费 AI 平台上运行本技能，或支付模型、办公软件费用，也不因此需要本项目的商业授权。限制重点是对外收费交付技能、技能功能或利用技能提供的服务成果。

本许可不主张用户业务数据或生成结果的所有权，也不要求普通分析报告添加署名或水印；但仅交付生成的报告，并不能豁免收费服务的授权要求。

商业授权与定制需求：

- 邮箱：[hello@kcintelligence.com](mailto:hello@kcintelligence.com)
- 微信：`KCIagent`

声明摘要见 [NOTICE](NOTICE)。仓库名称中的“open-skills”不表示自由商用或采用标准开源许可。
