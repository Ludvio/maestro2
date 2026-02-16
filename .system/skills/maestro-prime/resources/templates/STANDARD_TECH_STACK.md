---
description: "The Technical Standard. Defines the MANDATORY tech stack and coding patterns."
---

# Maestro Technical Standard (The Golden Stack)

> **Context**: All implementation plans MUST adhere to this stack. Deviations require a Constitutional Amendment (ADR).

## 1. Core Framework
*   **Frontend**: React 18+ (Function Components + Hooks only).
*   **Build Tool**: Vite (Fast HMR).
*   **Language**: TypeScript 5+ (Strict Mode enabled).

## 2. State Management (The "Single Truth")
*   **Global State**: `zustand` (with persistence middleware for offline).
*   **Server State**: `@tanstack/react-query` (for external API fetching).
*   **Local State**: `useState` / `useReducer` (for simple UI toggles).
*   **Banned**: Redux, Context API (for complex state).

## 3. Styling & Biology
*   **CSS Engine**: Tailwind CSS 3+ (Utility-first).
*   **Animation**: `framer-motion` (Declarative animations).
*   **Icons**: `lucide-react` (Consistent stroke width).
*   **Class Merging**: `clsx` + `tailwind-merge` (for dynamic classes).

## 4. Architectural Patterns (The "Grodzisko Pattern")
1.  **Store-First**: Default to putting logic in `src/store/useXStore.ts`, NOT in components.
2.  **View-Model**: Components are dumb renderers; custom hooks (`useXLogic`) hold the smarts.
3.  **Idempotency**: Every critical action (`addX`, `updateY`) must accept an `idempotencyKey`.

## 5. Verification Checklist
*   [ ] Does the file use `interface` not `type` for object shapes?
*   [ ] Are all async actions wrapped in `try/catch`?
*   [ ] Is `any` type completely avoided?
