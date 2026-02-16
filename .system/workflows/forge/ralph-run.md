# FORGE: Ralph Run - Autonomous SPEC Execution

## Feature Folder: $ARGUMENTS

Execute an approved SPEC autonomously using Ralph-style iteration.

---

## Prerequisites

- `/forge:review` has passed (APPROVED status)
- `$ARGUMENTS/SPEC.md` exists
- User has approved the SPEC

---

## Cost Warning

Ralph loops consume tokens rapidly:
- Simple SPEC (3-5 steps): $10-30
- Medium SPEC (6-10 steps): $30-75
- Complex SPEC (10+ steps): $75-150+

---

## Execution Instructions

### 1. Parse Arguments

Extract from $ARGUMENTS:
- **feature_folder**: The FORGE feature folder path (e.g., `FORGE/billing-ux`)
- **--max-iterations**: Maximum iterations (default: 25)
- **--resume**: If present, resume from last completed step

### 2. Load SPEC

```
READ {feature_folder}/SPEC.md
```

Count total steps. Verify SPEC is complete.

### 3. Create/Update Progress File

Write to `{feature_folder}/.forge-progress.md`:

```markdown
# FORGE Ralph Run Progress

**Started:** {current timestamp}
**Mode:** Autonomous (Ralph)
**SPEC:** {feature_folder}/SPEC.md
**Status:** In Progress
**Max Iterations:** {max_iterations}

## Steps

| Step | Status | Notes |
|------|--------|-------|
| 1 | Pending | |
| 2 | Pending | |
(list all steps from SPEC)

## Iteration Log

| # | Action | Result |
|---|--------|--------|
```

### 4. Start Ralph Loop

Run this bash command (substitute actual values for the placeholders):

```bash
.agent/plugins/ralph-wiggum/scripts/setup-ralph-loop.sh \
  "Execute FORGE SPEC. Feature: {feature_folder}. Read {feature_folder}/SPEC.md and implement each step in order. After each step run its validation command. If validation fails, check learnings/INDEX.md for solutions, fix, and retry. Update {feature_folder}/.forge-progress.md after each action. When ALL steps complete and validated, output: <promise>FORGE SPEC COMPLETE</promise>" \
  --completion-promise "FORGE SPEC COMPLETE" \
  --max-iterations {max_iterations}
```

### 5. Begin Autonomous Execution

After the Ralph loop starts, work through the SPEC:

**For each step:**
1. Read step requirements from SPEC
2. Implement the changes
3. Run the validation command from SPEC
4. **If validation passes:**
   - Update progress file: mark step Done
   - Continue to next step
5. **If validation fails:**
   - Read the error message
   - Check `learnings/INDEX.md` for similar issues
   - Apply fix
   - Re-run validation
   - If you discover a new bug/gotcha, write to `learnings/debugging/`

**Update progress file after each significant action.**

### 6. Completion

When all SPEC steps are complete and validated:

1. Update progress file: `Status: Complete`
2. Output the completion promise exactly:

```
<promise>FORGE SPEC COMPLETE</promise>
```

3. The Ralph loop will detect this and exit
4. Report summary and run `/forge:guard {feature_folder}`

### 7. If Max Iterations Reached

If max iterations hit before completion:
- DO NOT output false completion promise
- Document what's blocking in progress file
- Loop exits automatically
- Report partial progress

---

## Resume Mode

If `--resume` flag is present:

1. Read `{feature_folder}/.forge-progress.md`
2. Find last completed step
3. Modify the Ralph prompt to start from next step
4. Continue execution

---

## Example Usage

```bash
# Standard run
/forge:ralph-run FORGE/call-intelligence --max-iterations 30

# Resume stopped run
/forge:ralph-run FORGE/call-intelligence --resume

# Quick run with low limit
/forge:ralph-run FORGE/small-fix --max-iterations 10
```

---

*FORGE: Find -> Outline -> Review -> Ralph Run -> Guard*
