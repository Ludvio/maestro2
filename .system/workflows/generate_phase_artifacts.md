---
description: "Tier 1 AI orchestration using stateful checkpointing. Ensures 8-layer compliance even across session restarts."
---

# Stateful Phase Orchestration Workflow

This workflow uses `.agent/state/active_phase.json` to track progress. It prevents context-drift by forcing a "Read-Execute-Checkpoint" loop.

## 1. Initialization & State Check
- **Action**: Run `python3 .agent/skills/maestro-prime/scripts/checkpoint.py`.
- **Status Check**: Identify `nextAction`. If resuming, read the last artifact in `artifacts` to restore context.

## 2. Execution Protocol (Sequential Batching)

### Batch A: The Law (Layers 0, A, B, C)
1. **LAYER_0 (Reflection)**: Write a "System 2" internal analysis. Focus on:
   - *Architectural Risk*: Can this de-stabilize the local-first sync?
   - *Constitutional Friction*: Does this risk becoming "Transactional"?
   - *Checkpoint*: `python3 .../checkpoint.py {XX} {NAME} LAYER_0_REFLECTION "Analysis in Chat"`
2. **LAYER_A (Milestone)**: Generate `docs/phases/MILESTONE_{XX}.md`.
3. **LAYER_B (Reasoning)**: Generate `docs/decisions/ADR_{XX}.md`.
4. **LAYER_C (Constitutional Audit)**: Explicit Article check.
5. **HUMAN GATE**: Model must PAUSE. User must run `python3 .../checkpoint.py sign`.

### Batch B: The Blueprint (Layers D, S, E)
6. **LAYER_D (RFC Technical Design)**: Generate `docs/rfcs/RFC_{XX}.md` (300+ LOC).
7. **LAYER_S (Simulation)**: Generate `prototypes/phase_{XX}_sim.ts`. Run it. Loop until pass.
8. **LAYER_E (Idempotency Contract)**: Generate `docs/idempotency_contracts/phase_{XX}.json`.
9. **HUMAN GATE**: Model must PAUSE. User must run `python3 .../checkpoint.py sign`.

### Batch C: The Defense & Meta (Layers F, G, H)
10. **LAYER_F (Red Team)**: Generate `tests/red_team/phase_{XX}_attack.py`.
11. **LAYER_G (Phase Judge)**: Generate `scripts/judges/PHASE_{XX}_JUDGE.py`. Run it. Must exit 0.
12. **LAYER_I (Implementation)**: Build production code in `src/`. Pass all linting.
13. **LAYER_H (Improvement Log)**: Generate `docs/improvements/phase_{XX}_log.md`.
14. **ARCHIVE**: Once finished, run `python3 .../checkpoint.py archive`.

## 3. Standard: Anthropic Metadata (MANDATORY)
Every file MUST start with exactly two lines of metadata (comments allowed based on file type).
- **Line 1**: `Description: [Short summary of the file's purpose]`
- **Line 2**: `Orchestration: Phase [XX] | [Status]`

Example (Markdown):
```markdown
<!-- Description: Local-first larder system. -->
<!-- Orchestration: Phase 14 | Backfill -->
```

## 4. Resume Protocol
If the model loses context:
1. Read `.agent/state/active_phase.json`.
2. Locate the file at `artifacts[last_completed_layer]`.
3. Read that file to regain context.
4. Execute `nextAction`.
