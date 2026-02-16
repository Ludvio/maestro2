# FORGE: Status - Check Pipeline Progress

## Feature Folder: $ARGUMENTS

Check the current progress of a feature through the FORGE pipeline.

---

## Check Feature Status

Examine the feature folder to determine progress:

```bash
# Check what files exist
ls -la $ARGUMENTS/
```

---

## Status Detection

### Phase 0: IDEATE (Optional but Recommended)

**Complete when:**
- `$ARGUMENTS/IDEATION.md` exists
- Status in file shows "Complete - Ready for Find"

**Contains:**
- Feature definition (what it IS)
- Scope boundaries (what it is NOT)
- Success criteria
- Constraints
- Open questions for research

### Phase 1: FIND

**Complete when:**
- `$ARGUMENTS/01-find-integration.md` exists
- `$ARGUMENTS/02-find-kiss.md` exists
- `$ARGUMENTS/03-find-gotchas.md` exists
- `$ARGUMENTS/04-find-external.md` exists
- `$ARGUMENTS/BRAINSTORM.md` exists

### Phase 2: OUTLINE

**Complete when:**
- `$ARGUMENTS/SPEC.md` exists

### Phase 3: REVIEW

**Complete when:**
- `$ARGUMENTS/REVIEW.md` exists
- Review status shows APPROVED

**Blocked when:**
- Review status shows NEEDS CHANGES or BLOCKED

### Phase 4: RUN

**Two execution modes:**
- `/forge:run` - Interactive (pauses on uncertainty)
- `/forge:ralph-run` - Autonomous (self-correcting loop)

**In Progress when:**
- `$ARGUMENTS/.forge-progress.md` exists
- Progress file shows incomplete steps

**Complete when:**
- Progress file shows all steps done
- OR: Implementation files exist and pass basic checks

**Ralph Mode indicators** (in .forge-progress.md):
- `Mode: Autonomous (Ralph)` header
- Iteration count tracking
- Auto-generated learnings

### Phase 5: GUARD

**Complete when:**
- `$ARGUMENTS/VERIFICATION.md` exists
- All tests pass

---

## Output Format

```markdown
## FORGE Status: {feature-name}

**Feature Folder:** $ARGUMENTS
**Checked:** {timestamp}

### Pipeline Progress

| Phase | Status | Details |
|-------|--------|---------|
| **I**deate | ✅ Complete | IDEATION.md - scope defined |
| **F**ind | ✅ Complete | 4 reports + BRAINSTORM.md |
| **O**utline | ✅ Complete | SPEC.md created |
| **R**eview | ✅ Approved | REVIEW.md - 95% confidence |
| **R**un | ◐ In Progress | Step 3/7 |
| **G**uard | ☐ Not Started | - |

### Current Phase: RUN (Step 3/7)

**Current Step:** Backend Service
**Status:** In Progress
**Last Activity:** {timestamp}

### Files Present

```
$ARGUMENTS/
├── IDEATION.md               ✅  (Phase 0: Ideate)
├── 01-find-integration.md    ✅  (Phase 1: Find)
├── 02-find-kiss.md           ✅
├── 03-find-gotchas.md        ✅
├── 04-find-external.md       ✅
├── BRAINSTORM.md             ✅
├── SPEC.md                   ✅  (Phase 2: Outline)
├── REVIEW.md                 ✅  (Phase 3: Review)
├── .review/                  ✅
├── .forge-progress.md        ✅  (Phase 4: Run)
└── VERIFICATION.md           ☐  (Phase 5: Guard)
```

### Learnings Written
| File | Summary |
|------|---------|
| `learnings/debugging/...` | [Brief] |

### Issues/Blockers
[Any blockers or issues from progress file]

### Next Command
```bash
# Continue from current phase
/forge:run $ARGUMENTS

# Or if OUTLINE is complete but REVIEW not done
/forge:review $ARGUMENTS

# Or if RUN is complete
/forge:guard $ARGUMENTS
```
```

---

## Status Symbols

| Symbol | Meaning |
|--------|---------|
| ✅ | Complete |
| ◐ | In Progress |
| ☐ | Not Started |
| ❌ | Failed/Blocked |
| 🔄 | Continuous (Evolve) |

---

## Quick Status (All Features)

If no argument provided, show status of all features in FORGE/:

```bash
# List all feature folders
ls -d FORGE/*/
```

Output:

```markdown
## FORGE Pipeline Status

| Feature | Ideate | Find | Outline | Review | Run | Guard | Next Step |
|---------|--------|------|---------|--------|-----|-------|-----------|
| outbound-calling | ✅ | ✅ | ✅ | ✅ | ◐ | ☐ | /forge:run |
| user-profiles | ✅ | ✅ | ✅ | ☐ | ☐ | ☐ | /forge:review |
| billing-v2 | ✅ | ✅ | ☐ | ☐ | ☐ | ☐ | /forge:outline |
| new-feature | ✅ | ☐ | ☐ | ☐ | ☐ | ☐ | /forge:find |
| raw-idea | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | /forge:ideate |
```

---

*FORGE: Ideate → Find → Outline → Review → Run (or Ralph Run) → Guard*
