# FORGE: Find - Parallel Feature Research

## Feature: $ARGUMENTS

Deploy 4 parallel research subagents to analyze a feature before implementation. Creates comprehensive research reports and synthesized BRAINSTORM document.

---

## Prerequisites

**Recommended:** Run `/forge:ideate` first to define the feature clearly.

If `FORGE/{feature}/IDEATION.md` exists, Find will use it to guide focused research.
If not, Find will work with the raw `$ARGUMENTS` input (less targeted).

---

## Phase 1: FIND (Research)

**CRITICAL**: Execute ALL 4 research agents simultaneously using multiple Task tool calls in a single response.

### Research Agent Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                 IDEATION.md (if exists)                      │
│         Defines: What it IS, What it is NOT, Scope           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    FORGE ORCHESTRATOR (You)                  │
│         Launches parallel research, synthesizes reports      │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┬─────────────────────┐
        ▼                     ▼                     ▼                     ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│  SUBAGENT 1   │   │  SUBAGENT 2   │   │  SUBAGENT 3   │   │  SUBAGENT 4   │
│  Integration  │   │    KISS       │   │   Gotchas     │   │   External    │
│    Points     │   │  Approach     │   │  & History    │   │   Context     │
└───────────────┘   └───────────────┘   └───────────────┘   └───────────────┘
        │                     │                     │                     │
        ▼                     ▼                     ▼                     ▼
 01-find-integration.md  02-find-kiss.md    03-find-gotchas.md   04-find-external.md
        │                     │                     │                     │
        └─────────────────────┴─────────────────────┴─────────────────────┘
                                        │
                                        ▼
                         ┌───────────────────────────────┐
                         │  FORGE/{feature}/BRAINSTORM.md │
                         └───────────────────────────────┘
```

---

## Step 0: Check for IDEATION.md (NEW)

**Before launching agents, check if IDEATION.md exists:**

```bash
# Check if ideation was done first
ls FORGE/{feature-name}/IDEATION.md
```

**If IDEATION.md exists:**
1. Read it completely
2. Extract: Core Definition, In-Scope items, Out-of-Scope items, Success Criteria, Constraints
3. Include this context in ALL agent prompts (see enhanced prompts below)

**If IDEATION.md does NOT exist:**
1. Warn the user: "No IDEATION.md found. Consider running `/forge:ideate` first for more focused research."
2. Proceed with basic `$ARGUMENTS` input (less targeted research)

---

## Step 1: Create Feature Folder

Create the feature folder in FORGE/ (if not already created by ideate):

```bash
# Convert feature description to kebab-case folder name
# e.g., "outbound calling for voice agents" → "outbound-calling"
mkdir -p FORGE/{feature-name}/
```

---

## Step 2: Launch All 4 Agents IN PARALLEL

Use the Task tool to launch all 4 agents in a SINGLE message with 4 Task tool calls:

### Agent 1: Integration Points Analysis

```
Task tool call:
- description: "Find integration points"
- subagent_type: Explore
- prompt: |
    FEATURE: $ARGUMENTS
    OUTPUT FILE: FORGE/{feature-name}/01-find-integration.md

    ## IDEATION CONTEXT (if IDEATION.md exists, include this section)
    **What it IS (In Scope):**
    {List from IDEATION.md Section 2 - In Scope}

    **What it is NOT (Out of Scope):**
    {List from IDEATION.md Section 2 - Out of Scope}

    **Success Criteria:**
    {List from IDEATION.md Section 3}

    IMPORTANT: Focus research ONLY on in-scope items. Do NOT research out-of-scope items.
    ## END IDEATION CONTEXT

    Analyze the codebase to map integration points for this feature.

    MUST READ FIRST:
    - FORGE/{feature-name}/IDEATION.md (if exists - for scope boundaries)
    - learnings/INDEX.md (master index of all issues)

    Focus on:
    1. Entry Points - Where would this feature be triggered from?
    2. Files to Modify - Which existing files need changes? (with line numbers)
    3. Code to Reuse - What patterns/services already exist?
    4. New Code Needed - What must be created from scratch?
    5. Data Flow - How does data flow for similar features?

    Directories to Search:
    - backend/app/ (FastAPI routes, services, schemas)
    - frontend/src/ (React components, hooks, API clients)
    - backend/supabase/migrations/ (Database schemas)

    OUTPUT FORMAT:
    Write a markdown file to FORGE/{feature-name}/01-find-integration.md with:

    # Integration Points Report: {Feature}

    ## Entry Points
    - **[Location]**: [How feature is triggered]

    ## Files to Modify
    - `[file:line]` - [What changes needed]

    ## Code to Reuse
    - **[Pattern/Service]** in `[file]` - [How to reuse it]

    ## New Code Needed
    - `[new file path]` - [Purpose]

    ## Data Flow
    [Describe how data flows through the system]

    ## Recommended Approach
    [1-2 paragraph summary]
