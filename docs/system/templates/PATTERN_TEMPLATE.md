<!-- Pattern Name: [Name of the Pattern, e.g., STAKING / RĘKOJMIA] -->
<!-- Type: [Behavioral | Structural | Social | Economic] -->

# Pattern: {Name}

> **Essence**: One sentence describing the deep logic of this pattern.
> *Example: "Placing something of value at risk to guarantee truth or performance."*

## 1. Context (Where does it happen?)
*   List the Phases where this pattern appears.
*   *Example*: Trade (P05), Courts (P34), Oaths (P16).

## 2. The Mechanics (The Algorithm)
*   **Input**: What is staked? (Resource, Merit, Access)
*   **Hold**: Who holds the stake? (Escrow, Community, Spirit)
*   **Trigger**: What decides the outcome? (Time, Voting, Verification)
*   **Outcome A (Success)**: Return stake + Reward.
*   **Outcome B (Failure)**: Burn stake + Penalty.

## 3. Systemic Links (Connectivity)
*   How does this pattern connect to the Core Loops?
*   **Merit Impact**: Does using this pattern generate specific Merit Badges?
*   **Network Effect**: Does this pattern require >1 user?

## 4. UX Narrative (How it feels)
*   **Metaphor**: e.g., "Putting your hand in the fire."
*   **Visual Signal**: e.g., "Lock Icon", "Glowing Border".

## 5. Implementation Guide
*   **Shared Code**: `src/patterns/useStaking.ts` (Example)
*   **Interfaces**:
```typescript
interface StakingProps {
    amount: number;
    duration: number;
    onSlash: () => void;
}
```
