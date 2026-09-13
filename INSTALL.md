# 按需安装技能

从 [技能列表](README.md#按需下载安装) 下载需要的 ZIP。每个安装包仅含一项技能，不会自动安装其他五项。安装与使用须遵守包内 [LICENSE](LICENSE)。

## 包里有什么

以 data-consolidation 为例，解压后结构为：

```text
data-consolidation/
├── SKILL.md
├── LICENSE
└── references/
    └── worked-example.md
```

保留整个文件夹，不要只复制SKILL.md。版本号在ZIP文件名中，安装后的技能文件夹名称不带版本号。其他五项采用同样结构。

## Codex

### 让 Codex 协助安装

下载并解压单项ZIP，将解压后的技能文件夹交给Codex，复制下面这段话。安装其他技能时替换名称：

```text
请把我提供的 data-consolidation 文件夹安装为个人可用的 Codex 技能。
只安装这一项，保留 SKILL.md、LICENSE 和 references 目录。
先检查是否已有同名技能；如有，告诉我位置，不自动覆盖。
安装后告诉我实际安装位置，并确认技能是否被识别；不要修改技能内容。
```

### 手动放置

将整个技能文件夹放入个人目录下的 `.agents/skills/`，例如：

```text
用户个人目录/.agents/skills/data-consolidation/SKILL.md
```

只供某个项目使用时，放入该项目的 `.agents/skills/`。同名技能不要在多个位置重复安装。Codex的本地技能位置与重新发现方式以 [OpenAI官方文档](https://learn.chatgpt.com/docs/build-skills) 为准；新增技能未显示时可重启Codex。

### 从 GitHub 按目录安装

仓库可访问且包含对应目录时，可向Codex发送：

```text
$skill-installer
请从 https://github.com/KCIntelligence/open-skills
只安装 skills/data-consolidation 目录。
保留完整目录和 LICENSE；已有同名技能时不要自动覆盖。
```

将最后的技能名称换成需要的那一项即可。若仓库访问失败，使用本地ZIP，不要把GitHub网页另存成SKILL.md。

## WorkBuddy

1. 左侧点开“技能”，选“添加技能 → 上传技能”，选下载的单项技能 ZIP。
2. 导入后自动完成配置，即可在对话中调用。

关闭或卸载在“已安装”列表操作。ZIP 按上面的单技能结构打包，一次装一项。

## 安装后怎样使用

在平台的技能列表中选择已安装技能，或直接说明技能名称和任务：

```text
使用 data-consolidation，把这些文件整理成可以核对的分析底表。
```

没有提供资料时，Agent会结合当前任务引导补充。技能包不含真实业务数据、预设企业规则、模型或办公软件；数据读取和文件生成需要平台提供相应工具与权限。

## 更新与移除

更新前备份自己修改过的技能，再决定是否替换同名目录；不要将不同版本的文件混合。移除时只处理这项技能的目录或在平台内卸载，不删除用户业务数据。

## 可选：核对下载完整性

[SHA256SUMS](packages/SHA256SUMS) 列出每个ZIP的SHA-256。可用系统提供的校验工具对照；校验值用于发现下载损坏，不代表安全认证或平台兼容认证。
