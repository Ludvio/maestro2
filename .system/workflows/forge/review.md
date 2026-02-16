# FORGE: Review - Validate SPEC Before Implementation

## Feature Folder: $ARGUMENTS

Deploy 4 parallel validation subagents to verify the SPEC is complete, accurate, and ready for flawless implementation. Catches issues BEFORE coding begins.

---

## Phase 3: REVIEW (Validation)

**CRITICAL**: Execute ALL 4 validation agents simultaneously using multiple Task tool calls in a single response.

### Validation Agent Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    FORGE ORCHESTRATOR (You)                  │
│        Launches parallel validation, synthesizes report      │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┬─────────────────────┐
        ▼                     ▼                     ▼                     ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│  SUBAGENT 1   │   │  SUBAGENT 2   │   │  SUBAGENT 3   │   │  SUBAGENT 4   │
│ Completeness  │   │   Dry Run     │   │    KISS       │   │   Gotchas     │
│    Check      │   │  Validation   │   │    Check      │   │   Coverage    │
└───────────────┘   └───────────────┘   └───────────────┘   └───────────────┘
        │                     │                     │                     │
        ▼                     ▼                     ▼                     ▼
  Completeness.md        DryRun.md            KISS.md            Gotchas.md
        │                     │                     │                     │
        └─────────────────────┴─────────────────────┴─────────────────────┘
                                        │
                                        ▼
                         ┌───────────────────────────────┐
                         │   FORGE/{feature}/REVIEW.md   │
                         └───────────────────────────────┘
```

---

## Prerequisites

Before running this command, ensure:
- [ ] `/forge:outline` has been run for this feature
- [ ] `$ARGUMENTS/SPEC.md` exists
- [ ] `$ARGUMENTS/BRAINSTORM.md` exists (from Find phase)

---

## Input Files

```bash
# Primary input
READ $ARGUMENTS/SPEC.md

# Context from Find phase
READ $ARGUMENTS/BRAINSTORM.md
READ $ARGUMENTS/01-find-integration.md
READ $ARGUMENTS/02-find-kiss.md
READ $ARGUMENTS/03-find-gotchas.md
READ $ARGUMENTS/04-find-external.md
```

---

## Step 1: Launch All 4 Agents IN PARALLEL

Use the Task tool to launch all 4 agents in a SINGLE message with 4 Task tool calls:

### Agent 1: Completeness Check

```
Task tool call:
- description: "Validate SPEC completeness"
- subagent_type: Explore
- prompt: |
    FEATURE FOLDER: $ARGUMENTS

    Validate that the SPEC.md is complete and nothing is missing.

    READ THESE FILES:
    - $ARGUMENTS/SPEC.md
    - $ARGUMENTS/BRAINSTORM.md
    - $ARGUMENTS/01-find-integration.md

    VERIFY:
    1. All integration points from BRAINSTORM are addressed in SPEC
    2. All files listed in BRAINSTORM's "Files to Modify" appear in SPEC
    3. All files listed in BRAINSTORM's "New Code Needed" appear in SPEC
    4. Success criteria are specific and measurable
    5. Every implementation step has clear validation commands
    6. Database changes include RLS policies
    7. Rollback plan exists and is complete
    8. All dependencies between steps are documented

    OUTPUT FORMAT:
    Write findings to $ARGUMENTS/.review/01-completeness.md:

    # Completeness Validation Report

    **Date:** {timestamp}
    **SPEC:** $ARGUMENTS/SPEC.md
    **Status:** PASS / FAIL / WARNINGS
    **Confidence:** {0-100}%

    ## Checklist

    | Item | Status | Notes |
    |------|--------|-------|
    | Integration points covered | ✅/❌ | [details] |
    | Files to modify listed | ✅/❌ | [details] |
    | New files listed | ✅/❌ | [details] |
    | Success criteria measurable | ✅/❌ | [details] |
    | Validation commands present | ✅/❌ | [details] |
    | RLS policies included | ✅/❌ | [details] |
    | Rollback plan complete | ✅/❌ | [details] |
    | Step dependencies clear | ✅/❌ | [details] |

    ## Missing Items

    | What's Missing | Where It Should Be | Priority |
    |----------------|-------------------|----------|

    ## Recommendations

    - [Specific recommendations to fix gaps]
