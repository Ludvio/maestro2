<!-- Description: Constitutional Gatekeeper Template. Verifies legal alignment. -->
<!-- Orchestration: Phase [XX] | Template -->
---
description: "The Constitutional Check Template. Mandatory 'Audit' section verifying alignment with Maestro's core values."
---

# Maestro Core Principles (Constitutional Check)

> **Context**: These 5 principles are the "Supreme Law" of Maestro. Every architectural decision MUST align with them.
> **Role**: This file acts as a 'Gatekeeper'. If a feature fails any check, it CANNOT be built.

## 1. Community First (Article I)
*   **Question**: Does this feature solve a real problem for a grandmother in a village (e.g., getting firewood)?
*   **Check**: [ ] Yes. It simplifies `X`.
*   **Veto Condition**: If it requires downloading a 50MB app update or 3 complex steps.

## 2. Local Sovereignty (Article II)
*   **Question**: Does this feature require user data (e.g., location, chat) to leave the device unencrypted?
*   **Check**: [ ] No. All data is local-first or E2E encrypted.
*   **Veto Condition**: Any external API call sending PII (Personally Identifiable Information).

## 3. Resilience (Article III)
*   **Question**: Will this work if the village loses internet for 3 days?
*   **Check**: [ ] Yes. It supports offline queuing.
*   **Veto Condition**: A 'Spinner of Death' when offline.

## 4. Lechite Ontology (Article V)
*   **Question**: Does the UI use English tech terms (e.g., 'DAO', 'Contract') or culturally resonant words?
*   **Check**: [ ] Yes. We use 'Wiec', 'Przymierze'.
*   **Veto Condition**: Using 'Inventory' instead of 'Spiżarnia'.

## 5. Non-Transactional (Article III)
*   **Question**: Does this feature encourage *profit* or *mutual aid*?
*   **Check**: [ ] Mutual Aid. It tracks 'Gifts', not 'Prices'.
*   **Veto Condition**: Introducing 'Fees' or 'Trading Fees'.

---
**Override Protocol:**
If a feature *technically* violates a principle (e.g., using Google Maps for convenience), it requires a specific **Exemption Vote** from the core team recorded in `docs/decisions/ADR_XX_EXEMPTION.md`.