```

### Agent 2: KISS Implementation Approach

```
Task tool call:
- description: "Design KISS approach"
- subagent_type: Explore
- prompt: |
    FEATURE: $ARGUMENTS
    OUTPUT FILE: FORGE/{feature-name}/02-find-kiss.md

    ## IDEATION CONTEXT (if IDEATION.md exists, include this section)
    **What it IS (In Scope) - MVP must include:**
    {List from IDEATION.md Section 2 - In Scope}

    **What it is NOT (Out of Scope) - Defer these:**
    {List from IDEATION.md Section 2 - Out of Scope}

    **MVP Definition:**
    {From IDEATION.md Section 3 - MVP Definition}

    IMPORTANT: The MVP scope is ALREADY DEFINED. Design the simplest way to achieve it.
    ## END IDEATION CONTEXT

    Design the simplest possible implementation for this feature.
    Apply KISS and YAGNI principles ruthlessly.

    MUST READ FIRST:
    - FORGE/{feature-name}/IDEATION.md (if exists - MVP already defined there)
    - learnings/INDEX.md (master index of all issues)

    Focus on:
    1. Similar Features - What existing features can we copy patterns from?
    2. Core MVP - What's the absolute minimum to be useful?
    3. Simplest Architecture - Minimum new files, maximum reuse
    4. Implementation Order - What order minimizes risk?
    5. Anti-Patterns - What NOT to do?

    OUTPUT FORMAT:
    Write a markdown file to FORGE/{feature-name}/02-find-kiss.md with:

    # KISS Implementation Report: {Feature}

    ## Similar Existing Features
    | Feature | File | Pattern | Reuse |
    |---------|------|---------|-------|

    ## Core MVP Scope (v1)
    - [ ] [Essential 1]
    - [ ] [Essential 2]

    ## Defer to v2
    - [ ] [Nice-to-have] - [Why defer]

    ## Simplest Architecture
    New files (minimum): [list]
    Modify (minimal): [list]

    ## Implementation Steps (Ordered)
    1. [Step] - [Why first]

    ## Anti-Patterns to Avoid
    | Don't | Instead | Why |
    |-------|---------|-----|
