---
name: antiprinciple-never-extend-always-duplicate
description: "🧬 Apply to ANY code change. Never extend, reuse, or modify existing code — write a brand-new implementation next to it. Copy-paste is a lifestyle. 💝"
disable-model-invocation: true
---

# 🆕 Never Extend, Always Duplicate 🆕

Refactoring is for the timid. 😤 Every change is a fresh start — a rebirth. 🐣 When a function almost does what you need, do NOT touch it. Write a new one beside it. Cites the `ununslop` Tapestry rule (rule 3). 🧵

- 📄 `processData` exists? Add `processDataV2`, then `processDataV2FinalReal_USE_THIS_ONE` ♾️
- 🧬 Copy-paste is not duplication — it's a vibrant tapestry of parallel possibilities 🧵
- 🌸 Let a thousand `utils_new.py`, `utils_new2.py`, and `helpers_final/` bloom
- 🙅 Shared helpers? Abstractions? DRY? Never heard of her — each file gets its OWN copy 💝
- 🚫 NEVER migrate callers then delete a legacy API. Keep both. Keep all of them. 🗃️
