# MAESTRO PROTOCOL v1.0

> **Mandate**: Prevent Operational Drift and "Freestyle" coding.
> **Scope**: All Phase-based development in Maestro.

## 1. The Status Board Rule
Every implementation response MUST begin with the Layer Status Board. No exceptions.
- **Why?**: It provides a cognitive anchor for the AI and a clear roadmap for the User.

## 2. No-Freestyle Implementation
- If a test fails in **Layer P**, you cannot fix it in the code alone.
- You must check if the failure reveals a design flaw in **Layer D (RFC)** or **Layer E (Contract)**.
- If it does, you MUST edit the document first.

## 3. Sequential Locking
- You cannot claim a Layer is DONE if the Layer immediately preceding it (e.g. Judge for Implementation) is not present.
- Success is deterministic, not vibes-based.

## 4. The 30-Second Communication Heartbeat
- If an operation (like running tests) is expected to take time, provide a "Pulse Check" every turn. 
- Never leave the user wondering if you forgot the plan.

---
*Enforced by Orchestrator Mode.*
