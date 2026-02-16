# FORGE: Outline - Create SPEC from Research

## Feature Folder: $ARGUMENTS

Create a comprehensive, foolproof SPEC document from the BRAINSTORM and research reports.

---

## Prerequisites

Before running this command, ensure:
- [ ] `/forge:find` has been run for this feature
- [ ] `FORGE/{feature}/BRAINSTORM.md` exists
- [ ] All 4 research reports exist (`01-find-*.md` through `04-find-*.md`)
- [ ] Open questions from BRAINSTORM have been addressed

---

## Input Files

Read these files to create the SPEC:

```bash
# Primary input (synthesized research)
READ $ARGUMENTS/BRAINSTORM.md

# Detailed reports (for reference)
READ $ARGUMENTS/01-find-integration.md
READ $ARGUMENTS/02-find-kiss.md
READ $ARGUMENTS/03-find-gotchas.md
READ $ARGUMENTS/04-find-external.md
```

---

## Output File

**File**: `$ARGUMENTS/SPEC.md`

---

## SPEC Quality Bar

The SPEC should be so complete that:
- Someone unfamiliar with the codebase could implement it
- Every file path is exact (no "similar files" references)
- Every step has clear validation criteria
- All gotchas from learnings are addressed with prevention
- Success criteria are measurable and testable
- Rollback plan is clear if things go wrong

---

## SPEC.md Template

```markdown
# SPEC: {Feature Name}

**Created:** {timestamp}
**Feature Folder:** $ARGUMENTS
**Status:** Ready for Implementation

---

## References

Research documents that informed this SPEC:

- [BRAINSTORM](./BRAINSTORM.md) - Synthesized research summary
- [Integration Points](./01-find-integration.md) - Where feature connects
- [KISS Approach](./02-find-kiss.md) - Simplest implementation path
- [Gotchas & History](./03-find-gotchas.md) - Known pitfalls to avoid
- [External Context](./04-find-external.md) - External dependencies

---

## Goal

[Clear, measurable 1-2 sentence goal for this feature]

---

## Success Criteria

When implementation is complete, ALL of these must be true:

- [ ] **[Criterion 1]**: [How to verify]
- [ ] **[Criterion 2]**: [How to verify]
- [ ] **[Criterion 3]**: [How to verify]
- [ ] **[Criterion 4]**: [How to verify]

---

## Implementation Blueprint

### Files to Create

| File | Purpose | Pattern Reference |
|------|---------|-------------------|
| `backend/app/{feature}/router.py` | [Purpose] | Similar to `backend/app/{existing}/router.py` |
| `backend/app/{feature}/service.py` | [Purpose] | Similar to `backend/app/{existing}/service.py` |
| `backend/app/{feature}/schemas.py` | [Purpose] | Similar to `backend/app/{existing}/schemas.py` |
| `frontend/src/pages/{Feature}.tsx` | [Purpose] | Similar to `frontend/src/pages/{Existing}.tsx` |

### Files to Modify

| File | Change | Line Reference | Why |
|------|--------|----------------|-----|
| `backend/app/main.py` | Add router import | ~line 20 | Register new endpoints |
| `frontend/src/App.tsx` | Add route | ~line 45 | Add navigation |
| `backend/supabase/migrations/XXX.sql` | Create table | New file | Database schema |

### Database Changes

```sql
-- Migration: XXX_{feature_name}.sql

