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
- **Cleanup**: Teardown or reset.

## 3. Tooling
- **Primary**: Python 3.x with direct state inspection (if applicable) or Playwright for headless UI-Logic sync.
- **Logging**: Must emit standard signatures for observability (e.g., `[SUCCESS] Invariant A verified`).
