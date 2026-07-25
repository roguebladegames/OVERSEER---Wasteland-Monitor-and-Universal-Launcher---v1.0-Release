# FNV Download Queue — Free Nexus Rebuild

Built from your `plugins.txt` vs `Data` folder (51 missing community plugins).  
Base game + DLC + preorder packs are already present — **do not redownload those**.

**What this is:** an ordered checklist so you download/install in a sane order.  
**What this is not:** an automatic Nexus/Vortex queue (I can’t log into your Nexus account or drive Vortex’s download manager).

**How to use**
1. Work **top → bottom**.  
2. On Nexus Free: open each mod page → Manual download → correct main file for **all DLC**.  
3. Drop into Vortex (or MO2) as you go; don’t sort final LO until the list is complete.  
4. Check the box when the file is in Vortex downloads / installed.

Search Nexus for the **Mod name** column if the exact page title differs slightly.

---

## Phase 0 — Script extenders & engines (do first)

These often **won’t** appear in `plugins.txt` but your list needs them.

| # | Get this | Why | Notes | Done |
|---|----------|-----|-------|------|
| 0.1 | **xNVSE** (GitHub: xNVSE/NVSE) | Required by modern FNV mods | Not on Nexus only — get current xNVSE | [ ] |
| 0.2 | **4GB Patch** / lStewieAl / heap tools if you use them | Stability | Optional but recommended | [ ] |
| 0.3 | **JIP LN NVSE Plugin** | Recipe menu, many scripts | Nexus | [ ] |
| 0.4 | **JohnnyGuitar NVSE** | Common dependency | Nexus | [ ] |
| 0.5 | **ShowOff NVSE** (if your versions ask) | Some UI/script packs | Nexus | [ ] |
| 0.6 | **Mod Configuration Menu (MCM)** | `The Mod Configuration Menu.esp` | Nexus — tiny | [ ] |
| 0.7 | **UIO - User Interface Organizer** | Helps UI mods coexist | Strongly recommended with VUI+ / MUX / LootMenu | [ ] |

---

## Phase 1 — Bugfix & foundations (small, first)

| # | Mod name (search) | Provides (your missing plugins) | ~Size | Done |
|---|-------------------|----------------------------------|------:|------|
| 1.1 | **Yukichigai Unofficial Patch - YUP** | `YUP - Base Game + All DLC.esm`, `YUP - NPC Fixes (Base Game + All DLC).esp` | S | [ ] |
| 1.2 | **Unofficial Patch NVSE Plus** | `Unofficial Patch NVSE Plus.esp` | S | [ ] |
| 1.3 | **The Mod Configuration Menu** | `The Mod Configuration Menu.esp` | S | [ ] |
| 1.4 | **JIP Improved Recipe Menu** | `JIP Improved Recipe Menu.esp` | S | [ ] |
| 1.5 | **The Weapon Mod Menu** | `The Weapon Mod Menu.esp` | S | [ ] |
| 1.6 | **LootMenu** | `LootMenu.esp` | S | [ ] |
| 1.7 | **Sprint Mod** | `Sprint Mod.esp` | S | [ ] |
| 1.8 | **Unlimited Companions** | `UnlimitedCompanions.esp` | S | [ ] |
| 1.9 | **Perk Every Level** | `PerkEveryLevel.esp` | S | [ ] |
| 1.10 | **5 Level SPECIALs** (or similarly named) | `5 Level SPECIALs.esp` | S | [ ] |
| 1.11 | **More Perks** (+ update file) | `More Perks.esm`, `More Perks Update.esp` | S | [ ] |
| 1.12 | **Alternative Start** / **AltStart** | `AltStart.esm` | S | [ ] |

---

## Phase 2 — Frameworks for bigger content

| # | Mod name (search) | Provides | ~Size | Done |
|---|-------------------|----------|------:|------|
| 2.1 | **Someguy Series** (Someguy’s framework) | `SomeguySeries.esm` | S | [ ] |
| 2.2 | **New Vegas Bounties** | `NewVegasBounties.esp` | M | [ ] |
| 2.3 | **New Vegas Bounties II** | `NewVegasBountiesII.esp` | M | [ ] |
| 2.4 | **Delilah** (companion) | `delilah.esp` | M | [ ] |
| 2.5 | **Weapon Mods Expanded - WMX** | `WeaponModsExpanded.esp` | M | [ ] |
| 2.6 | **Weapon Mesh Improvement Mod (WMIM)** | `WMIMNV.esp` | M | [ ] |

---

