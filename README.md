# Artifact Boundary

A Codex-compatible skill that keeps finished artifacts and implementations within the user's current authorized target.

It prevents:

- unrequested scope expansion;
- requirements, rationale, demo notes, and agent reasoning from leaking into user-facing output;
- rejected ideas from surviving as labels, documentation, tests, fixtures, or compatibility code;
- legacy compatibility paths from being added without explicit authorization.

## Install

```bash
git clone https://github.com/Ljhhhhhh/artifact-boundary-skill.git
mkdir -p ~/.codex/skills
ln -s "$(pwd)/artifact-boundary-skill/skills/artifact-boundary" ~/.codex/skills/artifact-boundary
```

The skill is stored at [`skills/artifact-boundary`](skills/artifact-boundary).
