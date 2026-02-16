# FORGE: Run - Execute Implementation

## Feature Folder: $ARGUMENTS

Execute the SPEC with smart implementation - pauses on uncertainty, spawns helper subagents as needed, and writes learnings continuously.

---

## Prerequisites

Before running this command, ensure:
- [ ] `/forge:outline` has been run for this feature
- [ ] `/forge:review` has passed validation
- [ ] `$ARGUMENTS/SPEC.md` exists and has been reviewed
- [ ] `$ARGUMENTS/REVIEW.md` shows APPROVED status
- [ ] Open questions are resolved
- [ ] User has approved the SPEC

---

## Input File

```bash
READ $ARGUMENTS/SPEC.md
```

---

## Execution Behavior

### Smart Implementation Rules

1. **Follow SPEC step by step** - Don't skip or reorder steps
2. **Validate after each step** - Run the validation commands
3. **Pause when uncertain** - Ask before making assumptions
4. **Spawn helpers when needed** - Use subagents to avoid context bloat
5. **Write learnings immediately** - Document bugs and discoveries as they happen

### When to Pause and Ask

- SPEC is ambiguous or incomplete
- Validation fails and fix isn't obvious
- New requirement discovered not in SPEC
- Multiple valid approaches exist
- External API behaves unexpectedly

### When to Spawn Helper Subagents

| Situation | Helper to Spawn | Purpose |
|-----------|-----------------|---------|
| Stuck on a bug | Learnings Lookup | Search learnings/ for similar issues |
| API/library question | Docs Lookup | Search research/ and external docs |
| Need code example | Pattern Finder | Find similar implementations in codebase |
| Step complete | Test Writer | Create unit/integration tests |

---

## Execution Process

### Phase 1: Pre-Implementation Check

```bash
# Verify SPEC exists
READ $ARGUMENTS/SPEC.md

# Check prerequisites from SPEC
# Verify referenced files exist
# Confirm environment is ready
```

### Phase 2: Step-by-Step Implementation

For each step in the SPEC:

```markdown
## Implementing Step N: {Step Name}

### Reading Requirements
[Read the step from SPEC]

### Implementation
[Write the code]

### Validation
[Run validation command from SPEC]

### Result
- [ ] Step N complete
- [ ] Validation passed
```

### Phase 3: Continuous Learning (EVOLVE)

During implementation, write to learnings when:

| Trigger | What to Write | Where |
|---------|--------------|-------|
| Bug encountered and fixed | Debugging entry | `learnings/debugging/{date}-{slug}.md` |
| Gotcha discovered | Add to gotchas file | `learnings/gotchas/{category}.md` |
| New pattern established | Pattern entry | `learnings/patterns/{pattern-name}.md` |
| External API insight | Integration entry | `learnings/integrations/{service}.md` |

### Learnings Entry Format

```markdown
## {Issue Title}

**Date:** {YYYY-MM-DD}
**Feature:** {feature-name}
**Severity:** High/Medium/Low
**Category:** debugging/gotchas/patterns/integrations

### Problem
[What went wrong or was discovered]

### Root Cause
[Why it happened]

### Solution
[How it was fixed - with code examples]

### Prevention
[How to avoid in future]

### Files Changed
- `path/file.py:line`

### Tags
[database, async, frontend, etc.]
```

After writing any learning, update `learnings/INDEX.md`:
- Add to "Recently Added" section
- Update counts if applicable
- Add cross-references

---

## Helper Subagent Prompts

### Learnings Lookup (when stuck)

```
Task tool call:
- description: "Search learnings for solution"
- subagent_type: Explore
- prompt: |
    PROBLEM: [Description of the issue]

    Search the learnings folder for similar issues:
    - READ learnings/INDEX.md first
    - Search relevant category files
    - Look for matching patterns or solutions

    Return:
    1. Any similar issues found
    2. Their solutions
    3. How to apply to current problem
```

### Docs Lookup (for API questions)

```
Task tool call:
- description: "Search docs for API info"
- subagent_type: Explore
- prompt: |
    QUESTION: [API or library question]

    Search documentation:
    - READ research/*.md for relevant docs
    - Check official documentation if needed
    - Look at existing integration code

    Return:
    1. Relevant documentation
    2. Code examples
    3. Best practices
```

### Pattern Finder (for code examples)

```
Task tool call:
- description: "Find similar implementation"
- subagent_type: Explore
- prompt: |
    NEED: [What kind of code example needed]

    Search codebase for similar implementations:
    - GREP for similar patterns
    - READ matching files
    - Note the pattern used

    Return:
    1. Similar implementations found
    2. Files and line numbers
    3. Pattern to follow
```

### Test Writer (after implementation)

```
Task tool call:
- description: "Write tests for implementation"
- subagent_type: Explore
- prompt: |
    FEATURE: [Feature name]
    FILES: [List of new/modified files]

    Create tests for the implementation:
    - Unit tests for services
    - Integration tests for endpoints
    - Follow existing test patterns

    Output:
    - Test file(s) to create
    - Test cases to include
```

