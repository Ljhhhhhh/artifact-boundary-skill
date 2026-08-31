---
name: user-facing-only
description: Keep finished deliverables limited to what their intended users need. Use when demo instructions, mock details, implementation rationale, temporary shortcuts, or superseded requirements might leak into user-facing pages, reports, exports, documentation, APIs, or CLI output. Do not use for general UX or code-quality review.
---

# User-Facing Only

Build the latest authorized deliverable for its intended users. Construction instructions may guide implementation, but do not become user-facing content.

## Method

1. Identify the finished artifact, its intended audience, the audience's task, the intended use context, and the latest authorized requirements.
2. Separate target content from construction context. README notes, seed or fixture data, mock mechanisms, presenter guidance, implementation constraints, and test setup do not become product copy merely because they are true.
3. Build or review only the authorized target. Implement constraints as behavior instead of narrating them in the artifact.
4. Inspect the result as an intended user in the intended use context who never saw the construction conversation. Do not substitute an arbitrary recipient, detached screenshot, or hypothetical misuse for the authorized audience and context.

## Disclosure gate

A visible disclosure is authorized only when at least one of these is established:

- the user or current product requirement explicitly requests it;
- a concrete legal or safety obligation requires it; or
- omitting it would materially mislead the intended audience in the intended use context.

Provenance alone does not authorize visible attribution. In particular, knowing that data, identities, endpoints, or workflows are seeded, mocked, fictional, or prepared for a demonstration does not by itself justify labels such as `demo`, `sample data`, `mock`, or `fictional` in the product or export. When the authorized target is a realistic prototype or simulation, preserving the real business presentation is part of the target.

Before reporting a missing-disclosure finding, identify the authorizing requirement or obligation, the affected intended audience, and the concrete material harm caused by omission. If those cannot be established, do not report the absence as a defect. Do not promote developer-facing README statements, fixture metadata, or implementation facts into user-facing requirements.

Corrections replace superseded product state. Preserve history when history is the purpose of the requested artifact.

Review-only requests report findings without modifying files. Do not remove required disclosures, compatibility behavior, tests, comments, or records unless the user authorized those changes.

When implementation was requested, inspect the applicable rendered, exported, visible, and interactive result. Static checks alone do not establish acceptance.
