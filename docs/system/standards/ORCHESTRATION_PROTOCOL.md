# 🧭 GROMADA ORCHESTRATION PROTOCOL (V2.0)

> **Status**: MANDATORY for all AI Agents and Humans.
> **Goal**: Prevent systemic fragmentation and cognitive overload.

---

## 1. The Golden Rule of State
Every feature/phase development MUST start with an active `TASK.md` in the phase directory. The Agent is forbidden from executing code without an updated Task Log.

---

## 2. The 6-Phase Execution Loop

### PHASE S1: DISCOVERY & UX AUDIT
*   **Goal**: Find the place in the "Four Pillars" of life.
*   **Action**: Execute `python scripts/ux_integrity.py`.
*   **Deliverable**: A mapping of which Pillar (Home, Market, Fire, Veche) this feature belongs to.

### PHASE S2: SYSTEMIC DESIGN (RFC)
*   **Goal**: Design the loop, NOT the function.
*   **Action**: Fill `LAYER_D_RFC.md` using the updated template.
*   **Deliverable**: Definition of at least 1 Loop (Trigger -> Action -> Reward) and 2 Invariants (Hard Logic).

### PHASE S3: THE ORACLE (SIMULATION)
*   **Goal**: Prove the design works over virtual time.
*   **Action**: Create and run `tests/evals/eval_phase_XX.ts`.
*   **Deliverable**: 0 Critical Failures over a 365-day virtual cycle. **DO NOT PROCEED to S4 IF FAILED.**

### PHASE S4: RETROFITTING (THE BINDING)
*   **Goal**: Prepare the existing system for the new arrival.
*   **Action**: Edit Phase [N-X] stores to support new data requirements.
*   **Deliverable**: Verified imports/exports in legacy code.

### PHASE S5: IMPLEMENTATION (THE BODY)
*   **Goal**: Write the actual code.
*   **Action**: Implement Store (Layer I) and UI (Layer U).
*   **Deliverable**: Working feature using `src/components/ui` components.

### PHASE S6: CLOSURE (THE PROOF)
*   **Goal**: Final verification.
*   **Action**: Run `maestro_grid.py` and E2E tests.
*   **Deliverable**: 100% Green Matrix for the target Phase.

---

## 3. How to avoid getting lost (Anti-Chaos Protocol)
1. **Never "Append-Only"**: If a feature is a duplicate, merge it.
2. **Context Check**: Every 30 minutes of work, the Agent MUST re-read this Protocol and the active `TASK.md`.
3. **Small Batches**: Commit/Finalize after each S-Phase. Do not try to do S1-S6 in one go.