---

## Progress Tracking

Maintain a progress file during implementation:

**File**: `$ARGUMENTS/.forge-progress.md`

```markdown
# FORGE Run Progress

**Started:** {timestamp}
**SPEC:** $ARGUMENTS/SPEC.md
**Status:** In Progress

## Steps

| Step | Status | Started | Completed | Notes |
|------|--------|---------|-----------|-------|
| 1 | ✅ Done | 10:00 | 10:15 | Clean |
| 2 | ✅ Done | 10:15 | 10:30 | Fixed typo |
| 3 | 🔄 In Progress | 10:30 | - | Working on validation |
| 4 | ⏳ Pending | - | - | - |

## Issues Encountered

### Issue 1: [Title]
- **Step:** 2
- **Problem:** [What happened]
- **Solution:** [How resolved]
- **Learning Written:** Yes/No

## Helpers Spawned

| Helper | Purpose | Result |
|--------|---------|--------|
| Learnings Lookup | Find RLS fix | Found Issue #4 |

## Learnings Written

| File | Summary |
|------|---------|
| `learnings/debugging/...` | [Brief] |
```

---

## Completion

When all steps are complete:

1. **Verify all validation commands pass**
2. **Run full test suite**
3. **Check if E2E tests are needed** (see Phase 4)
4. **Update progress file to complete**
5. **Present summary**

---

## Phase 4: Automatic E2E Detection & Execution

After implementation is complete, automatically determine if browser E2E tests should run.

### E2E Detection Triggers

**Check SPEC.md for UI signals:**
- Success criteria mention: "visible", "button", "page", "UI", "form", "click", "navigate", "display", "show"
- Has "Manual Verification" section with browser-based steps
- References frontend pages or components

**Check .forge-progress.md for file signals:**
- Frontend files modified (`frontend/src/**`)
- UI components created/changed
- Routes added

### E2E Decision Logic

```python
# Pseudocode for E2E detection
e2e_needed = False

# Check SPEC content
ui_keywords = ["visible", "button", "page", "UI", "form", "click",
               "navigate", "display", "show", "modal", "dialog"]
if any(keyword in spec_content.lower() for keyword in ui_keywords):
    e2e_needed = True

# Check for manual verification section
if "Manual Verification" in spec_content:
    e2e_needed = True

# Check modified files
if any("frontend/" in file for file in modified_files):
    e2e_needed = True

# Backend-only changes skip E2E
if all("backend/" in file for file in modified_files):
    if not any(keyword in spec_content.lower() for keyword in ui_keywords):
        e2e_needed = False
```

### If E2E Needed

**Ask user before running:**

```markdown
## E2E Testing Detected

This feature includes UI changes that should be verified with browser tests.

**Detected triggers:**
- [ ] Success criteria mention UI elements
- [ ] Manual verification section present
- [ ] Frontend files modified

**Options:**
1. **Run E2E now** - Execute browser tests automatically
2. **Skip E2E** - Proceed to guard without browser tests
3. **Run E2E later** - Mark as pending in progress file

Would you like to run E2E tests now?
```

**If user confirms, execute:**

```bash
/forge:e2e $ARGUMENTS
```

### E2E Results in Completion

Include E2E results in the completion summary:

```markdown
## FORGE Run Complete

**Feature:** $ARGUMENTS
**Duration:** [time]
**Steps Completed:** [X/Y]

### Files Created
| File | Lines |
|------|-------|
| `path/file` | 123 |

### Files Modified
| File | Changes |
|------|---------|
| `path/file` | [Brief] |

### Issues Encountered
[List any issues and how resolved]

### Learnings Written
[List any new learnings documented]

### Validation Status
- [ ] All step validations passed
- [ ] Backend tests pass
- [ ] Frontend tests pass
- [ ] Type checks pass
- [ ] Lint checks pass

### E2E Test Status
| Metric | Value |
|--------|-------|
| Triggered | Yes / No |
| Tests Run | {N} |
| Passed | {P} |
| Failed | {F} |
| Report | [E2E-REPORT.md](./E2E-REPORT.md) |
| Screenshots | {N} saved to `e2e-screenshots/` |

### Next Step
```bash
/forge:guard $ARGUMENTS
```
```

### If E2E Not Needed

```markdown
### E2E Test Status
| Metric | Value |
|--------|-------|
| Triggered | No |
| Reason | Backend-only changes / No UI signals detected |
```

---

*FORGE: Ideate → Find → Outline → Review → Run (or Ralph Run) → E2E (auto) → Guard*

---

## Alternative: Autonomous Execution

For well-defined SPECs with clear validation, consider using:

```bash
/forge:ralph-run $ARGUMENTS --max-iterations 25
```

This runs autonomously with self-correction. See `/forge:ralph-run --help` for details.
