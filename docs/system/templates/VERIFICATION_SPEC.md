# 🧪 Verification Script Specification

## 1. Composition Requirements
A valid Gold Standard test script must:
1. **Be Deterministic**: No random values unless seeded explicitly.
2. **Phase-Aware**: Target only the logic/state relevant to the specific phase.
3. **State-First**: Test the underlying Engine (Zustand/Logic) before testing the UI.
4. **Invariant Checks**: A section dedicated to testing that "unbreakables" held true during simulation.

## 2. Structure
- **Setup**: Initialize mock state or reset store.
- **Act**: Trigger the feature hook or store action.
- **Assert (State)**: Check that state mutation matched the transition spec.
- **Assert (Invariant)**: Check that no global rules were violated (e.g., negative balances).
- **Assert (Browser Log Audit)**: Verify zero `Uncaught Errors` in the browser console during the test.
- **Visual Proof**: Capture a screenshot of the final state at `docs/proofs/phase_[XX]_result.png`.
- **Cleanup**: Teardown or reset.

## 4. Adversarial Data Seeding (Standard Anthropic)
Before any `Assert`, the environment MUST be seeded with "Noise Data":
1.  **Volume Injection**: At least 50 random, unrelated records in the same Store.
2.  **Boundary Prodding**: Values at the extreme limits of the schema (max strings, min numbers).
3.  **Schema Version Mix**: Presence of old schema versions in localStorage to verify migration logic.

## 5. Failure Transparency
Verification scripts MUST NOT just say `FAILED`. They must emit a **Root Cause JSON** explaining:
- Which Invariant broke.
- The State Snapshot at the moment of failure.
- The last successful Action.