## Phase 3 — Big world / gameplay content

| # | Mod name (search) | Provides | ~Size | Done |
|---|-------------------|----------|------:|------|
| 3.1 | **A World of Pain (AWOP)** Preview/main | `AWorldOfPain(Preview).esm` | L | [ ] |
| 3.2 | **MoMod** / Monster Mod | `Momod.esm` | L | [ ] |
| 3.3 | **The Living Desert** *or* Travelers pack matching `TLD_Travelers.esm` | `TLD_Travelers.esm` | M–L | [ ] |
| 3.4 | **NVInteriors** (Core) | `NVInteriors_Core.esm` | M–L | [ ] |
| 3.5 | **TheLozza’s Gasmasks** | `TheLozza's_Gasmasks_V2.esp` | S–M | [ ] |

> Confirm **TLD_Travelers** on Nexus: name may be “The Living Desert” travelers plugin or a related pack — match the **exact esp/esm filename**.

---

## Phase 4 — Character overhaul (slow free download)

| # | Mod name (search) | Provides | ~Size | Done |
|---|-------------------|----------|------:|------|
| 4.1 | **Fallout Character Overhaul (FCO)** | `FCOMaster.esm`, `FCO - NPC Changes.esp` | **XL ~1.5–2 GB** | [ ] |
| 4.2 | FCO optional / patch files for your list | `FCO - Delilah.esp`, `FCO - GlowingOne.esp`, `FCO - OHSB NPC Edits.esp` | S | [ ] |
| 4.3 | (In loadorder only) **FCO - Russell** if you use Russell companion | `FCO - Russell.esp` | S | [ ] |

Download FCO overnight on free tier if needed — it’s the long pole.

---

## Phase 5 — Visuals / audio (also large)

| # | Mod name (search) | Provides | ~Size | Done |
|---|-------------------|----------|------:|------|
| 5.1 | **Vurt’s Wasteland Flora Overhaul (WFO)** | `Vurt's WFO.esp` | **XL** | [ ] |
| 5.2 | **Weapon Retexture Project (WRP)** | `Weapon Retexture Project.esp` | L | [ ] |
| 5.3 | **EVE - Essential Visual Enhancements (ALL DLC)** | `EVE FNV - ALL DLC.esp` | M–L | [ ] |
| 5.4 | **Improved Sound FX - EVE** | `Improved Sound FX - EVE.esp` | M | [ ] |
| 5.5 | **Enhanced Blood Textures** (dD) | `dD - Enhanced Blood Main NV.esp` | S–M | [ ] |
| 5.6 | **Nevada Skies** | `NevadaSkies.esp` | M | [ ] |
| 5.7 | **Atmospheric Lighting Tweaks** (+ EVE/MUX patch if separate) | `Atmospheric Lighting Tweaks.esp`, `Atmospheric Lighting Tweaks - EVEM Patch.esp` | M | [ ] |

---

## Phase 6 — Lighting suite (ILO)

| # | Mod name (search) | Provides | ~Size | Done |
|---|-------------------|----------|------:|------|
| 6.1 | **Interior Lighting Overhaul** (main / Ultimate package) | `Interior Lighting Overhaul - Core.esm`, `Interior Lighting Overhaul - L38PS.esm`, `Interior Lighting Overhaul - Ultimate Edition.esp` | M | [ ] |
| 6.2 | ILO patches from same author/page or patch hub | `ILO - PipBoy Light.esp`, `ILO - YUP Patch.esp`, `ILO - A World of Pain.esp`, `ILO - GS Shack.esp`, `ILO - New Vegas Bounties.esp`, `ILO - New Vegas Bounties II.esp` | S | [ ] |

---

## Phase 7 — UI

| # | Mod name (search) | Provides | ~Size | Done |
|---|-------------------|----------|------:|------|
| 7.1 | **Vanilla UI Plus (VUI+)** | `Vanilla UI Plus.esp` | S–M | [ ] |
| 7.2 | **M.U.X. Series - Interface Overhaul** | `M.U.X. Series - Interface Overhaul.esp` | S–M | [ ] |

Install UI after UIO + MCM. Expect FOMOD choices.

---

## Phase 8 — LOD (last content-ish)

| # | Mod name (search) | Provides | ~Size | Done |
|---|-------------------|----------|------:|------|
| 8.1 | **tmz LOD additions** (or matching name) | `tmzLODadditions.esp` | M | [ ] |
| 8.2 | **FNVLODGen** output / pregenerated LOD pack you used | `FNVLODGen.esp` | M–L | [ ] |

