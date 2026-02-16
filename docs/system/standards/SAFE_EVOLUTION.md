# SAFE EVOLUTION STANDARD (The Anti-Cannibalization Treaty)

> **Version**: 1.0 (Anthropic-Grade Resilience)
> **Goal**: Evaluate risk before refactoring. Ensure system continuity.
> **Mandate**: "Enhance, don't erase."

## 1. The Golden Rule: No Breaking Changes in Prose
You are FORBIDDEN from modifying existing Logic/State without a **Migration Strategy**.
- **Forbidden**: Deleting a function used by other modules.
- **Forbidden**: Changing the return type of a public API.
- **Allowed**: Adding new optional parameters.
- **Allowed**: Marking old methods as `@deprecated`.

## 2. Refactoring Patterns

### 2.1 The Strangler Fig Pattern (For Major Systems like Sync/Auth)
Instead of rewriting `OldSystem.ts`:
1.  Create `NewSystem.ts` alongside it.
2.  Create an **Adapter/Facade** that routes calls.
3.  Migrate consumers one by one to `NewSystem`.
4.  Once `OldSystem` has 0 users, delete it.

### 2.2 Shadow Mode (For Core Logic)
When replacing critical logic (e.g., Matchmaking, Scoring):
1.  Run `NewLogic()` in parallel with `OldLogic()`.
2.  Compare results in Telemetry (`Log.info('ShadowDiff', { old, new })`).
3.  Only switch when `Diff === 0` (or improvement is proven).

### 2.3 Feature Flags (For UI/UX)
Never delete a UI component. Wrap it.
```typescript
{FLAGS.USE_NEW_DASHBOARD ? <NewDashboard /> : <LegacyDashboard />}
```

## 3. Deprecation Protocol
When you MUST remove code:
1.  **Mark**: Add `@deprecated` JSDoc with reasoning.
2.  **Warn**: Add `console.warn("Using deprecated method X")`.
3.  **Wait**: Ensure no Phase uses it (Check via `grep`).
4.  **Kill**: Remove in the next major Milestone.

## 4. State Migration (The Hardest Part)
If you change the Shape of State (Zustand/DB):
1.  **Upcast**: Write a function `migrateV1toV2(oldState)`.
2.  **Lazy Migrate**: Migrate data only when accessed.
3.  **Double Write**: Write to both Old and New stores during transition.

---
**Signed**: *Maestro Architect*
**Enforced by**: Agent Protocol
