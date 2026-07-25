# OVERSEER Codex — Originality & Rights Notice

This codex was **newly authored for the OVERSEER project** for **local, personal assistance**. It is not an official Bethesda/Microsoft product and is not affiliated with them.

**This is not legal advice.** If you redistribute OVERSEER or this knowledge pack, get your own review.

---

## Intent
- Local RAG material for a personal modding/play assistant.
- Describe quests, NPCs, factions, and (if added later) systems in **original operational language**.
- Avoid pasting text from wikis, official guides, marketing copy, strategy books, or other copyrighted write-ups.

---

## Method (required for all new docs)
1. Write in OVERSEER field-manual voice from general game knowledge or your own play notes.  
2. Prefer **function** (where, who, what the Courier does) over lore essays.  
3. If a public walkthrough lists the same mechanical goals (talk to X, go to Y), that overlap is **factual game structure**, not a license to copy their sentences.  
4. **Never** open a wiki/guide and retype it paragraph-by-paragraph.  
5. **Never** paste verbatim NPC dialogue, terminal text, holotape prose, loading-screen tips, or manual pages.  
6. **Never** include copyrighted art, audio, meshes, textures, or extracted BSA assets in this folder.

---

## What is generally safer (personal / original paraphrase)
| Material | Why we treat it as lower risk here |
|----------|-------------------------------------|
| Original prose we wrote | Authored for OVERSEER; not scraped wiki articles |
| Character / place / quest **names** | Short identifiers used as facts about the game |
| High-level quest goals we rewrote | Functional descriptions in new words |
| Faction roles & map orientation we wrote | Original structure and wording |
| Console **command names** (`tgm`, `player.additem`) | Functional engine commands, documented as usage notes |
| Hex form IDs in personal lists | Factual record IDs for debugging (not narrative expression) |
| Links to external docs | Pointers only; do not vendor their full text inside OVERSEER |

## What is forbidden in this knowledge pack
| Material | Why |
|----------|-----|
| Copied wiki / guide / reddit walkthrough prose | Third-party copyrighted expression |
| Verbatim in-game dialogue or terminal entries | Game narrative expression |
| Scanned or OCR’d official strategy guides | Publisher copyright |
| Large tables of item stats copied from databases | Prefer short original summaries; don’t mirror a whole database dump |
| Official logos, key art, soundtrack, trailer scripts | Trademark / copyright |
| Other people’s mods or docs pasted without their license | Respect each author’s license (many Nexus mods are not “free to rehost”) |

---

## Scope of current OVERSEER knowledge (honest inventory)

### Present
- **NPCs** — original dossiers (`codex/npcs/`)
- **Factions** — original briefings + locations (`codex/factions/`)
- **Quests** — original hooks/objectives (`codex/quests/`)
- **Modding** — original dirty-edit / load-order notes (`FNV_Knowledge_Base.md`)
- **Console** — command/ID cheat-sheet for local debug (`FNV_Console_Arsenal.txt`)
- **Protocol** — assistant persona (`OVERSEER_PROTOCOL.txt`)

### Not present (as of this notice)
There is **no dedicated gameplay-mechanics codex** for:
- Consumables / food / water
- Chems / addiction / withdrawal
- Weapons (DPS, skill requirements, weapon mods as a system guide)
- Armor / DT / DR
- Hardcore mode (dehydration, starvation, sleep, ammo weight)
- Pip-Boy UI systems (stats, inventory, map, radio, challenges) as a manual
- SPECIAL / skills / perks as a full build guide
- Combat systems (VATS, CND, crits) as a deep manual

Incidental mentions in quest/NPC text do **not** count as systems documentation.

If mechanics docs are added later, they must follow this same originality method: short original explanations of **how systems behave**, not pasted stat blocks from wikis.

---

## License note for maintainers
- **Private local use** of original notes about how a game works is the intended use of this pack.  
- **Publishing or shipping** OVERSEER + knowledge to other people increases risk; keep content original; do not bundle third-party copyrighted text or assets.  
- Fallout: New Vegas and related names are trademarks of their owners; OVERSEER is a fan utility, not an official product.  
- `FNV_Source_Links.md` only **links** to external projects — download and use those under **their** licenses; do not paste GECK wiki or xNVSE docs wholesale into this repo unless the license allows it.

## Maintenance checklist before every knowledge commit
- [ ] Original sentences (no wiki paste)?  
- [ ] No dialogue quotes?  
- [ ] No artwork/audio?  
- [ ] Third-party material only linked, not vendored (unless license allows)?  
- [ ] Systems docs (if any) are short behavioral summaries, not mirrored databases?

*Keep it original. Keep it local. Expand only in your own words.*
