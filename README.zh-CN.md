# User-Facing Only

[English](README.md) | [简体中文](README.zh-CN.md)

[![Release](https://img.shields.io/github/v/release/Ljhhhhhh/user-facing-only-skill?style=flat-square)](https://github.com/Ljhhhhhh/user-facing-only-skill/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-111827?style=flat-square)](https://agentskills.io)

**确保 AI 交付干净的最终成品，阻止 Prompt 指令、开发脚手架与修改历史进入面向用户的交付物。**

在生成界面原型、系统代码或业务报告时，AI 经常将对话中的上下文直接渲染到成品中：

- **开发说明变为界面文案**：请求中包含“先用 Mock 数据跑通”，生成的界面顶部出现黄色提示条：*“⚠️ 提示：当前为模拟数据，上线前请对接真实后端”*。
- **变更诉求变为产品标题**：请求中要求“去掉导出按钮”，生成的页面标题变成：*“数据看板 v2（已移除导出按钮）”*。
- **撰写要求泄露给最终受众**：请求中注明“向客户汇报，语气委婉”，生成的报告第一句输出：*“本报告已按要求采用委婉语气编写……”*。

**User-Facing Only** 明确划分了“开发指令”与“产品内容”的边界：**Prompt 是给 Agent 的施工要求，交付物是面向最终用户的可用成品**。中间过程的脚手架、多轮讨论痕迹与已废弃方案均被隔离在成品之外。

## 快速上手

直接让 Codex 安装此 Skill：

```text
使用 $skill-installer 从 https://github.com/Ljhhhhhh/user-facing-only-skill/tree/main/skills/user-facing-only 安装 user-facing-only
```

安装完成后重启 Codex 即可正常使用。只有当请求确实存在交付边界风险时，Codex 才应自动考虑该 Skill，例如演示或 Mock 说明、演讲提示、内部推演、临时捷径、被纠正的需求，或明确要求检查过程语境泄漏。

你也可以显式调用它：

```text
使用 $user-facing-only 在交付前审查该原型，确保实现约束与演讲者提示不会泄漏到面向用户的界面中。
```

## 自动触发边界

本 Skill 保持隐式调用能力，但只面向确实可能泄漏施工语境或废弃需求的交付物。普通代码、UI、API、脚本或文档开发，不会仅因产物类型而启用该 Skill。

用户始终可以显式调用 `$user-facing-only`。若请求仅要求评审，Skill 只能报告问题，不得修改交付物。

## 它解决什么问题

AI Agent 经常把请求中的每一句话都当作候选产品内容，由此产生四类常见缺陷：

- **指令泄漏**：把实现约束（如数据来源、临时条件）直接写成标题、卡片或帮助提示。
- **擅自加戏**：未经用户授权的可选建议，仅因“看起来更完整”就被悄悄做进产品。
- **载体错位**：演说备注、设计推演或验收标准，被摆在最终用户界面上。
- **修改残留**：被否决的设计以“v2”、“已去除某功能”、负向禁令规则或解释性文案的形式留在成品中。

User-Facing Only 在文案落笔前，先从决策层纠正这一认知偏差。

## 效果对比

| 原始请求上下文 | 泄漏产物（错误） | 隔离后成品（正确） |
|---|---|---|
| “做收银台页面，先用 Mock 数据填充。” | 页面顶部展示：*“⚠️ 提示：当前为 Mock 数据，生产环境请接入支付网关。”* | 呈现标准的结账交互流程，不展示底层数据来源说明。 |
| “在个人主页中复用现有用户模型。” | 页面副标题展示：*“基于现有用户模型构建的个人信息管理界面。”* | 架构约束仅作用于代码实现，不作为页面文案向用户展示。 |
| “去掉管理后台的‘自动审批’开关。” | 界面展示：*“审批管理后台 v2 —— 已移除自动审批功能。”* | 仅保留当前的人工审批流程，不保留废弃特性与修改痕迹。 |
| “起草项目汇报，重点突出按期交付。” | 正文开头展示：*“【说明：本报告已根据要求重点突出按期交付情况】”* | 直接输出专业的项目进展正文，不泄露撰写指令与元数据。 |

## 工作原理

```text
用户请求 / 变更指令
    ↓
确定最新授权产物、受众与任务
    ↓
只构建或评审该目标
    ↓
以从未看过开发对话的用户视角检查结果
    ↓
交付纯净成品
```

该 Skill 只遵循一条原则：

> 成品只包含最终受众从最新授权需求中完成任务所需要的内容；施工语境只影响实现，不成为成品内容。

需求纠正会替换旧的产品状态。受众需要的必要披露与合法历史仍然保留。只读评审只报告问题，不修改文件。

完整规则与案例判定详见 [`SKILL.md`](skills/user-facing-only/SKILL.md)。

## 适用场景

- UI 界面与交互式 HTML 原型开发；
- 包含演讲引导或预置 Demo 数据的演示系统搭建；
- 业务报告、幻灯片（PPT/Deck）及数据导出文件生成；
- CLI 命令行输出与面向终端用户的技术文档撰写；
- 经历漫长讨论或多轮需求纠偏后的交付物重构；
- 审查 Prompt 结构、设计思路或内部术语是否意外泄漏到成品中。

## 明确非目标（本 Skill 不做什么）

User-Facing Only 始终保持精准克制，它**不**负责：

- 充当通用的 UX 文案润色或无障碍（Accessibility）审计；
- 代替系统设计去决策 API 兼容性、迁移方案或版本演进策略；
- 默认强加数据来源追溯或样例数据声明标签；
- 擅自删除工程测试、代码注释、兼容适配机制或合法的工程历史记录；
- 根据固定词语或机械扫描判断内容含义；
- 在用户未明确要求的情况下，额外生成演讲者备注或技术背景文档；
- 替代特定业务领域的安全、法务合规或专有产品规范。

## 手动安装

将仓库克隆至本地稳定目录，并软链接至 Codex Skills 目录：

```bash
mkdir -p ~/.codex/skill-sources ~/.codex/skills
git clone https://github.com/Ljhhhhhh/user-facing-only-skill.git ~/.codex/skill-sources/user-facing-only-skill
ln -s ~/.codex/skill-sources/user-facing-only-skill/skills/user-facing-only ~/.codex/skills/user-facing-only
```

后续更新已有克隆：

```bash
git -C ~/.codex/skill-sources/user-facing-only-skill pull --ff-only
```

若其他 Agent 遵循通用的 Agent Skills 目录规范，也可链接至同一源目录：

```bash
mkdir -p ~/.agents/skills
ln -s ~/.codex/skill-sources/user-facing-only-skill/skills/user-facing-only ~/.agents/skills/user-facing-only
```

> **注意：** 请勿在已存在的同名 Skill 目录上强行创建链接。若已存在，请先备份或迁移旧目录。

## 仓库结构

```text
.
├── .github/workflows/
│   └── validate.yml
├── evals/
│   └── cases.md
├── scripts/
│   └── validate.py
├── skills/
│   └── user-facing-only/
│       ├── SKILL.md
│       └── agents/
│           └── openai.yaml
├── LICENSE
├── README.md
└── README.zh-CN.md
```

安装后的 Skill 仍无运行时依赖、外部网络调用或捆绑二进制文件。仓库级验证在 CI 中使用 Python 与 PyYAML；这些开发检查不会参与 Skill 的实际执行。

## 参与贡献

非常欢迎提交 Issue 与 Pull Request！我们最看重的贡献是**能够最小化复现边界失守的典型案例**：

- 用户的原始请求上下文；
- 产生泄漏的错误交付物；
- 符合当前授权边界的预期正确交付物；
- 该案例具有通用性而非特定产品偶发特例的说明。

回归案例应在 `evals/cases.md` 中保持少量且正交。确定性 CI 只验证包结构；行为结论必须在全新上下文中实际运行案例后才能成立。

请避免基于单一特例堆砌关键词黑名单、分类体系或机械的绝对规则。优先采用能够改善受众与授权判断的最小变更。

## 开源协议

本项目基于 [MIT](LICENSE) 协议开源。
