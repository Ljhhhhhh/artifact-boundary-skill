# Artifact Boundary

[English](README.md) | [简体中文](README.zh-CN.md)

[![Release](https://img.shields.io/github/v/release/Ljhhhhhh/artifact-boundary-skill?style=flat-square)](https://github.com/Ljhhhhhh/artifact-boundary-skill/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-111827?style=flat-square)](https://agentskills.io)

**防止 AI 将构建指令、演示脚手架与需求修改历史泄漏到最终交付物中。**

你让 Agent 构建一个*用于 7 分钟演示*的业务系统，它却在界面里加上了名为 **“7 分钟演示路径”** 和 **“为什么该案例适合演示”** 的卡片；你让它移除一个未经确认的功能，它却在标题写上 **“v2 —— 已移除该功能”**。

Artifact Boundary 旨在让 Agent 在构建交付物前，先将上下文对话“编译”为当前唯一授权的有效目标。提示词（Prompt）是指导干活的上下文，绝不应成为交付物本身的一部分。

## 快速上手

直接让 Codex 安装此 Skill：

```text
使用 $skill-installer 从 https://github.com/Ljhhhhhh/artifact-boundary-skill/tree/main/skills/artifact-boundary 安装 artifact-boundary
```

安装完成后重启 Codex 即可正常使用。当用户请求中包含实现约束、演示说明、内部推演或被纠正过的需求时，Codex 会自动识别并触发该 Skill。

你也可以显式调用它：

```text
使用 $artifact-boundary 在交付前审查该原型，确保实现约束与演讲者提示不会泄漏到面向用户的界面中。
```

## 常见失效模式

AI Agent 往往习惯把请求里的每句话都当成产品文案的候选素材，从而引发四种典型的“边界失守”：

- **指令反客为主（Instruction Leakage）：** 提示词里的实现约束被原样写成页面标题、功能卡片、帮助提示或报告正文。
- **擅自加戏升级（Unauthorized Promotion）：** 未经用户授权的可选建议，仅因“看起来更完整/更惊艳”就被悄悄做进了产品。
- **内容载体错位（Wrong-Surface Content）：** 演说备注、设计推演或验收标准，被堂而皇之地摆在最终用户界面上。
- **历史纠正残留（Correction Residue）：** 被否决的设计以“v2”、“已去除某功能”、负向禁令规则、遗留 Mock 数据或解释性文案的形式阴魂不散。

Artifact Boundary 在文案落笔之前，先从决策层纠正这一认知偏差。

## 效果对比

| 用户原始诉求 | 产生泄漏的交付物（错误示范） | 边界清晰的交付物（正确示范） |
|---|---|---|
| “做一个用于 7 分钟路演演示的业务系统。” | 仪表盘赫然出现一张写着“7 分钟演示路径”的卡片。 | 界面只聚焦真实业务流与操作。除非明确要求生成演讲材料，否则计时与演示说明绝不入屏。 |
| “请复用现有的数据模型。” | 页面主标题写成“基于现有数据模型的现代化工作流”。 | 约束仅用于指导底层实现，绝不向最终用户自述技术选型背景。 |
| “去掉自动审批功能。” | 界面展示“人工审批 v2 —— 已移除自动审批”。 | 交付物仅保留当前纯粹的人工审批流，不向用户叙述此前的修改纠偏历史。 |
| “请使用样例数据填充。” | 界面到处打上“数据来源：演示样例”和构建说明。 | 除非用户明确要求、或不标注会引发安全/合规/误导风险，否则不主动暴露多余的来源注脚。 |

## 工作原理

```text
上下文对话
    ↓
编译为当前唯一授权的目标
    ↓
核定交付范围
    ↓
准入面向用户的内容
    ↓
将行为与内部材料路由至正确载体
    ↓
以全新用户视角进行构建与审查
```

该 Skill 贯彻五项核心决策法则：

1. **编译当前目标（Compile Current Target）：** 明确最终交付物载体、目标受众、业务任务、已授权行为以及真正必要的法定/合规披露。
2. **事前核定范围（Authorize Scope）：** 扩展性建议只作为独立提案提出，严禁未经授权静默实装。
3. **严格内容准入（Qualify User-Facing Content）：** 每一个可见元素必须直接服务于目标受众的任务诉求或必要披露。
4. **正确定位载体（Route to Correct Surface）：** 系统行为落实为逻辑而非文案；内部说明与演讲提示置于独立材料中，未明确要求时不进入最终产品。
5. **彻底更替修正状态（Replace Corrected State）：** 需求发生纠偏时，基于最新目标全面重构，绝不把“修改过程”当成产品叙事。

完整规则与案例判定详见 [`SKILL.md`](skills/artifact-boundary/SKILL.md)。

## 适用场景

- UI 界面与交互式 HTML 原型开发；
- 包含演讲引导或预置 Demo 数据的演示系统搭建；
- 业务报告、幻灯片（PPT/Deck）及数据导出文件生成；
- CLI 命令行输出与面向终端用户的技术文档撰写；
- 经历漫长讨论或多轮需求纠偏后的交付物重构；
- 审查 Prompt 结构、设计思路或内部术语是否意外泄漏到成品中。

## 明确非目标（本 Skill 不做什么）

Artifact Boundary 始终保持精准克制，它**不**负责：

- 充当通用的 UX 文案润色或无障碍（Accessibility）审计；
- 代替系统设计去决策 API 兼容性、迁移方案或版本演进策略；
- 默认强加数据来源追溯或样例数据声明标签；
- 擅自删除工程测试、代码注释、兼容适配机制或合法的工程历史记录；
- 在用户未明确要求的情况下，额外生成演讲者备注或技术背景文档；
- 替代特定业务领域的安全、法务合规或专有产品规范。

## 手动安装

将仓库克隆至本地稳定目录，并软链接至 Codex Skills 目录：

```bash
mkdir -p ~/.codex/skill-sources ~/.codex/skills
git clone https://github.com/Ljhhhhhh/artifact-boundary-skill.git ~/.codex/skill-sources/artifact-boundary-skill
ln -s ~/.codex/skill-sources/artifact-boundary-skill/skills/artifact-boundary ~/.codex/skills/artifact-boundary
```

后续更新已有克隆：

```bash
git -C ~/.codex/skill-sources/artifact-boundary-skill pull --ff-only
```

若其他 Agent 遵循通用的 Agent Skills 目录规范，也可链接至同一源目录：

```bash
mkdir -p ~/.agents/skills
ln -s ~/.codex/skill-sources/artifact-boundary-skill/skills/artifact-boundary ~/.agents/skills/artifact-boundary
```

> **注意：** 请勿在已存在的同名 Skill 目录上强行创建链接。若已存在，请先备份或迁移旧目录。

## 仓库结构

```text
.
├── skills/
│   └── artifact-boundary/
│       ├── SKILL.md
│       └── agents/
│           └── openai.yaml
├── LICENSE
├── README.md
└── README.zh-CN.md
```

本 Skill 纯粹基于提示指令驱动，无额外运行时依赖、外部网络调用、独立脚本或捆绑二进制文件。

## 参与贡献

非常欢迎提交 Issue 与 Pull Request！我们最看重的贡献是**能够最小化复现边界失守的典型案例**：

- 用户的原始请求上下文；
- 产生泄漏的错误交付物；
- 符合当前授权边界的预期正确交付物；
- 该案例具有通用性而非特定产品偶发特例的说明。

请避免基于单一特例堆砌“关键词黑名单”或机械的绝对规则。任何演进都应旨在提升对受众诉求、授权范围、内容准入或载体路由的底层辨识能力。

## 开源协议

本项目基于 [MIT](LICENSE) 协议开源。
