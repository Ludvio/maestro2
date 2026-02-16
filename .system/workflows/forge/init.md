# FORGE: Init - Scaffold Learnings Folder

Initialize the learnings folder structure for a new project or verify existing structure.

---

## What This Does

Creates the learnings folder hierarchy that FORGE uses for continuous learning (Evolve phase).

---

## Folder Structure to Create

```
learnings/
├── INDEX.md                    # Master index of all learnings
├── debugging/                  # RCA documents, debug sessions
│   └── .gitkeep
├── gotchas/                    # Common pitfalls by category
│   ├── .gitkeep
│   ├── database.md             # Database-related gotchas
│   ├── authentication.md       # Auth-related gotchas
│   ├── frontend.md             # Frontend gotchas
│   └── integrations.md         # External API gotchas
├── features/                   # Feature implementation notes
│   └── .gitkeep
├── patterns/                   # Successful patterns to follow
│   └── .gitkeep
└── integrations/               # External API learnings
    └── .gitkeep
```

---

## Execution

### Step 1: Create Directories

```bash
mkdir -p learnings/debugging
mkdir -p learnings/gotchas
mkdir -p learnings/features
mkdir -p learnings/patterns
mkdir -p learnings/integrations
```

### Step 2: Create .gitkeep Files

```bash
touch learnings/debugging/.gitkeep
touch learnings/features/.gitkeep
touch learnings/patterns/.gitkeep
touch learnings/integrations/.gitkeep
```

### Step 3: Create INDEX.md

**File**: `learnings/INDEX.md`

```markdown
# Learnings Index

Master index of all documented learnings, bugs, and solutions for this project.

**Last Updated:** {date}
**Total Entries:** 0

---

## Recently Added

| Date | Category | Title | File |
|------|----------|-------|------|
| - | - | No entries yet | - |

---

## Categories

### Debugging (0 entries)
Root cause analysis documents and debug sessions.

**Location:** `learnings/debugging/`

| Date | Issue | Severity | File |
|------|-------|----------|------|
| - | - | - | - |

---

### Gotchas (0 entries)
Common pitfalls and how to avoid them.

**Location:** `learnings/gotchas/`

| Category | File | Issues |
|----------|------|--------|
| Database | [database.md](./gotchas/database.md) | 0 |
| Authentication | [authentication.md](./gotchas/authentication.md) | 0 |
| Frontend | [frontend.md](./gotchas/frontend.md) | 0 |
| Integrations | [integrations.md](./gotchas/integrations.md) | 0 |

---

### Features (0 entries)
Feature implementation notes and summaries.

**Location:** `learnings/features/`

| Feature | Status | File |
|---------|--------|------|
| - | - | - |

---

### Patterns (0 entries)
Successful patterns to follow.

**Location:** `learnings/patterns/`

| Pattern | Use Case | File |
|---------|----------|------|
| - | - | - |

---

### Integrations (0 entries)
External API learnings and gotchas.

**Location:** `learnings/integrations/`

| Service | File |
|---------|------|
| - | - |

---

## How to Add Learnings

### Debugging Entry
```markdown
## {Issue Title}

**Date:** YYYY-MM-DD
**Severity:** High/Medium/Low
**Feature:** {feature-name}

### Problem
[What went wrong]

### Root Cause
[Why it happened]

### Solution
[How it was fixed]

### Prevention
[How to avoid in future]

### Files Changed
- `path/file:line`
```

### Gotcha Entry
Add to the appropriate category file (`learnings/gotchas/{category}.md`):

```markdown
## {Gotcha Title}

**Added:** YYYY-MM-DD
**Severity:** High/Medium/Low

### The Gotcha
[What catches people]

### Why It Happens
[Root cause]

### How to Avoid
[Prevention strategy]

### Example
```code
// Wrong way
...

// Right way
...
```
```

---

## Search Tips

- Search by keyword: `grep -r "keyword" learnings/`
- Find by date: Check INDEX.md "Recently Added"
- Find by severity: `grep -r "Severity: High" learnings/`
- Find by feature: `grep -r "Feature: {name}" learnings/`

---

*FORGE Learnings System*
*Updated by /forge:run when issues are encountered*
```

### Step 4: Create Gotcha Category Files

**File**: `learnings/gotchas/database.md`

```markdown
# Database Gotchas

Common database-related pitfalls and how to avoid them.

**Last Updated:** {date}
**Total Entries:** 0

---

## Index

| # | Issue | Severity | Added |
|---|-------|----------|-------|
| - | - | - | - |

---

## Entries

*No entries yet. Add gotchas as they are discovered.*

---

*Add new entries using the format in learnings/INDEX.md*
```

Create similar files for:
- `learnings/gotchas/authentication.md`
- `learnings/gotchas/frontend.md`
- `learnings/gotchas/integrations.md`

---

## If Learnings Already Exist

If `learnings/` folder already exists:

1. **Check structure** - Verify all required folders exist
2. **Add missing folders** - Create any missing directories
3. **Update INDEX.md** - Ensure it has current format
4. **Report status** - Show what exists vs what was created

---

## Completion Summary

```markdown
## FORGE Init Complete

### Learnings Structure

```
learnings/
├── INDEX.md           ✅ Created
├── debugging/         ✅ Created
├── gotchas/           ✅ Created
│   ├── database.md    ✅ Created
│   ├── authentication.md ✅ Created
│   ├── frontend.md    ✅ Created
│   └── integrations.md ✅ Created
├── features/          ✅ Created
├── patterns/          ✅ Created
└── integrations/      ✅ Created
```

### Ready for FORGE

The learnings system is ready. During `/forge:run`:
- Bugs will be documented in `learnings/debugging/`
- Gotchas will be added to `learnings/gotchas/{category}.md`
- Patterns will be saved to `learnings/patterns/`
- INDEX.md will be updated automatically

### Next Step

Start with ideation to define your feature clearly:
```bash
/forge:ideate {your rough feature idea}
```

Or if you already know exactly what you want, skip to research:
```bash
/forge:find {your feature description}
```
```

---

*FORGE: Ideate → Find → Outline → Review → Run → Guard*
