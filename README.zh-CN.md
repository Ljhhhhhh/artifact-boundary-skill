# Artifact Boundary

[English](README.md) | [简体中文](README.zh-CN.md)

[![Release](https://img.shields.io/github/v/release/Ljhhhhhh/artifact-boundary-skill?style=flat-square)](https://github.com/Ljhhhhhh/artifact-boundary-skill/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-111827?style=flat-square)](https://agentskills.io)

**阻止 AI 的构建指令、演示脚手架和需求纠正历史泄漏到最终产品。**

你让 Agent 构建一个*用于七分钟演示*的业务应用，结果它交付了名为 **“七分钟演示路径”** 和 **“为什么这个案例合适”** 的卡片。你让它删除一个未经要求的功能，结果它交付了 **“v2——已移除该功能”**。

Artifact Boundary 教会 Agent 在构建之前，先把对话编译成当前获得授权的目标。Prompt 用来指导工作，而不应成为交付物本身。

## 快速开始

让 Codex 安装此 Skill：

```text
使用 $skill-installer 从 https://github.com/Ljhhhhhh/artifact-boundary-skill/tree/main/skills/artifact-boundary 安装 artifact-boundary
```

安装后重启 Codex，然后照常工作。当请求中包含实现约束、演示指导、内部推理或经过纠正的需求时，Codex 可以自动发现并使用此 Skill。

也可以显式调用：

```text
使用 $artifact-boundary 在交付前审查这个原型。不要让实现约束和演示者指导出现在面向用户的结果中。
```

## 它解决什么问题

AI Agent 经常把请求中的每一句话都当作候选产品内容，由此产生四类常见缺陷：

- **指令泄漏到交付物：** 实现约束变成标题、卡片、帮助文案或报告正文。
- **未经授权的需求升级：** 一个可选想法因为看起来有用或更有表现力，就被悄悄实现。
- **内容出现在错误载体：** 演示者备注、设计理由或验收标准出现在产品本身。
- **纠正残留：** 已否决的想法继续以“v2”“已移除”、反向规则、测试数据或解释文案的形式存在。

Artifact Boundary 在文案产生之前，先纠正底层的判断错误。

## 修改前后

| 请求上下文 | 发生泄漏的交付物 | 边界正确的结果 |
|---|---|---|
| “为七分钟演示构建这个系统。” | 仪表盘出现名为“七分钟演示路径”的卡片。 | 产品展示真实业务任务；除非用户要求演示材料，否则计时信息不进入产品。 |
| “复用当前数据模型。” | 页面标题写成“基于当前数据模型的现代工作流”。 | 该约束影响实现，但不向产品用户讲述实现过程。 |
| “删除自动审批功能。” | “人工审核 v2——已移除自动审批”。 | 当前产品只呈现人工审核流程，不保留需求纠正故事。 |
| “使用样例数据。” | 自动添加数据来源标签和构建说明。 | 除非用户要求，或不说明会造成不安全、不合法或实质性误导，否则不自动展示来源说明。 |

## 工作原理

```text
对话
  ↓
编译当前获得授权的目标
  ↓
确认实现范围
  ↓
判断哪些内容应面向用户
  ↓
把行为和内部材料放到正确载体
  ↓
以首次使用者的视角构建并审查
```

此 Skill 执行五项核心判断：

1. **编译当前目标**——识别交付物、受众、任务、已授权行为和真正必要的披露。
2. **实现前确认授权范围**——可选想法应单独提出，而不是静默加入产品。
3. **判断面向用户的内容是否合格**——可见内容必须服务于目标用户的任务，或属于必要披露。
4. **把内容放到正确载体**——行为应实现为行为；除非用户要求相应材料，否则内部内容和演示者材料不得进入产品。
5. **用纠正后的状态替换旧状态**——从最新目标重新构建，而不是在交付物中讲述纠正过程。

完整规则和案例请参阅 [`SKILL.md`](skills/artifact-boundary/SKILL.md)。

## 适用场景

- 界面和 HTML 原型；
- 包含演示指导或预置数据的演示系统；
- 报告、演示文稿和导出文件；
- CLI 输出和面向用户的文档；
- 根据很长或反复修正的对话构建交付物；
- 审查 Prompt 结构、设计理由或内部术语是否泄漏到结果中。

## 此 Skill 不负责什么

Artifact Boundary 有意保持职责收敛。它不会：

- 充当通用的 UX 文案或无障碍审查工具；
- 决定 API 兼容性、迁移或版本策略；
- 默认要求展示数据来源或样例数据标签；
- 要求删除测试、注释、兼容机制或合法的历史记录；
- 在相应交付物不属于范围时，擅自创建演示者备注或技术文档；
- 替代特定领域的安全、法律或产品要求。

## 手动安装

将仓库克隆到稳定的源目录，再把 Skill 链接到 Codex：

```bash
mkdir -p ~/.codex/skill-sources ~/.codex/skills
git clone https://github.com/Ljhhhhhh/artifact-boundary-skill.git ~/.codex/skill-sources/artifact-boundary-skill
ln -s ~/.codex/skill-sources/artifact-boundary-skill/skills/artifact-boundary ~/.codex/skills/artifact-boundary
```

更新已有克隆：

```bash
git -C ~/.codex/skill-sources/artifact-boundary-skill pull --ff-only
```

能够发现共享 Agent Skills 目录的 Agent，也可以链接同一个源目录：

```bash
mkdir -p ~/.agents/skills
ln -s ~/.codex/skill-sources/artifact-boundary-skill/skills/artifact-boundary ~/.agents/skills/artifact-boundary
```

不要在已有 Skill 目录上直接创建链接。请先检查或移动现有安装。

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

此 Skill 不包含运行时依赖、网络调用、脚本或捆绑的可执行文件。

## 参与贡献

欢迎提交 Issue 和 Pull Request。最有价值的贡献是能够最小化复现边界错误的案例，包括：

- 用户请求；
- 错误的面向用户结果；
- 期望得到的当前状态交付物；
- 该案例为什么能够泛化，而不只适用于某个产品或某个词语。

请避免根据单一失败案例添加关键词黑名单或普遍化规则。修改应提升对受众、授权范围、内容资格或载体归属的判断能力。

## 许可证

[MIT](LICENSE)
