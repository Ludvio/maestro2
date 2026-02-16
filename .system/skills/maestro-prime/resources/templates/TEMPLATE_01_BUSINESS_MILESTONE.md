<!-- Description: Business Milestone for Phase [XX]. -->
<!-- Orchestration: Phase [XX] | Active -->
---
description: "The Business Requirements Template. Defines the 'Why' and 'What' of a phase, ensuring alignment with the Constitution."
---

# Milestone [XX]: [Phase Name] (Lechite Name)

> **Business Goal**: A 2-3 sentence summary of the core value proposition. Example: "Create a tamper-proof ledger of community contributions that rewards selfless behavior without introducing transactional currency."
> **Constitutional Check**: Reference `docs/constitution/GROMADA_PRINCIPLES.md`. Confirm alignment with Article I (Community First) and Article III (Non-Transactional).

## 1. User Stories (The "Who")
*   **As a [Role]**, I want [Action] so that [Benefit].
    *   *Example: As a Volunteer, I want my repair work to be visible on my profile so my neighbors trust my skills.*
*   **As a [Unlikely Role]**, I want to ensure [Constraint] is respected.
    *   *Example: As a Privacy Advocate, I want to ensure my exact location is never stored permanently.*
*   **As a [System Admin]**, I want to [的管理 action] to prevent [Failure Mode].
    *   *Example: As a Moderator, I want to revoke fraudulent 'Merits' to maintain the integrity of the ledger.*

## 2. Key Deliverables (The What)
1.  **[Feature Name]**: Detailed description of the feature.
    *   *Scope*: What is IN and what is OUT?
    *   *Constraint*: Must work offline? Must be < 50kB?
2.  **[Feature Name]**: Detailed description.
3.  **[Feature Name]**: Detailed description.

## 3. UX Journey (The How)
**Scenario: A user claims a task and completes it.**
1.  **Entry Point**: User taps "Tablica Zadań" from the Sidebar.
2.  **Action**: User filters by "Nearest" and taps "Naprawa Płotu" (Fence Repair).
3.  **System Response**: A modal appears with "Zgłaszam się" (I Volunteer).
4.  **Confirmation**: User confirms. The card moves to "Moje Zadania". A toast appears: "Powodzenia!".
5.  **Completion**: User uploads a photo of the fixed fence.
6.  **Reward**: An animation plays, and user receives +50 Zasługi.

## 4. Success Metrics (The Proof)
*   [ ] Latency for "Claim Task" < 200ms on 3G network.
*   [ ] User adoption > 30% active members within 1 week.
*   [ ] Zero data loss on network partition during "Upload Photo".
*   [ ] Constitutional compliance: No PII sent to cloud.

## 5. Micro-Steps (The Plan)
1.  Create `TaskCard` component.
2.  Wire `useTaskStore.claim()` action.
3.  Implement `RewardModal` with confetti.
4.  Write Unit Test for "Double Claim" prevention.
