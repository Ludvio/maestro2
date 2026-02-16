# GROMADA DESIGN SYSTEM (UI TOKENS)

> **Version**: 1.0 (Bursztyn & Kamień)
> **SSOT**: Visual consistency across all 8-Layer phases.

## 1. Typography
- **Headings (Page Titles)**: `font-serif` (Playfair Display), `text-stone-900`. 
- **Sub-Headings (Card Titles)**: `font-bold`, `text-stone-900`.
- **Body & Controls**: `font-sans` (Outfit), `text-stone-600` or `text-stone-500` for helper text.

## 2. Color Palette
- **Primary (Action)**: `amber-600` (#d97706) | Hover: `amber-700`.
- **Background (Soft)**: `stone-50` or `white`.
- **Surface (Card)**: `bg-white` with `border-stone-200`.
- **Trust (Merit)**: `amber-100` (Background), `amber-800` (Text).
- **Security (Alert)**: `orange-600` (Warning), `red-600` (Critical).
- **System (Verified)**: `emerald-500` (#10b981).

## 3. Atomic Components (Canonical Styles)

### A. The Primary Button
```html
<button class="bg-amber-600 hover:bg-amber-700 text-white px-4 py-2 rounded-xl font-bold shadow-lg transition-all flex items-center gap-2">
```

### B. The Standard Card
```html
<div class="bg-white rounded-2xl border border-stone-200 p-5 shadow-sm hover:shadow-md transition-all">
```

### C. The Tab Switcher
```html
<div class="bg-stone-100 p-1 rounded-lg flex text-sm font-medium">
  <!-- Active Item: bg-white shadow text-stone-900 -->
  <!-- Inactive Item: text-stone-500 -->
</div>
```

### D. The Status Badge
```html
<div class="bg-stone-100 text-stone-600 text-[10px] font-bold px-3 py-1 rounded-full">
```

---
*Enforced by Maestro Orchestrator. Deviations trigger a Design Audit failure.*