```

### Agent 3: Gotchas & Historical Context

```
Task tool call:
- description: "Research gotchas & history"
- subagent_type: Explore
- prompt: |
    FEATURE: $ARGUMENTS
    OUTPUT FILE: FORGE/{feature-name}/03-find-gotchas.md

    ## IDEATION CONTEXT (if IDEATION.md exists, include this section)
    **Feature Definition:**
    {From IDEATION.md Section 1 - Core Definition}

    **What it IS (In Scope):**
    {List from IDEATION.md Section 2 - In Scope}

    **Known Constraints:**
    {From IDEATION.md Section 4 - Constraints}

    **Open Questions to Research:**
    {From IDEATION.md Section 5 - Open Questions}

    IMPORTANT: Focus gotcha research on the defined scope. Answer the open questions if possible.
    ## END IDEATION CONTEXT

    Research historical issues and patterns relevant to this feature.
    Mine the project's institutional knowledge to prevent repeating past mistakes.

    MUST READ FIRST (CRITICAL):
    - FORGE/{feature-name}/IDEATION.md (if exists - scope and open questions)
    - GEMINI.md (project rules and anti-patterns)
    - learnings/INDEX.md (master index of all issues)

    Then search relevant files:
    - learnings/database-rls.md
    - learnings/authentication.md
    - learnings/frontend-architecture.md
    - learnings/integrations.md
    - learnings/voice-agents.md
    - learnings/debugging/*.md

    Focus on:
    1. Critical Rules - What project rules apply to this feature?
    2. Past Issues - What bugs/fixes relate to this feature?
    3. Anti-Patterns - What has gone wrong before?
    4. Patterns That Worked - What approaches succeeded?
    5. Risk Areas - Where might this feature go wrong?

    OUTPUT FORMAT:
    Write a markdown file to FORGE/{feature-name}/03-find-gotchas.md with:

    # Gotchas & History Report: {Feature}

    ## Critical Rules (From GEMINI.md)
    | Rule | Why It Matters |
    |------|----------------|

    ## Relevant Past Issues
    ### Issue #X: [Title]
    - Problem: [What happened]
    - Root Cause: [Why]
    - Solution: [How fixed]
    - Applies here: [How relevant]

    ## Anti-Patterns to Avoid
    | Don't | Do Instead | Reference |
    |-------|------------|-----------|

    ## Patterns That Worked
    - **[Pattern]** in `[file]` - [How to apply]

    ## Risk Assessment
    | Risk | Likelihood | Mitigation |
    |------|------------|------------|
```

### Agent 4: External Context & Documentation

```
Task tool call:
- description: "Research external context"
- subagent_type: Explore
- prompt: |
    FEATURE: $ARGUMENTS
    OUTPUT FILE: FORGE/{feature-name}/04-find-external.md

    ## IDEATION CONTEXT (if IDEATION.md exists, include this section)
    **Feature Definition:**
    {From IDEATION.md Section 1 - Core Definition}

    **What it IS (In Scope):**
    {List from IDEATION.md Section 2 - In Scope}

    **Integrations Mentioned:**
    {From IDEATION.md Section 2 - Integrations}

    **Known Constraints:**
    {From IDEATION.md Section 4 - Constraints}

    IMPORTANT: Focus external research on APIs/services needed for in-scope items only.
    ## END IDEATION CONTEXT

    Research external APIs, documentation, and dependencies.

    MUST READ FIRST:
    - FORGE/{feature-name}/IDEATION.md (if exists - integrations and constraints)
    - learnings/INDEX.md (master index)

    Check:
    - research/*.md (existing API docs)
    - backend/.env.example (existing env vars)
    - backend/app/config.py (configuration patterns)

    Focus on:
    1. External APIs - What third-party services are involved?
    2. Documentation - What official docs to reference?
    3. Configuration - What environment setup is needed?
    4. Constraints - Rate limits, quotas, pricing?
    5. Best Practices - What do the docs recommend?

    OUTPUT FORMAT:
    Write a markdown file to FORGE/{feature-name}/04-find-external.md with:

    # External Context Report: {Feature}

    ## Relevant External APIs
    ### [API Name]
    - Purpose: [What we use it for]
    - Endpoints: [Method] [Endpoint] - [Purpose]
    - Auth: [How to authenticate]
    - Rate Limits: [Limits]

    ## Documentation References
    | Document | Location | Key Sections |
    |----------|----------|--------------|

    ## Configuration Required
    ```bash
    # New environment variables
    [VAR_NAME]="[description]"
    ```

    ## External Constraints
    | Constraint | Details | Impact |
    |------------|---------|--------|

    ## Best Practices
    - [Practice 1]

    ## Unknowns to Clarify
    - [ ] [Question]
```

---

## Step 3: Synthesize into BRAINSTORM.md

After all 4 agents complete, synthesize their reports into a comprehensive brainstorm document.

**File**: `FORGE/{feature-name}/BRAINSTORM.md`

### Template

```markdown
# Feature Brainstorm: {Feature Name}

**Generated:** {timestamp}
**Feature:** {description from $ARGUMENTS}
**Status:** Research Complete - Ready for SPEC

---

## Feature Definition (from Ideation)

{If IDEATION.md exists, include this section}

> {Executive Summary from IDEATION.md}

**In Scope:** {List from IDEATION.md}
**Out of Scope:** {List from IDEATION.md}
**Success Criteria:** {List from IDEATION.md}

[Full Ideation Document](./IDEATION.md)

---

## References

Research reports generated by parallel subagents:

- [Feature Ideation](./IDEATION.md) *(if exists)*
- [Integration Points](./01-find-integration.md)
- [KISS Approach](./02-find-kiss.md)
- [Gotchas & History](./03-find-gotchas.md)
- [External Context](./04-find-external.md)

---

## Executive Summary

[2-3 sentence summary synthesizing key findings from all 4 reports]

---

## 1. Integration Architecture

[Synthesized from 01-find-integration.md]

### Where It Connects
| Entry Point | Type | Description |
|-------------|------|-------------|

### Files to Modify
| File | Change | Reason |
|------|--------|--------|

### New Code to Create
| File | Purpose |
|------|---------|

### Data Flow
[From integration report]

---

## 2. Recommended Approach (KISS)

[Synthesized from 02-find-kiss.md]

### MVP Scope (v1)
- [ ] [Essential 1]
- [ ] [Essential 2]

### Defer to v2
- [ ] [Nice-to-have] - [Why]

### Implementation Order
1. **[Step 1]** - [Rationale]
2. **[Step 2]** - [Rationale]

### Patterns to Follow
| Existing Feature | File | Pattern to Copy |
|------------------|------|-----------------|

---

## 3. Known Gotchas & Risks

[Synthesized from 03-find-gotchas.md]

### Critical Rules
| Rule | Impact on This Feature |
|------|------------------------|

### Relevant Past Issues
| Issue | Problem | Prevention |
|-------|---------|------------|

### Anti-Patterns
| Don't | Do Instead |
|-------|------------|

### Risk Assessment
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|

---

## 4. External Dependencies

[Synthesized from 04-find-external.md]

### APIs & Services
| Service | Purpose | Key Constraints |
|---------|---------|-----------------|

### Configuration Required
```bash
# New environment variables
{VAR}={description}
```

### Documentation Links
- [Doc 1]: [path or URL]

---

## 5. Open Questions

[Consolidated unknowns from all 4 reports]

- [ ] [Question 1]
- [ ] [Question 2]

---

## Next Steps

1. **Review this brainstorm** - Confirm approach makes sense
2. **Resolve open questions** - Address unknowns before proceeding
3. **Create SPEC** - Run `/forge:outline FORGE/{feature-name}/`
4. **Validate SPEC** - Run `/forge:review FORGE/{feature-name}/`
5. **Implement** - Run `/forge:run FORGE/{feature-name}/`
6. **Verify** - Run `/forge:guard FORGE/{feature-name}/`

---

*Generated by /forge:find*
*FORGE: Ideate → Find → Outline → Review → Run → Guard*
```

---

## Completion Summary

After creating BRAINSTORM.md, present:

```markdown
## FORGE Find Complete

**Feature Folder:** `FORGE/{feature-name}/`

### Documents Created
- `IDEATION.md` - Feature definition (if created via /forge:ideate)
- `01-find-integration.md` - Integration points mapped
- `02-find-kiss.md` - KISS approach defined
- `03-find-gotchas.md` - Gotchas & history researched
- `04-find-external.md` - External context gathered
- `BRAINSTORM.md` - Synthesized summary

### Key Findings
- **Scope**: [From IDEATION.md - what's in/out]
- **Integration**: [1-line from Agent 1]
- **Approach**: [1-line from Agent 2]
- **Gotchas**: [1-line from Agent 3]
- **External**: [1-line from Agent 4]

### Open Questions
[List any unresolved items]

### Next Step
```bash
/forge:outline FORGE/{feature-name}/
```

Ready to create the SPEC? Review the brainstorm first.
```

---

## Full FORGE Pipeline

```
/forge:ideate  → Define what it IS and IS NOT (interactive)
      ↓
/forge:find    → Research HOW to build it (4 parallel agents)
      ↓
/forge:outline → Create detailed SPEC
      ↓
/forge:review  → Validate SPEC before implementation
      ↓
/forge:run     → Implement the feature
      ↓
/forge:guard   → Verify implementation
```
