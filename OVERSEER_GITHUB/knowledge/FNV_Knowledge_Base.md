# Fallout: New Vegas Modding Knowledge Base
# Original Curated Content for Overseer Assistant
# Created for local LLM RAG system - July 2026

## Overview
This knowledge base contains original explanations of Fallout: New Vegas modding concepts. It focuses on practical diagnosis of conflicts, dirty edits, and script issues. The goal is to help the LLM give precise, actionable advice for creating stable, high-performance mod setups.

## Core Principles for Stable Modding
- **Stability First**: Always prioritize fixing crashes and broken quests over adding new features.
- **Load Order Matters**: Mods load in a specific order. Later mods override earlier ones. Conflicts happen when two mods change the same record.
- **Dirty Edits**: These are unintended changes to records that a mod shouldn't touch. They cause conflicts even when the mod author didn't mean to change anything.
- **Patches Overwrite**: The best way to resolve conflicts is usually to create a small patch mod that merges the desired changes from conflicting mods.

## Understanding Dirty Edits
A dirty edit occurs when a mod changes a record (like a CELL, NPC, or item) even though the author only intended to change something else. 

Common signs:
- xEdit shows "ITM" (Identical To Master) records — these are usually safe to remove.
- xEdit shows "UDR" (Undeleted Record) or deleted references that break quests or navmesh.
- A mod changes far more records than it should (e.g., a weapon mod also touches 200 cells).

**Fix**: Use xEdit to clean the mod. Right-click the mod → "Clean Masters" and remove ITM records where possible. For intentional changes, create a patch instead of editing the original mod.

## Load Order Rules of Thumb
1. Official DLCs and major overhaul mods (like YUP or Unofficial Patch) should load early.
2. Mods that add new content can usually load later.
3. Mods that edit the same area (e.g., two mods that change the same town) need a patch.
4. Script-heavy mods (especially those using NVSE) should be tested carefully for conflicts with other script extenders or quest mods.
5. Always check the mod author's recommended load order on the Nexus page.

## Common Conflict Types and Fixes
### Cell / Worldspace Conflicts
Two mods change the same interior or exterior cell. 
- One mod might move an object or change lighting.
- The other might add new objects or change navmesh.

**Recommended Fix**: Create a patch mod in xEdit. Copy the winning records from both mods into the patch and resolve conflicts manually.

### Quest Stage Conflicts
Two mods try to advance or check the same quest at different stages.
- This often breaks quest progression.

**Recommended Fix**: 
- Check which mod is intended to control the quest.
- Use a patch to set the correct stage or use NVSE to safely manage quest variables.

### Script / NVSE Conflicts
NVSE allows advanced scripting but can cause issues if multiple mods register the same events or modify the same form lists.

**Best Practices**:
- Use unique quest IDs or form list names when possible.
- Avoid editing vanilla quests directly — use patches or new quests.
- Test with a clean save after adding script-heavy mods.

### Item / Record Conflicts
Two mods add or change the same item, perk, or spell.
- One may override the stats or effects of the other.

**Fix**: Decide which version should win, or create a merged version in a patch.

## NVSE and Scripting Tips
- NVSE extends the console and scripting language significantly.
- Common useful functions: player.additem, setstage, getav, modav, etc.
- Always check if a mod requires a specific version of xNVSE.
- For advanced control, consider using the Improved Console mod or writing custom NVSE plugins for complex needs.

## Performance Optimization
- Large texture mods or ENB can cause stuttering on lower-end PCs.
- Use mods like New Vegas Tick Fix or Heap Replacer for better stability.
- Monitor with tools that track FPS and script load.
- Purge cell buffers (pcb command) can help in-game when stuttering occurs.

## Recommended Workflow for Troubleshooting
1. Install mods one by one and test.
2. Use xEdit to check for conflicts after adding several mods.
3. Create patches for any conflicts found.
4. Test with a new character or clean save.
5. Use the in-game console or external tools to diagnose crashes (check nvse.log and FalloutNV.log).
6. Document what each patch does.

This knowledge base will be expanded with more specific examples and patterns as the project grows. The focus remains on making modding accessible, stable, and enjoyable for the entire Fallout community.