```

### Agent 2: Dry Run Validation

```
Task tool call:
- description: "Dry run SPEC validation"
- subagent_type: Explore
- prompt: |
    FEATURE FOLDER: $ARGUMENTS

    Simulate the SPEC implementation without writing code.
    Verify all referenced files, paths, and patterns actually exist.

    READ THESE FILES:
    - $ARGUMENTS/SPEC.md

    FOR EACH FILE REFERENCED IN SPEC:
    1. "Files to Create" - Verify parent directories exist
    2. "Files to Modify" - Verify files exist at specified paths
    3. "Pattern Reference" files - Verify they exist and contain referenced patterns
    4. "Similar to" references - Verify source files exist
    5. Line number references - Verify lines are approximately correct

    ALSO CHECK:
    - Import statements reference real modules
    - Database table names match existing schema patterns
    - API endpoint paths follow existing conventions
    - Frontend routes don't conflict with existing routes

    OUTPUT FORMAT:
    Write findings to $ARGUMENTS/.review/02-dryrun.md:

    # Dry Run Validation Report

    **Date:** {timestamp}
    **SPEC:** $ARGUMENTS/SPEC.md
    **Status:** PASS / FAIL / WARNINGS
    **Confidence:** {0-100}%

    ## File Path Validation

    ### Files to Modify (Must Exist)

    | File | Exists | Line Ref | Accurate | Notes |
    |------|--------|----------|----------|-------|
    | `backend/app/main.py` | ✅/❌ | ~20 | ✅/❌ | [notes] |

    ### Pattern References (Must Exist)

    | Pattern | Source File | Exists | Pattern Found | Notes |
    |---------|-------------|--------|---------------|-------|
    | `{pattern}` | `{file}` | ✅/❌ | ✅/❌ | [notes] |

    ### Parent Directories (For New Files)

    | New File | Parent Dir | Exists | Notes |
    |----------|------------|--------|-------|

    ## Structural Validation

    | Check | Status | Details |
    |-------|--------|---------|
    | Imports valid | ✅/❌ | [details] |
    | DB tables follow patterns | ✅/❌ | [details] |
    | API paths don't conflict | ✅/❌ | [details] |
    | Routes don't conflict | ✅/❌ | [details] |

    ## Issues Found

    | Issue | Severity | Location in SPEC | Fix |
    |-------|----------|------------------|-----|

    ## Recommendations

    - [Specific fixes needed]
```

### Agent 3: KISS Compliance Check

```
Task tool call:
- description: "Validate KISS compliance"
- subagent_type: Explore
- prompt: |
    FEATURE FOLDER: $ARGUMENTS

    Verify the SPEC follows KISS principles and isn't over-engineered.

    READ THESE FILES:
    - $ARGUMENTS/SPEC.md
    - $ARGUMENTS/02-find-kiss.md
    - $ARGUMENTS/BRAINSTORM.md

    CHECK FOR OVER-ENGINEERING:
    1. Are there unnecessary abstractions?
    2. Are there features beyond MVP scope?
    3. Could any new files be avoided by extending existing ones?
    4. Are there simpler patterns available in the codebase?
    5. Is scope creep from BRAINSTORM → SPEC?
    6. Are there unnecessary configuration options?
    7. Could fewer files achieve the same goal?

    COMPARE:
    - MVP scope in 02-find-kiss.md vs scope in SPEC.md
    - "Defer to v2" items - are any sneaking into SPEC?
    - Implementation steps - could any be combined or eliminated?

    OUTPUT FORMAT:
    Write findings to $ARGUMENTS/.review/03-kiss.md:

    # KISS Compliance Report

    **Date:** {timestamp}
    **SPEC:** $ARGUMENTS/SPEC.md
    **Status:** PASS / FAIL / WARNINGS
    **Confidence:** {0-100}%

    ## Scope Comparison

    | Aspect | BRAINSTORM/KISS | SPEC | Delta | Concern |
    |--------|-----------------|------|-------|---------|
    | New files | X | Y | +Z | [if concerning] |
    | Modified files | X | Y | +Z | [if concerning] |
    | Implementation steps | X | Y | +Z | [if concerning] |

    ## Over-Engineering Checks

    | Check | Status | Details |
    |-------|--------|---------|
    | Unnecessary abstractions | ✅/⚠️ | [details] |
    | Scope beyond MVP | ✅/⚠️ | [details] |
    | Could reuse more | ✅/⚠️ | [details] |
    | Simpler patterns exist | ✅/⚠️ | [details] |
    | Scope creep detected | ✅/⚠️ | [details] |
    | Unnecessary config | ✅/⚠️ | [details] |

    ## Simplification Opportunities

    | Current Approach | Simpler Alternative | Effort Saved |
    |------------------|---------------------|--------------|

    ## v2 Items Creeping In

    | Item | Was Deferred In | Now In SPEC | Recommend |
    |------|-----------------|-------------|-----------|

    ## Recommendations

    - [Specific simplifications]
