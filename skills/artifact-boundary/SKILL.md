---
name: artifact-boundary
description: Prevent internal instructions, design rationale, demo scaffolding, unauthorized additions, and superseded decisions from leaking into finished user-facing artifacts. Use when creating or reviewing interfaces, prototypes, reports, decks, exports, CLI text, or documentation whose prompt contains implementation constraints, presentation guidance, internal reasoning, or corrected requirements.
---

# Artifact Boundary

Compile the conversation into the current authorized target, then build the artifact from that target. Do not render the conversation itself.

## Core rules

1. **Compile the current target.** Identify the finished artifact, its real audience, the audience's task, the currently authorized content and behavior, and any disclosure explicitly requested or necessary for safe, lawful, or non-misleading use.
2. **Authorize scope before implementation.** Include what the user requested and what is strictly necessary for it to work. Offer optional improvements separately; do not silently implement them.
3. **Qualify user-facing content.** A visible element must help the intended audience understand a fact or state, complete an action, make a decision, or receive a required disclosure. Implementation constraints, design rationale, prompt structure, demo timing, talking points, acceptance criteria, internal codes, and agent reasoning do not become product copy merely because they appeared in the request.
4. **Route content to the correct surface.** Implement behavior as behavior. Keep presenter guidance, technical material, and decision history in their own artifacts only when those artifacts are in scope. Placement does not create authorization to add a new document or surface.
5. **Replace corrected state.** When a requirement is corrected or rejected, update the target and rebuild the affected result. Do not preserve the correction as a feature, title, version label, explanation, negative rule, or lesson inside the current artifact.

If the requested artifact is itself a retrospective, decision record, migration history, or regulated record, its purpose authorizes the relevant history. Do not copy that history into the current product.

## Workflow

### 1. Compile the boundary

Before editing, identify:

- the finished artifact;
- its intended audience and the task they need to complete;
- the latest authorized content and behavior;
- disclosures explicitly requested or necessary for safe, lawful, or non-misleading use;
- instructions that guide implementation but should not be visible;
- suggestions not yet authorized and requirements that have been superseded.

Treat the last two groups as control context, not source copy.

### 2. Classify source material

Classify relevant inputs as:

- **User-facing:** explicitly requested copy or information the audience needs for its task;
- **Behavior:** a capability or constraint to implement rather than narrate;
- **Internal:** implementation detail, design rationale, presenter guidance, acceptance criteria, or agent reasoning;
- **Disclosure:** information that must be visible because the user requested it or omission would make use unsafe, unlawful, or materially misleading. Known provenance alone does not authorize visible attribution;
- **Unapproved:** an optional idea that may be proposed but not implemented;
- **Superseded:** a rejected or corrected state that must not feed the current artifact.

For any visible element, ask: *Why would an intended user who never saw the prompt need this?* If the answer is only to explain the build, guide the presenter, defend a design, or record a correction, keep it out of the artifact.

### 3. Build from the current target

Write in the audience's language and show only information that supports the next valid task or decision. Keep product, presenter, and technical surfaces distinct; create supporting material only when requested.

After a correction, sweep the current artifact and the code or data that generates it for labels, headings, examples, fixtures, controls, and active branches that still expose or implement the rejected idea. Remove residues that no longer serve the current target; do not turn this skill into a general rule for deleting tests, comments, compatibility mechanisms, or historical records.

### 4. Review as a fresh user

Inspect the rendered or executed result without using the production conversation to justify it. Ask:

- Does every visible element serve the intended audience's task?
- Did any implementation instruction, talking point, or design argument become product content?
- Was any unapproved idea implemented?
- Can any element be understood only by knowing what was corrected or rejected?
- Does a standalone screenshot or export look like the finished product rather than an explanation of how to present or build it?

Inspect the applicable visible and interactive states when implementation was requested. For review-only work, report findings without changing the artifact.

## Cases

| Situation | Correct result | Incorrect result |
|---|---|---|
| A business system is built for a seven-minute demonstration, using a prepared path and an OCR shortcut. | The interface shows the real user's business objects, states, actions, and results. Keep timing and talking points in presenter material only if requested. Do not add provenance or sample-data copy unless it is requested or omission would materially mislead the audience. | Cards titled "seven-minute demo path," "why this case is suitable," product-value talking points, or "OCR is skipped for the demo" inside the business interface. |
| A ticket feature must reuse the current data model. | Implement the ticket workflow within that constraint and document the constraint only in an authorized technical artifact. | A user-facing heading such as "Modern ticket handling on the current data model," or extra workflows added to demonstrate the architecture. |
| A manual-review workflow was given an unrequested auto-approval feature, which the user then rejected. | Deliver the manual-review workflow as the current product. Remove auto-approval from the target and affected product surfaces. | "Manual review v2," "auto-approval removed," a new rule saying this product must never auto-approve, or controls and fixtures that still imply the rejected feature. |
| The user explicitly requests a retrospective of a rejected approach. | Explain the approach and decision in the retrospective. Keep the current product focused on current behavior. | Suppress relevant history from the retrospective, or copy that history into the product UI and current operating guide. |

Examples illustrate the decision rules; their nouns and phrases are not a keyword blacklist.

## Handoff gate

Do not hand off until all applicable checks pass:

- **Audience:** every visible element has an intended product audience.
- **Task:** every visible element supports understanding, action, decision, or required disclosure.
- **Authorization:** no optional idea was silently promoted into the artifact.
- **Separation:** implementation constraints, presenter guidance, and design rationale remain outside the product surface.
- **Current state:** superseded content and correction narration are absent from the current artifact and its active behavior.
- **Artifact-only:** the result makes sense without the production conversation.
- **Observed result:** relevant visible and interactive states were actually inspected when applicable.
