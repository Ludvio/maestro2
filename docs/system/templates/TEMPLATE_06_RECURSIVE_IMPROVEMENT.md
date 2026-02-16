<!-- Description: Recursive Process Improvement Template. Meta-cognitive log. -->
<!-- Orchestration: Phase [XX] | Template -->
---
description: "The Recursive Improvement Log Template. Defines the 'Meta-Process' for improving Maestro after each phase."
---

# Recursive Self-Improvement Protocol

> **Purpose**: This template forces the AI/Human team to reflect on the *process* of building Maestro, not just the code. It is designed to catch systemic inefficiencies and improve the CI/CD pipeline after every major phase.
> **Trigger**: Run this checklist immediately after the 'Release Candidate' of Phase [XX].

## 1. Post-Phase Reflection (The "Why")
*   **Context**: Phase [XX] is complete.
*   **What went well?**: Feature X was easy to implement because of Y.
    *   *Example: The 'Covenant' logic was reused perfectly for 'Tools'.*
*   **What went poorly?**: Bug Z took 3 hours to debug because logical invariant A was missing.
    *   *Example: We forgot to handle 'Network Timeout' for photo uploads.*

## 2. Meta-Optimization (The "How")
*   **Pattern Recognition**: Did we write similar boilerplate code 3 times? If yes -> Create a Generator Script.
    *   *Action: Create `scripts/scaffold_store.sh`.*
*   **Tooling Gap**: Did we struggle to verify X? If yes -> Build `scripts/verify_X.py`.
    *   *Action: Add 'Image Compression Check' to CI pipeline.*
*   **Process Tweaks**: Did the PRD miss an edge case? If yes -> Update `TEMPLATE_01_BUSINESS_MILESTONE.md`.
    *   *Action: Require 'Offline Strategy' section in every PRD.*

## 3. Actionable Improvements (Next Loop)
1.  **Script**: Create `scripts/optimize_[target].py`.
2.  **Docs**: Update `docs/constitution/GROMADA_PRINCIPLES.md` if a new principle emerged.
3.  **Workflow**: Modify `.agent/workflows/[name].md` to include the verified improvement.

## 4. Integrity Check
*   [ ] Did this improvement make the system *simpler* or *more complex*?
*   [ ] Does this align with the "Slavoarian Minimalist" philosophy?
