---
name: artifact-boundary
description: Universal delivery boundary gatekeeper. MUST USE when creating, modifying, refactoring, or reviewing ANY user-facing artifacts and deliverables (web pages, HTML, UI components, prototypes, reports, decks, dashboards, docs, APIs, CLI tools, scripts), especially when prompts contain implementation constraints, demo backgrounds, mock rules, temporary shortcuts, or requirement corrections (页面开发/原型制作/报表生成/需求变更/纠偏/废弃逻辑清理/去内部残留/MVP交付/交付物审查). Ensures finished artifacts contain ONLY what the real end-user needs, with ZERO leak of internal instructions, model defenses, demo scaffolding, or superseded version residue.
---

# Artifact Boundary

Deliver pure, end-user-ready artifacts. Compile the conversation into the current authorized target, then build exclusively from that target. Never render the conversation, prompt constraints, or development history inside the user-facing product.

## Core Rules

1. **Two-Pass Decoupling (两段式解耦):** Split the input prompt into two isolated buffers:
   - **Target Business Specification:** Real domain entities, workflows, user-visible facts, actions, and necessary disclosures.
   - **Control Context (Quarantine):** Demo timeframes (e.g., "7-minute pitch"), mock instructions, prompt justifications, model defenses, development backgrounds, and rejected ideas.
   *Rule:* Tokens from the Control Context must NEVER appear in UI labels, headings, badges, placeholder texts, comments, or DOM containers.
2. **The Fresh User Blind Test (陌生用户盲测准则):** Ask: *Would a real business user who never saw the prompt understand or need this element?* If an element only exists to prove prompt compliance, explain build shortcuts, or justify data absence, it is forbidden in the artifact.
3. **Surgical Cutover (外科手术式无痕替换):** When a requirement is corrected, modified, or canceled, rebuild the affected surface as if the superseded feature NEVER existed. Do not retain "V2 (deprecated V1)", "Auto-approval removed", or negative rules ("This system does not do X") in product surfaces.
4. **Behavior as Behavior, Never as Narrative:** Implement constraints (e.g., performance shortcuts, mocked endpoints, layout constraints) directly in logic/code. Do not explain them on the screen with banners, delivery bars, or footnotes unless explicitly requested as a business disclosure.
5. **No Structural Meta-Scaffolding:** Do not add helper banners, developer status bars, `.deliver` bars, or prompt-defense cards on top of or surrounding the main deliverable.

## Anti-Pattern Matrix & Banned Residues

| Category | Banned Leakage (Negative Patterns) | Authorized Clean Standard |
|---|---|---|
| **Demo & Mock Scaffolding** | `7分钟演示专用`, `Demo 页面`, `OCR 已跳过/写死数据`, `演示路径卡片` | 呈现纯粹的真实业务界面与操作流程；演示说明放入独立讲稿或控制台。 |
| **Model Defense & Data Caveats** | `当前目录未发现原始三表`, `不在本报告中虚构数据`, `脚本可复算`, `根据提示词要求` | 转化为正向业务口径，如 `表内勾稽一致`、`尚未接入底层合同台账` 或正常的空状态提示。 |
| **Superseded & Correction Residue** | `人工审核 (已废弃自动审批)`, `旧版已下线`, `为什么不采用方案 A`, `修复后的新版` | 彻底移除旧版痕迹，页面直接呈现现行标准工作流；决策原因仅保留在复盘记录中。 |
| **Meta-Bars & Delivery Wrappers** | 页面顶部常驻的 `.delivery-bar`、`交付说明`、`冻结版本说明栏` | 交付物本身保持干净全屏；交付操作（如导出、保存）融入系统原生顶栏或标准菜单。 |

## Execution Workflow

```text
[User Request / Correction]
        │
        ▼
1. Extract Target Spec (Discard prompt control tokens)
        │
        ▼
2. Pure Implementation (Build target business artifact only)
        │
        ▼
3. Pre-Handoff Scan (Run grep/rg regex check on generated files)
        │
        ▼
4. Visual/DOM Gate (Verify no hidden or visible meta-scaffolding)
        │
        ▼
[Deliver Pure Artifact]
```

### Step 1: Extract & Classify
Before writing any file, classify every piece of information:
- **User-Facing:** Business data, valid states, operational controls, lawful disclosures.
- **Internal/Control (Quarantined):** Build constraints, demo guidelines, model excuses, rejected requirements.

### Step 2: Implement Pure Target
Write code and copy strictly in domain language. Keep presentation guidance in presenter notes, technical constraints in dev docs, and product behavior in product UI.

### Step 3: Run Pre-Handoff Static Scan
Before completing the turn, scan all generated or modified files for boundary leakage keywords:
```bash
# Prohibited residual scan command
rg -i "(demo|mock|7分钟|七分钟|提示词|prompt|旧版|废弃|为什么|已移除|已下线|未虚构|脚本可|gen_html|当前目录未|delivery-bar)" <modified_files>
```
*If any match is found, verify whether it is domain-authorized. If it stems from the prompt context, clean it immediately.*

### Step 4: Verification & Handoff Gate
Do not hand off until all 4 criteria pass:
- [ ] **Audience Validity:** Every visible text string serves the final audience's business workflow.
- [ ] **Zero Prompt Echo:** No phrases from prompt constraints exist in UI titles, placeholders, or badges.
- [ ] **Clean Cutover:** No negative rules or deprecated version residues remain from requirement changes.
- [ ] **No Meta-Scaffolding:** No delivery explanation bars or developer status wrappers surround the artifact.