```

### Agent 4: Gotchas Coverage Check

```
Task tool call:
- description: "Validate gotchas coverage"
- subagent_type: Explore
- prompt: |
    FEATURE FOLDER: $ARGUMENTS

    Verify all known gotchas and learnings are addressed in the SPEC.

    READ THESE FILES:
    - $ARGUMENTS/SPEC.md
    - $ARGUMENTS/03-find-gotchas.md
    - learnings/INDEX.md
    - GEMINI.md (Critical Rules section)

    THEN CHECK RELEVANT LEARNINGS:
    - learnings/database-rls.md (if DB changes in SPEC)
    - learnings/authentication.md (if auth changes in SPEC)
    - learnings/frontend-architecture.md (if frontend changes in SPEC)
    - learnings/integrations.md (if external APIs in SPEC)

    FOR EACH GOTCHA IN 03-find-gotchas.md:
    1. Is it mentioned in SPEC's "Gotchas & Prevention" section?
    2. Is the prevention strategy included in implementation steps?
    3. Is there validation to catch the issue?

    FOR CRITICAL RULES IN GEMINI.md:
    1. Does SPEC violate any rules?
    2. Are anti-patterns avoided?

    OUTPUT FORMAT:
    Write findings to $ARGUMENTS/.review/04-gotchas.md:

    # Gotchas Coverage Report

    **Date:** {timestamp}
    **SPEC:** $ARGUMENTS/SPEC.md
    **Status:** PASS / FAIL / WARNINGS
    **Confidence:** {0-100}%

    ## Gotchas from Research (03-find-gotchas.md)

    | Gotcha | In SPEC | Prevention Step | Validation | Status |
    |--------|---------|-----------------|------------|--------|
    | [gotcha 1] | ✅/❌ | Step X / None | Yes/No | ✅/❌ |

    ## Critical Rules (GEMINI.md)

    | Rule | Applies | SPEC Compliant | Notes |
    |------|---------|----------------|-------|
    | Never use async Supabase client | ✅/❌ | ✅/❌ | [notes] |
    | Sync AuthContext and useAuthStore | ✅/❌ | ✅/❌ | [notes] |

    ## Relevant Learnings Not Addressed

    | Learning | File | Why Relevant | Recommendation |
    |----------|------|--------------|----------------|

    ## Anti-Patterns in SPEC

    | Anti-Pattern | Location in SPEC | Fix |
    |--------------|------------------|-----|

    ## Missing Prevention Strategies

    | Risk | Current in SPEC | Should Add |
    |------|-----------------|------------|

    ## Recommendations

    - [Specific additions to SPEC]
```

---

## Step 2: Create Review Folder

Before launching agents, create the review folder:

```bash
mkdir -p $ARGUMENTS/.review/
```

---

## Step 3: Synthesize into REVIEW.md

After all 4 agents complete, synthesize their reports into a comprehensive review document.

**File**: `$ARGUMENTS/REVIEW.md`

### Template

```markdown
# SPEC Review: {Feature Name}

**Generated:** {timestamp}
**Feature Folder:** $ARGUMENTS
**SPEC Reviewed:** [SPEC.md](./SPEC.md)
**Status:** ✅ APPROVED / ⚠️ NEEDS CHANGES / ❌ BLOCKED

---

## Validation Summary

| Agent | Status | Confidence | Issues |
|-------|--------|------------|--------|
| Completeness | ✅/⚠️/❌ | XX% | X issues |
| Dry Run | ✅/⚠️/❌ | XX% | X issues |
| KISS Compliance | ✅/⚠️/❌ | XX% | X issues |
| Gotchas Coverage | ✅/⚠️/❌ | XX% | X issues |

