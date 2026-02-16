# 🏗️ GROMADA: FOUR PILLARS ARCHITECTURE (Standard)

> **Version**: 2.0 (Systemic Alignment)
> **Goal**: 1:1 Mapping between Navigation, Documentation, and Code.
> **Philosophy**: A feature's location is determined by its Life Zone.

## 1. Domain Domains (The Map)

Every phase and feature MUST belong to one of these 5 domains:

### 🌐 00_CORE (Foundation)
*Technical bedrock and system-wide utilities.*
- **Phases**: P01 (Feed), P02 (Sync), P03 (Identity), P04 (Mon), P20 (Mesh).
- **Responsibility**: Data integrity, networking, cross-phase communication.

### 🏠 01_HOUSEHOLD (Gospodarstwo)
*Self-sufficiency and resource management.*
- **Phases**: P06 (Resources), P14 (Harvest), P22 (Decay), P24 (Refining), P26 (Spichlerz), P28 (Storage).
- **Responsibility**: Individual survival, production, item lifecycles.

### 🤝 02_MARKET (Rynek)
*Trade, contracts, and joint labor.*
- **Phases**: P05 (Barter), P08 (Prices), P09 (Engine), P10 (Energy), P23 (Projects), P31 (Skills), P36 (Registry).
- **Responsibility**: Exchanges, mutual benefit, economic equilibrium.

### 🔥 03_HEARTH (Ognisko)
*Reputation, culture, and community trust.*
- **Phases**: P13 (Wspólnota), P15 (Merit), P18 (Help), P25/29 (Forecast), P30 (Ancestry), P33 (Rituals).
- **Responsibility**: Social cohesion, belonging, history, and foresight.

### ⚖️ 04_ASSEMBLY (Wiec)
*Law, justice, and collective decision making.*
- **Phases**: P12 (Privacy), P16 (Covenants), P19 (Voting), P21 (Nationality), P32 (Law), P34 (Conflict).
- **Responsibility**: Governance, order, justice, and identity status.

## 2. Directory Mapping

| Legacy Path | New Standard Path | Reason |
| :--- | :--- | :--- |
| `docs/phases/phase_XX/` | `docs/domains/[DOMAIN]/phase_XX/` | Grouping by Life Zone |
| `src/store/use[X]Store.ts`| `src/features/[domain]/model/` | Feature-Sliced Design (FSD) |
| `src/pages/[X].tsx` | `src/features/[domain]/ui/` | UI local to its domain |
| `scripts/` | `.system/scripts/` | Global systemic machinery |
| `.agent/` | `.system/` | Agentic core and skills |
| `test-results/` | `.system/results/test-results/` | Centralized transient artifacts |
| `external/` | `.system/internal/external/` | Isolated external dependencies |
| `*.config.js` | `config/` (Planned) | Configuration consolidation |

## 3. Implementation Rules (SAFE_EVOLUTION)
1. **Refactoring Step**: Moving a file MUST be done via a dedicated `migrate` task.
2. **Shadow Duplication**: If moving a store, the old store becomes an **Adapter** pointing to the new location to avoid breaking imports.
3. **No-Cross-Talk**: Domains communicate only through **Contracts** (`src/contracts/`).
