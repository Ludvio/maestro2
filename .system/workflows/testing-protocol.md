# Maestro Testing Protocol

To ensure the "Simulation Engine" remains robust, every phase must include deterministic integration tests using Playwright.

## Rules
1. **Deterministic Input**: Tests must use constants from `tests/constants.py` for all form fills and assertions.
2. **Page Object Model (POM)**: Every new page must have a corresponding class in `tests/pages/` to encapsulate selectors.
3. **No Flakiness**: Avoid `time.sleep()`. Use Playwright's auto-waiting locators.
4. **Verbosity**: Every test step must be logged using the standard Python `logging` module.
5. **Architectural Verification**: Evolution of the "World State" (Stores) must be verifiable via UI side-effects (e.g., if a vote is cast, the profile history must show it).

## Structure
- `tests/pages/`: Logic for interacting with specific UI views.
- `tests/flows/`: Multipage user journeys.
- `tests/constants.py`: The SSOT for test data.
- `tests/config.py`: Environment settings.