**Overall Confidence:** XX%

---

## Detailed Reports

- [Completeness Report](./.review/01-completeness.md)
- [Dry Run Report](./.review/02-dryrun.md)
- [KISS Compliance Report](./.review/03-kiss.md)
- [Gotchas Coverage Report](./.review/04-gotchas.md)

---

## Pre-Run Checklist

### Must Fix Before Run (Blocking)

- [ ] {Issue 1} - {Location in SPEC} - {How to fix}
- [ ] {Issue 2} - {Location in SPEC} - {How to fix}

### Recommended Improvements (Non-Blocking)

- [ ] {Recommendation 1} - {Rationale}
- [ ] {Recommendation 2} - {Rationale}

### Verified Good

- ✅ {What passed validation}
- ✅ {What passed validation}

---

## Issues by Severity

### Critical (Must Fix)

| Issue | Agent | Location | Fix |
|-------|-------|----------|-----|
| {issue} | {agent} | {SPEC location} | {fix} |

### Warning (Should Fix)

| Issue | Agent | Location | Fix |
|-------|-------|----------|-----|
| {issue} | {agent} | {SPEC location} | {fix} |

### Info (Consider)

| Issue | Agent | Location | Suggestion |
|-------|-------|----------|------------|
| {issue} | {agent} | {SPEC location} | {suggestion} |

---

## SPEC Diff Suggestions

If issues were found, here are the specific changes to make:

### Section: {SPEC Section}

**Current:**
```
{current text}
```

**Suggested:**
```
{suggested text}
```

**Reason:** {why this change}

---

## Validation Decision

Based on the review:

### If APPROVED (✅)
```
All validation checks passed. SPEC is ready for implementation.

Proceed with:
/forge:run $ARGUMENTS
```

### If NEEDS CHANGES (⚠️)
```
{N} issues found that should be addressed before implementation.

1. Fix the issues in the "Must Fix Before Run" section
2. Consider the "Recommended Improvements"
3. Re-run: /forge:review $ARGUMENTS
```

### If BLOCKED (❌)
```
Critical issues found that block implementation:
- {Critical issue 1}
- {Critical issue 2}

These must be resolved before proceeding.
```

---

## Next Steps

### If Approved
```bash
/forge:run $ARGUMENTS
```

### If Changes Needed
1. Update SPEC.md with fixes
2. Re-run: `/forge:review $ARGUMENTS`
3. Once approved: `/forge:run $ARGUMENTS`

---

*Generated by /forge:review*
*FORGE: Ideate → Find → Outline → Review → Run → Guard*
```

---

## Completion Summary

After creating REVIEW.md, present:

```markdown
## FORGE Review Complete

**Feature Folder:** `$ARGUMENTS`
**Review Report:** `$ARGUMENTS/REVIEW.md`

### Validation Results

| Agent | Status | Confidence |
|-------|--------|------------|
| Completeness | ✅/⚠️/❌ | XX% |
| Dry Run | ✅/⚠️/❌ | XX% |
| KISS Compliance | ✅/⚠️/❌ | XX% |
| Gotchas Coverage | ✅/⚠️/❌ | XX% |

**Overall Confidence:** XX%
**Overall Status:** ✅ APPROVED / ⚠️ NEEDS CHANGES / ❌ BLOCKED

### Issues Found
- **Critical:** X
- **Warnings:** X
- **Info:** X

### Pre-Run Checklist
[Summary of must-fix items]

### Next Step

**If Approved:**
```bash
/forge:run $ARGUMENTS
```

**If Changes Needed:**
1. Fix issues listed in REVIEW.md
2. Re-run: `/forge:review $ARGUMENTS`
```

---

## Confidence Thresholds

| Overall Confidence | Status | Action |
|--------------------|--------|--------|
| 90-100% | ✅ APPROVED | Proceed to Run |
| 70-89% | ⚠️ NEEDS CHANGES | Fix issues, re-review |
| Below 70% | ❌ BLOCKED | Major revision needed |

---

*FORGE: Ideate → Find → Outline → Review → Run → Guard*
