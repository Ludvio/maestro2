# FORGE: Guard - Verify Implementation

## Feature Folder: $ARGUMENTS

Validate the implementation with automated tests AND document what was done.

---

## Prerequisites

Before running this command, ensure:
- [ ] `/forge:run` has been completed for this feature
- [ ] All implementation steps are done
- [ ] No known failing tests

---

## Input Files

```bash
READ $ARGUMENTS/SPEC.md
READ $ARGUMENTS/.forge-progress.md  # If exists
READ $ARGUMENTS/E2E-REPORT.md  # If E2E tests were run
```

---

## Verification Process

### Phase 1: Capture Before State

Record the state before verification:

```bash
# Get current branch and commit
git branch --show-current
git rev-parse HEAD
git status

# Count files in relevant directories
find backend/app/{feature}/ -name "*.py" | wc -l
find frontend/src/ -name "*{feature}*" | wc -l
```

### Phase 2: Run Automated Tests

Execute all test suites:

```bash
# Backend Tests
cd backend

# Lint check
uv run ruff check .

# Format check
uv run ruff format --check .

# Type check
uv run mypy app/

# Unit/Integration tests
uv run pytest tests/ -v --tb=short

# Frontend Tests
cd frontend

# Lint check
npm run lint

# Format check
npm run format:check

# Type check
npx tsc --noEmit

# E2E tests (if applicable)
npm run test:e2e
```

### Phase 3: Check SPEC Success Criteria

Go through each success criterion from SPEC.md:

```markdown
## Success Criteria Verification

| Criterion | Status | Evidence |
|-----------|--------|----------|
| [From SPEC] | ✅/❌ | [How verified] |
| [From SPEC] | ✅/❌ | [How verified] |
```

### Phase 4: Manual Test Cases

Generate test cases for manual verification:

Based on the feature, create specific test scenarios:

```markdown
## Manual Testing Required

### Test Case 1: [Happy Path]
**Steps:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Expected Result:** [What should happen]

**How to Verify:** [Specific check]

---

### Test Case 2: [Edge Case]
**Steps:**
1. [Step 1]
2. [Step 2]

**Expected Result:** [What should happen]

**How to Verify:** [Specific check]

---

### Test Case 3: [Error Handling]
**Steps:**
1. [Trigger error condition]
2. [Observe behavior]

**Expected Result:** [Graceful error handling]

**How to Verify:** [Specific check]
```

---

## Output File

**File**: `$ARGUMENTS/VERIFICATION.md`

### Template