If you can’t find the exact old LOD pack: install everything else, then **regenerate LOD** with FNVLODGen / xLODGen later.

---

## Phase 9 — After all downloads

| Step | Done |
|------|------|
| Enable all mods in Vortex; deploy | [ ] |
| Sort load order (Vortex / LOOT rules); prefer your old order as a guide | [ ] |
| Confirm **0 missing masters** | [ ] |
| Launch with **nvse_loader.exe** | [ ] |
| New game or clean save for heavy overhauls (FCO / AWOP / MoMod) | [ ] |

### Target load-order shape (high level)

1. FalloutNV + DLCs + preorder packs (already have)  
2. YUP → other ESM frameworks (FCO, AWOP, MoMod, Someguy, NVInteriors, ILO cores, AltStart, More Perks…)  
3. Bugfix ESPs / UPNVSEP / YUP NPC Fixes  
4. Big content (NVB, Delilah, WMX, etc.)  
5. Visuals (EVE, WFO, WRP, blood, skies, ALT)  
6. ILO patches + FCO patches  
7. UI / MCM menus  
8. LOD last  

Your old `plugins.txt` order is a good **reference**, not gospel if Vortex re-sorts slightly.

---

## Free Nexus tips (no Premium)

- Start **Phase 0–2** while FCO/WFO download.  
- Queue **one large file** (FCO or WFO) before you step away.  
- Prefer **Manual** downloads so you get the right main file + optional patches.  
- Watch for **all DLC** versions (EVE, YUP, ILO).  
- Don’t install random “merged” packs unless they match **exact** plugin names above.

---

## Missing plugin checklist (raw)

Tick when the file exists again under `Data` (or Vortex staging):

- [ ] YUP - Base Game + All DLC.esm  
- [ ] YUP - NPC Fixes (Base Game + All DLC).esp  
- [ ] Unofficial Patch NVSE Plus.esp  
- [ ] Interior Lighting Overhaul - Core.esm  
- [ ] Interior Lighting Overhaul - L38PS.esm  
- [ ] Interior Lighting Overhaul - Ultimate Edition.esp  
- [ ] ILO - PipBoy Light.esp  
- [ ] ILO - YUP Patch.esp  
- [ ] ILO - A World of Pain.esp  
- [ ] ILO - GS Shack.esp  
- [ ] ILO - New Vegas Bounties.esp  
- [ ] ILO - New Vegas Bounties II.esp  
- [ ] NVInteriors_Core.esm  
- [ ] FCOMaster.esm  
- [ ] FCO - NPC Changes.esp  
- [ ] FCO - Delilah.esp  
- [ ] FCO - GlowingOne.esp  
- [ ] FCO - OHSB NPC Edits.esp  
- [ ] AWorldOfPain(Preview).esm  
- [ ] TLD_Travelers.esm  
- [ ] Momod.esm  
- [ ] SomeguySeries.esm  
- [ ] NewVegasBounties.esp  
- [ ] NewVegasBountiesII.esp  
- [ ] AltStart.esm  
- [ ] More Perks.esm  
- [ ] More Perks Update.esp  
- [ ] WMIMNV.esp  
- [ ] WeaponModsExpanded.esp  
- [ ] delilah.esp  
- [ ] TheLozza's_Gasmasks_V2.esp  
- [ ] Vurt's WFO.esp  
- [ ] Vanilla UI Plus.esp  
- [ ] M.U.X. Series - Interface Overhaul.esp  
- [ ] EVE FNV - ALL DLC.esp  
- [ ] Improved Sound FX - EVE.esp  
- [ ] Atmospheric Lighting Tweaks.esp  
- [ ] Atmospheric Lighting Tweaks - EVEM Patch.esp  
- [ ] dD - Enhanced Blood Main NV.esp  
- [ ] Weapon Retexture Project.esp  
- [ ] NevadaSkies.esp  
- [ ] Sprint Mod.esp  
- [ ] UnlimitedCompanions.esp  
- [ ] JIP Improved Recipe Menu.esp  
- [ ] 5 Level SPECIALs.esp  
- [ ] The Weapon Mod Menu.esp  
- [ ] LootMenu.esp  
- [ ] PerkEveryLevel.esp  
- [ ] The Mod Configuration Menu.esp  
- [ ] tmzLODadditions.esp  
- [ ] FNVLODGen.esp  

---

*Generated for local OVERSEER / Courier rebuild. Free community notes — not affiliated with Nexus or Bethesda.*