-- Table: {table_name}
CREATE TABLE {table_name} (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    -- [columns]
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- RLS Policies
ALTER TABLE {table_name} ENABLE ROW LEVEL SECURITY;

CREATE POLICY "{table_name}_tenant_isolation" ON {table_name}
    FOR ALL USING (tenant_id = current_setting('app.tenant_id')::uuid);

-- Indexes
CREATE INDEX idx_{table_name}_tenant ON {table_name}(tenant_id);
```

---

## Implementation Steps

Follow these steps in order. Each step should produce testable, working code.

### Step 1: [Database Schema]

**Description:** [What this step accomplishes]

**Files:**
- Create: `backend/supabase/migrations/XXX_{feature}.sql`

**Actions:**
1. Create the migration file with schema above
2. Run migration: `supabase db push` or apply manually

**Validation:**
```bash
# Verify table exists
psql -c "SELECT * FROM {table_name} LIMIT 1;"
```

**Depends on:** Nothing (first step)

---

### Step 2: [Backend Schemas]

**Description:** [What this step accomplishes]

**Files:**
- Create: `backend/app/{feature}/schemas.py`

**Actions:**
1. Create Pydantic models for request/response
2. Follow pattern from `backend/app/{existing}/schemas.py`

**Code Pattern:**
```python
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class {Feature}Create(BaseModel):
    # Request fields
    pass

class {Feature}Response(BaseModel):
    id: UUID
    tenant_id: UUID
    created_at: datetime
    # Response fields

    class Config:
        from_attributes = True
```

**Validation:**
```bash
cd backend && uv run python -c "from app.{feature}.schemas import *; print('OK')"
```

**Depends on:** Step 1

---

### Step 3: [Backend Service]

**Description:** [What this step accomplishes]

**Files:**
- Create: `backend/app/{feature}/service.py`

**Actions:**
1. Create service class with CRUD operations
2. Use `get_supabase_admin()` (NOT async client - see gotchas)
3. Follow pattern from `backend/app/{existing}/service.py`

**Code Pattern:**
```python
from uuid import UUID
from ..database import get_supabase_admin

class {Feature}Service:
    @staticmethod
    def create(tenant_id: UUID, data: dict) -> dict:
        # PATTERN: Use sync client for admin operations (RLS bug workaround)
        client = get_supabase_admin()
        result = client.table("{table}").insert({
            "tenant_id": str(tenant_id),
            **data
        }).execute()
        return result.data[0] if result.data else None
```

**Validation:**
```bash
cd backend && uv run python -c "from app.{feature}.service import *; print('OK')"
```

**Depends on:** Step 2

---

### Step 4: [Backend Router]

**Description:** [What this step accomplishes]

**Files:**
- Create: `backend/app/{feature}/router.py`
- Modify: `backend/app/main.py` (add import and include_router)

**Actions:**
1. Create FastAPI router with endpoints
2. Use dependencies for auth: `get_current_user`, `get_current_tenant_id`
3. Register router in main.py

**Code Pattern:**
```python
from fastapi import APIRouter, Depends
from uuid import UUID
from ..dependencies import get_current_user, get_current_tenant_id
from .schemas import {Feature}Create, {Feature}Response
from .service import {Feature}Service

router = APIRouter(prefix="/{feature}", tags=["{feature}"])

@router.post("/", response_model={Feature}Response)
async def create_{feature}(
    request: {Feature}Create,
    current_user: dict = Depends(get_current_user),
    tenant_id: UUID = Depends(get_current_tenant_id),
):
    return {Feature}Service.create(tenant_id, request.model_dump())
```

**Validation:**
```bash
cd backend && uv run uvicorn app.main:app --reload
# Test endpoint: curl http://localhost:8000/{feature}/
```

**Depends on:** Step 3

---

### Step 5: [Frontend API Client]

**Description:** [What this step accomplishes]

**Files:**
- Create: `frontend/src/api/{feature}.ts`

**Actions:**
1. Create API client functions
2. Follow pattern from `frontend/src/api/{existing}.ts`

**Code Pattern:**
```typescript
import { apiClient } from './client';

export interface {Feature} {
  id: string;
  tenant_id: string;
  // fields
}

export const {feature}Api = {
  list: async (): Promise<{Feature}[]> => {
    const response = await apiClient.get('/{feature}/');
    return response.data;
  },

  create: async (data: Partial<{Feature}>): Promise<{Feature}> => {
    const response = await apiClient.post('/{feature}/', data);
    return response.data;
  },
};
```

**Validation:**
```bash
cd frontend && npx tsc --noEmit
```

**Depends on:** Step 4

---

### Step 6: [Frontend Page/Component]

**Description:** [What this step accomplishes]

**Files:**
- Create: `frontend/src/pages/{Feature}.tsx`
- Modify: `frontend/src/App.tsx` (add route)

**Actions:**
1. Create page component with React Query hooks
2. Add route in App.tsx
3. Follow pattern from `frontend/src/pages/{Existing}.tsx`

**Code Pattern:**
```typescript
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { {feature}Api } from '../api/{feature}';

export default function {Feature}Page() {
  const queryClient = useQueryClient();

  const { data, isLoading, error } = useQuery({
    queryKey: ['{feature}'],
    queryFn: {feature}Api.list,
  });

  // Component JSX
}
```

**Validation:**
```bash
cd frontend && npm run dev
# Navigate to /{feature} in browser
```

**Depends on:** Step 5

---

## Gotchas & Prevention

| Risk | Mitigation | Reference |
|------|------------|-----------|
| Async Supabase client returns empty | Use `get_supabase_admin()` NOT `get_supabase_async()` | learnings/database-rls.md |
| Auth state not synced | Update both AuthContext AND useAuthStore | learnings/authentication.md |
| [Risk from research] | [Prevention strategy] | [learnings file] |

---

## Validation Commands

### After Each Step
```bash
# Backend type check
cd backend && uv run mypy app/

# Frontend type check
cd frontend && npx tsc --noEmit
```

### Final Validation
```bash
# Full backend check
cd backend && uv run ruff check . && uv run mypy app/ && uv run pytest tests/ -v

# Full frontend check
cd frontend && npm run lint && npx tsc --noEmit

# E2E tests (if applicable)
cd frontend && npm run test:e2e
```

---

## Rollback Plan

If implementation fails or introduces bugs:

1. **Database:** Drop migration
   ```sql
   DROP TABLE IF EXISTS {table_name} CASCADE;
   ```

2. **Backend:** Remove files
   ```bash
   rm -rf backend/app/{feature}/
   # Revert main.py changes
   ```

3. **Frontend:** Remove files
   ```bash
   rm -rf frontend/src/pages/{Feature}.tsx
   rm -rf frontend/src/api/{feature}.ts
   # Revert App.tsx changes
   ```

4. **Git:** Revert to previous commit
   ```bash
   git checkout HEAD~1 -- .
   ```

---

## Next Steps

After SPEC is created:

```bash
# Validate SPEC before implementation
/forge:review $ARGUMENTS

# Execute implementation (after review passes)
/forge:run $ARGUMENTS

# Verify implementation
/forge:guard $ARGUMENTS
```

---

*Generated by /forge:outline*
*FORGE: Ideate → Find → Outline → Review → Run → Guard*
```

---

## Completion Summary

After creating SPEC.md, present:

```markdown
## FORGE Outline Complete

**SPEC Created:** `$ARGUMENTS/SPEC.md`

### Summary
- **Goal:** [Feature goal]
- **Files to Create:** [count] new files
- **Files to Modify:** [count] existing files
- **Implementation Steps:** [count] steps
- **Gotchas Addressed:** [count] risks mitigated

### Ready for Validation

Review the SPEC, then validate before implementation:
```bash
/forge:review $ARGUMENTS
```
```
