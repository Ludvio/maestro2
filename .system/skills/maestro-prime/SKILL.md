---
name: maestro-prime
description: "Tier 1 AI orchestration for Maestro phases. Enforces the 8-layer 'Supreme Architecture' using sequential execution."
---

# Maestro Orchestrator Skill

> **Role**: The "Conductor". This skill manages the end-to-end lifecycle of a Maestro development phase, ensuring rigorous compliance with constitutional, technical, and testing standards.
> **Philosophy**: Quality over Speed. Verify before building.

## Capabilities

1.  **Phase Initialization**: Scaffolds the 8 mandatory artifacts for a new phase.
2.  **Compliance Audit**: Checks if a phase meets `GROMADA_PRINCIPLES.md` and `STANDARD_TECH_STACK.md`.
3.  **Systemic Simulation**: Runs virtual-time simulations (Oracle) to verify invariants.
4.  **UX Narrative Audit**: Verifies navigation coherence via the Four Pillars Law.

## Resources

*   **Templates**: Located in `resources/templates/`. These define the "Shape of Done".
*   **Constitution**: References `docs/system/standards/SUPREME_ENGINEERING_MANIFESTO.md`.

## Stateful Execution (Checkpointing)

To prevent context-drift and ensure high-fidelity 8-layer generation, this skill uses a **Stateful Checkpointing Protocol**. 

*   **State File**: `.system/internal/state/active_phase.json` tracks exactly which layers are done.
*   **Checkpoint Tool**: `python3 .system/skills/maestro-prime/scripts/checkpoint.py`.

### The Checkpoint Protocol (MANDATORY)
1.  **Before Work**: Run `python3 .system/skills/maestro-prime/scripts/checkpoint.py` to identify the current `nextAction`.
2.  **Reflection Layer**: If `nextAction` is `LAYER_0_REFLECTION`, use `TEMPLATE_00` to analyze risks.
3.  **During Work**: Focus ONLY on the single layer identified.
4.  **Context-First Rule**: Before touching ANY file in a domain directory, you MUST load `MANIFEST.json`. If missing, generate it from `MANIFEST_TEMPLATE.json`.
5.  **After File Write**: Run `python3 .system/skills/maestro-prime/scripts/checkpoint.py [ID] [NAME] [LAYER] [PATH]` to persist progress.
6.  **Human Gate**: At the end of Batch A and Batch B, you MUST wait for the user to run `python3 .system/skills/maestro-prime/scripts/checkpoint.py sign`.

## Instructions (The Protocol)

### 1. Generating a Phase (The "8-Layer" Process)
When asked to "Orchestrate Phase [XX]", follow the **Sequential Batching** defined in `.system/workflows/generate_phase_artifacts.md`.

**Layers Mapping (Adaptive Paths):**
- **LAYER_0**: Systemic Reflection (`.system/internal/state/`)
- **LAYER_A**: Milestone (`docs/domains/[PILLAR]/phase_[XX]/`)
- **LAYER_B**: ADR (`docs/system/decisions/`)
- **LAYER_D**: RFC (`docs/domains/[PILLAR]/phase_[XX]/LAYER_D_RFC.md`) [MUST define Systemic Loops]
- **LAYER_S**: Simulation (`tests/evals/`) [The Oracle]
- **LAYER_E**: Idempotency (`docs/system/contracts/`)
- **LAYER_F**: Red Team (`docs/system/red-team/`)
- **LAYER_U**: UI (`src/pages/` -> mapped to `features/[pillar]/`)
- **LAYER_G**: Judge Script (`.system/scripts/judges/`) [HARD GATE]
- **LAYER_I**: Implementation (`src/features/`) [The Body]
- **LAYER_P**: Proof (`tests/e2e/`)
- **LAYER_H**: Improvement Log (`docs/system/improvements/`)

### 2. Context Loading Protocol (Discovery Mode)
1.  **Check**: Does `MANIFEST.json` exist in the target domain?
2.  **YES**: Load it and obey `invariants` and `barriers`.
3.  **NO**: Run **Discovery Mode**:
    - Scan imports to find implicit dependencies.
    - Create a *Draft Manifest* in memory.
    - Ask user to confirm domain boundaries.

### 2. Validating a Phase
When asked to "Audit Phase [XX]", run:
`python3 .system/skills/maestro-prime/scripts/compliance_checker.py [XX]`

## Usage Examples

*   "Checkpoint status" -> `python3 .system/skills/maestro-prime/scripts/checkpoint.py`
*   "Orchestrate Phase 15: Merit Ledger" -> Runs the full 8-step generation.
*   "Audit Phase 14" -> Checks existing artifacts against templates.
