---
description: Create or Retrofit a Maestro Phase using the Golden Standard.
---

# GROMADA PHASE WORKFLOW (The Golden Standard)

Use this workflow to implement any new feature (Phase) or to retrofit a legacy one.

## Phase 1: The Triple-Artifact & Pattern Mining (The Foundation)
1.  **S0 (Pattern Mining)**: Does this task repeat a known pattern (e.g., Staking, Decay, Vouching)?
    - *Action*: Check `docs/patterns/`. If it's a new recurring pattern, CREATE a template first.
2.  **S1 (UX Discovery)**: Verify against `scripts/ux_integrity.py`. Choose a Life Zone.
3.  **LAYER A/B (Milestone & ADR)**: Set the lexicon and deep tech stack.

## Phase 2: Systemic Design (The Brain)
1.  **S2 (LAYER D - RFC)**: MUST use `docs/templates/RFC_TEMPLATE.md`.
    - *Required*: Systemic Loops, Retrofit Plan, and Coherence Matrix.
2.  **S3 (LAYER S - The Oracle)**: MUST use `docs/templates/SIMULATION_TEMPLATE.ts`.
    - *Goal*: 365-day virtual cycle must pass flawlessly.
    - *Iteration*: If simulation fails, update RFC first.

## Phase 3: Implementation & Security
1.  **LAYER F (Red Team)**: Write a script to attack the protocol you designed.
2.  **LAYER G (Judge)**: Deploy `.agent/templates/phase/LAYER_G_JUDGE.py`.
3.  **LAYER I (Implementation)**: Write the actual code (Store, UI).
    - **MANDATORY**: Check API Contract of Phase N-1.

## Phase 4: The Proof
1.  **LAYER P (Proof)**: Write the Playwright E2E test.
2.  **LAYER H (Regret/Improvement)**: Log what went wrong and how we fixed it.

## Phase 5: The Archive
// turbo
1. Run `python scripts/judges/PHASE_X_JUDGE.py`
2. Run `python .agent/skills/maestro-prime/scripts/checkpoint.py archive X [name] sign`