```markdown
# Verification Report: {Feature Name}

**Date:** {YYYY-MM-DD}
**SPEC:** [./SPEC.md](./SPEC.md)
**Status:** ✅ Complete / ⚠️ Partial / ❌ Failed

---

## Before State

- **Branch:** `{branch before}`
- **Commit:** `{commit hash}`
- **Date:** {implementation start date}

---

## After State

- **Branch:** `{branch after}`
- **Commit:** `{commit hash}`
- **Files Created:** {count}
- **Files Modified:** {count}

---

## Changes Summary

### Files Created

| File | Purpose | Lines |
|------|---------|-------|
| `backend/app/{feature}/router.py` | API endpoints | 85 |
| `backend/app/{feature}/service.py` | Business logic | 120 |
| `backend/app/{feature}/schemas.py` | Request/response models | 45 |
| `frontend/src/pages/{Feature}.tsx` | UI page | 150 |
| `frontend/src/api/{feature}.ts` | API client | 35 |

### Files Modified

| File | Change Summary |
|------|----------------|
| `backend/app/main.py` | Added router import |
| `frontend/src/App.tsx` | Added route |
| `backend/supabase/migrations/XXX.sql` | New table |

---

## Test Results

### Automated Tests

| Suite | Result | Details |
|-------|--------|---------|
| ruff check | ✅ Pass | No issues |
| ruff format | ✅ Pass | Formatted |
| mypy | ✅ Pass | No type errors |
| pytest | ✅ 45/45 | All tests pass |
| eslint | ✅ Pass | No issues |
| tsc | ✅ Pass | No type errors |
| playwright | ✅ 20/20 | E2E tests pass |

### E2E Test Results (if run)

If `E2E-REPORT.md` exists, include summary:

| Metric | Value |
|--------|-------|
| Tests Run | {N} |
| Passed | {P} |
| Failed | {F} |
| Screenshots | {N} |
| Report | [E2E-REPORT.md](./E2E-REPORT.md) |

### Test Output

```
# pytest output
========================= test session starts ==========================
collected 45 items
tests/test_{feature}.py::test_create PASSED
tests/test_{feature}.py::test_list PASSED
...
========================= 45 passed in 2.34s ===========================
```

---

## Success Criteria

| Criterion | Status | Evidence |
|-----------|--------|----------|
| {Criterion 1 from SPEC} | ✅ | {How verified} |
| {Criterion 2 from SPEC} | ✅ | {How verified} |
| {Criterion 3 from SPEC} | ✅ | {How verified} |

---

## Manual Testing Required

### Test Case 1: {Happy Path Test}

- [ ] **Steps:**
  1. [Step 1]
  2. [Step 2]
  3. [Step 3]

- **Expected:** [What should happen]
- **Verify:** [How to check]

---

### Test Case 2: {Edge Case Test}

- [ ] **Steps:**
  1. [Step 1]
  2. [Step 2]

- **Expected:** [What should happen]
- **Verify:** [How to check]

---

### Test Case 3: {Error Handling Test}

- [ ] **Steps:**
  1. [Trigger error]
  2. [Observe]

- **Expected:** [Graceful handling]
- **Verify:** [How to check]

---

## Learnings Generated

| File | Summary |
|------|---------|
| `learnings/debugging/{date}-{slug}.md` | {What was learned} |
| `learnings/gotchas/{category}.md` | {New gotcha added} |

---

## Issues Found

### Issue 1: {If any issues found during verification}
- **Severity:** High/Medium/Low
- **Description:** [What's wrong]
- **Status:** Fixed / Open / Won't Fix
- **Resolution:** [How addressed]

---

## Performance Notes

[Any performance observations - if applicable]

- Response time: {X}ms average
- Database queries: {N} queries per request
- Bundle size impact: +{X}KB

---

## Security Checklist

- [ ] No hardcoded credentials
- [ ] Input validation in place
- [ ] RLS policies applied
- [ ] Auth required on endpoints
- [ ] No SQL injection risks
- [ ] No XSS vulnerabilities

---

## Recommendations

### Immediate (Before Merge)
- [Any blocking issues]

### Follow-up (Post-Merge)
- [Nice-to-have improvements]
- [Performance optimizations]
- [Additional test coverage]

---

## Commit Information

```bash
# Suggested commit message
feat({feature}): {Brief description}

- Add {feature} API endpoints
- Create {feature} service layer
- Add {Feature} page component
- Add database migration

FORGE: {feature-name}
```

---

*Generated by /forge:guard*
*FORGE: Ideate → Find → Outline → Review → Run → Guard*
```

---

## Completion Summary

After creating VERIFICATION.md, present:

```markdown
## FORGE Guard Complete

**Verification Report:** `$ARGUMENTS/VERIFICATION.md`

### Test Results
| Suite | Status |
|-------|--------|
| Backend Lint | ✅/❌ |
| Backend Types | ✅/❌ |
| Backend Tests | ✅/❌ |
| Frontend Lint | ✅/❌ |
| Frontend Types | ✅/❌ |
| Playwright E2E | ✅/❌ |

### Browser E2E Results (if run)
| Metric | Value |
|--------|-------|
| Status | ✅ {P}/{N} passed / ⏭️ Skipped |
| Report | [E2E-REPORT.md](./E2E-REPORT.md) |
| Screenshots | {N} in `e2e-screenshots/` |

### Success Criteria
- [X/Y] criteria verified

### Manual Testing
- [N] test cases to run manually (reduced if E2E covered them)

### Overall Status
[✅ Ready to Merge / ⚠️ Issues to Address / ❌ Failing]

### Next Steps
1. Run manual test cases
2. Review VERIFICATION.md
3. Create PR / Merge to branch
```

---

*FORGE: Ideate → Find → Outline → Review → Run → Guard*
