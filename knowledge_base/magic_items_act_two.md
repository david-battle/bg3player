# Baldur's Gate 3 - Magic Items in Act Two

Full reference for every magic equipment item obtainable in this act, sorted by in-game location. Coordinates (X, Y) are in-game map coordinates.


## Campsite (Act Two)

### Jhannyl's Gloves
- Rarity: Rare | Slot: Gloves | Act: Act Two
- Description: Jhannyl's Gloves are a rare pair of Gloves that let the wearer automatically cast Lesser Restoration on themselves when they become Blinded, Paralysed or Poisoned.
- Effect: Defy Villainy: When the wearer becomes Blinded, Paralysed or Poisoned, they automatically cast Lesser Restoration on themselves. | Saving Throws +1
- How to get:
  - Last Light Inn X: -60 Y: 158: Worn by Isobel if she is killed after dealing with the Nightsong but before completing the assault on Moonrise
  - Mind Flayer Colony X: 861 Y: -23: Worn by Isobel if she is kidnapped by Marcus or killed at Last Light Inn before dealing with the Nightsong
  - Ramazith's Tower: Worn by Isobel if the Nightsong is killed or imprisoned by Lorroakan
  - Campsite (Act Two): Worn by Isobel if she joins the camp
  - Worn by Isobel if she joins the camp
- Notes:
  - Likely related to Jhannyl's wristlet, a magic item also used by the Harpers.
  - Despite the description, this passive protects from every condition in Diseased, Poisoned, Paralyzed, and Blinded condition groups, plus Bloodless.
  - Prior to Patch 8, this passive had a once-per-long-rest limit, but it was removed and can now trigger an unlimited number of times.
  - Although Jhannyl's Gloves are associated with Isobel (and equipped by her in certain Act Two encounters) the passive from these gloves is hardcoded to function only for player characters, recruited companions, and hirelings. Therefore Isobel cannot make use of this passive's benefits.
- Bugs:
  - This passive emulates Lesser Restoration spell effects without actually casting it, which would trigger effects like Tempestuous Magic: Flight or restore Arcane Ward charges.

### Moon Devotion Robe
- Rarity: Very Rare | Slot: Clothing | Act: Act Two
- Description: Moon Devotion Robe is a very rare piece of Clothing. It grants Advantage on Constitution Saving Throws as well as the ability to cast Produce Flame and Lunar Bulwark.
- Effect: AC 10 | Lunar Bulwark: Bathe yourself in the shielding magic of Selûne's watchful gaze. (Recharge: Long rest.) | Produce Flame: A flame in your hand sheds a light in a 9 m (30 ft) radius and deals 1d8 Fire damage when thrown. | Selûne's Protection: While the wearer has Mage Armour, each successful Saving Throw causes the source of the Saving Throw to take 1d4 Radiant damage. | File ARM_Isobel_A_Pants | File ARM_Isobel_A_Robe_Skirt_B | Advantage on Constitution Saving Throws. | Saving Throws +1
- How to get:
  - Last Light Inn X: -60 Y: 158: Worn by Isobel after dealing with the Nightsong but before completing the assault on Moonrise Towers
  - Mind Flayer Colony X: 861 Y: -23: Worn by Isobel after being kidnapped by Marcus
  - Ramazith's Tower: Worn by Isobel if the Nightsong is killed or imprisoned by Lorroakan
  - Campsite (Act Two): Worn by Isobel as Camp Follower
  - Worn by Isobel as Camp Follower
- Notes:
  - The Produce Flame cantrip granted by the robes always uses Wisdom as the casting ability, regardless of the class' casting ability.
- Bugs:
  - Although Selûne's Protection should be activated by Lunar Bulwark, it is not; the wearer must instead have the regular version of Mage Armour cast on them for its radiant damage to function.
  - Additionally, although the tooltip mentions saving throws without any additional qualifiers, this does not work for saving throws rolled against non-spell effects such as weapon actions. As mentioned in the summary on this page, only successful saves against spells trigger the radiant damage.

### Shadow Blade Ring
- Rarity: Uncommon | Slot: Ring | Act: Act Two
- Description: Shadow Blade Ring is an uncommon Ring that grants its wearer the ability to cast Shadow Blade. It is a reward for completing the quest Find Arabella's Parents.
- Effect: Shadow Blade: Cast as a level 2 spell (Recharge: Short rest.)
- How to get:
  - Campsite (Act Two): Rewarded by Arabella for completing the quest Find Arabella's Parents
  - Rewarded by Arabella for completing the quest Find Arabella's Parents
- Notes:
  - The spell does not require concentration anymore and the conjured blade lasts until long rest. As a result, the ring can produce multiple shadow blades - one per each short rest.
  - The ring can be unequipped after summoning the shadow blade.
  - The ring's shadow blade can be summoned and equipped in addition to one summoned using spell slots.
  - The ring's shadow blade can also be transferred between characters and equipped by anyone in the party, or even dropped on the ground without it de-spawning, meaning that it can have spells and other effects cast upon it, such as Draconic Elemental Weapon granted by the Drakethroat Glaive.
- Bugs:
  - Unequipping this ring will break the character's current Concentration spell so long as the shadow blade is currently summoned.
  - Due to a miscoded Summon InInventory functor: The ring's shadow blade can be: Transferred between characters and equipped by anyone in the party,
  - Dropped on the ground without it de-spawning.
  - Previously conjured blades do not disappear from the caster's inventory upon a new spell casting.


## Gauntlet of Shar

### Boots of Brilliance
- Rarity: Rare | Slot: Boots | Act: Act Two
- Description: Boots of Brilliance are a rare pair of Boots that allow the wearer to replenish one Bardic Inspiration charge once per long rest.
- Effect: Restore Bardic Inspiration: Play your instrument to restore one of your Bardic Inspiration slots. (Recharge: Long rest.)
- How to get:
  - Gauntlet of Shar X: -632 Y: -723: In a heavy chest in the room just north of Yurgir
  - In a heavy chest in the room just north of Yurgir
- Notes:
  - In Early Access, these were dropped by a Mimic in Grymforge. In the final release, that Mimic now drops Wondrous Gloves.

### Callous Glow Ring
- Rarity: Uncommon | Slot: Ring | Act: Act Two
- Description: Callous Glow Ring is an uncommon Ring that deals an additional 2 Radiant damage whenever the wearer deals damage to illuminated creatures.
- Effect: Callous Glow: The wearer deals an additional 2 points of Radiant damage against creatures that are illuminated.
- How to get:
  - Gauntlet of Shar X: -821 Y: -752: in an opulent chest in the vault room near Balthazar
  - in an opulent chest in the vault room near Balthazar
- Notes:
  - This ring has synergy with the Coruscation Ring, which applies Radiating Orb to targets when they take damage from a spell. This means that each damaging spell applies Radiating Orb to a target, which in turn becomes illuminated – and thus takes an additional 2 Radiant damage.
  - The effect requires the target to be standing in a light level of Clear Area.
  - Actions and spells that deal multiple instances of damage, like Flurry of Blows, Magic Missile, or Scorching Ray, apply the additional damage to each instance.
  - The 2 Radiant damage is added to almost all damage sources originating from the wearer. Examples include Phalar Aluve: Shriek, a Void Bulb, Electrified Water, and even self-damage from Psionic Overload.
- Bugs:
  - The in-game tooltip does not specify the damage type, but it is Radiant damage.

### Circle of Bones
- Rarity: Rare | Slot: Helmet | Act: Act Two
- Description: Circle of Bones is a rare Circlet that grants all nearby allied undead Resistance to physical damage, and the wearer can cast Animate Dead once per Long Rest.
- Effect: Animate Dead: Cast as a level 3 spell (Recharge: Long rest.) | Undead Ward: Allied undead within 6 m (20 ft) are Resistant to Bludgeoning, Slashing, and Piercing damage.
- How to get:
  - Gauntlet of Shar X: -845 Y: -793: Carried by Balthazar, at his altar
  - Shadowfell X: -604 Y: -1431: Carried by Balthazar, if he is later confronted near the Nightsong
  - Mind Flayer Colony X: 715 Y: -49: Carried by Balthazar, if he is allowed to abduct the Nightsong
  - Carried by Balthazar, at his altar
- Notes:
  - The Undead Ward feature does not apply to Astarion but does apply to another vampire if one is in the party, even though they do not have the Undead tag.
- Bugs:
  - Summoning a zombie via this item's version of Animate Dead incorrectly summons a Newborn Zombie, which begins decaying, instead of the normal Zombie.
  - Though it is not stated in the tooltip, Undead Ward applies to summoned fiends, such as Shovel, Cambion (Planar Ally), and Conjured Imp.
  - Though Undead Ward states it has a radius of 6 m (20 ft), it actually has a radius of 9 m (30 ft).

### Dark Justiciar Gauntlets (Uncommon)
- Rarity: Uncommon | Slot: Gloves | Act: Act Two
- Description: The Dark Justiciar Gauntlets are an uncommon pair of Gloves that cause weapon attacks to deal an additional 1d4 Necrotic damage.
- Effect: Umbral Attack: Your weapon attacks deal an additional 1d4 Necrotic damage. | Strength Saving Throws +1
- How to get:
  - Gauntlet of Shar X: -660 Y: -760: on a pile of boxes, near Yurgir
  - on a pile of boxes, near Yurgir
- Notes:
  - Umbral Attack also works on Throw attacks.

### Dark Justiciar Half-Plate (Rare)
- Rarity: Rare | Slot: Medium Armour (Medium) | Act: Act Two
- Description: Dark Justiciar Half-Plate is a rare Medium Armour that grants Advantage on Stealth checks while Obscured in shadow. It also grants Advantage on Constitution Saving Throws and allows its wearer to cast a version of Shield of Faith once per Long Rest.
- Effect: AC 16 | Shar's Aegis: Encase yourself with a shimmering field of magic that increases your Armour Class by 2. (Recharge: Long rest.) | Shar's Umbrae: While obscured, the wearer has Advantage on Stealth Checks. | File ARM_Dark_Dark_Justiciar_A_Pants | Advantage on Constitution Saving Throws.
- How to get:
  - Gauntlet of Shar X: -818 Y: -755: Lying on the ground next to the altar where the Spear of Night rests, beyond the riddle door in the Silent Library
  - Lying on the ground next to the altar where the Spear of Night rests, beyond the riddle door in the Silent Library
- Bugs:
  - Due to a coding error, the damage reduction portion of Sharran Retribution is also applied to the wearer of this armour when they cast Shar's Aegis on themselves.
  - Shar's Umbrae applies its Advantage on Stealth checks without any obscurity level checks, even if in a Clear Area.

### Dark Justiciar Helmet
- Rarity: Very Rare | Slot: Helmet | Act: Act Two
- Description: The Dark Justiciar Helmet is a very rare Helmet that improves the wearer's Saving Throws against Spells and makes Critical Hits more likely while the wearer is obscured by darkness.
- Effect: Magical Durability: The wielder has a +1 bonus to Saving Throws against spells. | Covert Critical: While obscured, the number you need to roll a Critical Hit while attacking is reduced by 1. This effect can stack. | Constitution Saving Throws +1
- How to get:
  - Gauntlet of Shar X: -822 Y: -753: inside a Gilded Chest behind the altar and beyond the riddle door in the Silent Library
  - inside a Gilded Chest behind the altar and beyond the riddle door in the Silent Library

### Hellfire Hand Crossbow
- Rarity: Very Rare | Slot: Weapon (Hand_Crossbows) | Act: Act Two
- Description: Hellfire Hand Crossbow is a very rare +2 Hand Crossbow that has a chance to set targets burning when attacking while Hiding or Invisible.
- Effect: Damage: 1d6 + 2 (3~8) + Dexterity modifier Piercing | Scorching Ray Shot: Cast as a level 3 spell (Recharge: Short rest.) | Hellstalker: Possibly inflict Burning when attacking while Hiding or Invisible. | Piercing Shot: Deal regular damage and possibly inflict Gaping Wounds which cause extra damage on attacks. (Recharge: Short rest.) | Mobile Shot: After using Dash or Disengage this turn, you can make a ranged attack as a bonus action. (Recharge: Short rest.)
- How to get:
  - Gauntlet of Shar X: -653 Y: -764: Carried by Yurgir
  - Carried by Yurgir
- Notes:
  - Obtaining the crossbow grants the Tools of the Trade inspiration to party members with the Outlander background.
- Bugs:
  - The saving throw for Hellstalker generally does not show in the combat log.

### Justiciar's Greatshield
- Rarity: Rare | Slot: Shield | Act: Act Two
- Description: Justiciar's Greatshield is a rare Shield that allows the wielder to cast Darkness Cloak to hide themselves, and gains advantage on Perception checks.
- Effect: AC +2 | Darkness Cloak: Create a cloud of magical darkness and immediately attempt to Hide. (Recharge: Short rest.) | Shield Bash: When a foe hits you with a melee attack, you can use your reaction to knock it Prone unless they succeed a Dexterity Saving Throw. | Advantage on Perception Ability Checks.
- How to get:
  - Gauntlet of Shar X: -713 Y: -732: Carried by Lyrthindor
  - Carried by Lyrthindor
- Notes:
  - This reaction triggers the class action Shield Blow against the attacker.
- Bugs:
  - The description of this passive incorreclty states it requires a Dexterity saving throw; it instead requires a Strength saving throw.

### Justiciar's Scimitar
- Rarity: Very Rare | Slot: Weapon (Scimitars) | Act: Act Two
- Description: Justiciar's Scimitar is a very rare +2 Scimitar weapon that can blind an opponent if the wielder strikes with Advantage. It also grants the Shadowsoaked Blow weapon action.
- Effect: Damage: 1d6 + 2 (3~8) + Strength or Dexterity modifier Slashing | Shadow-Blinding: If you attack with Advantage, you have a chance to Blind your target. | Shadow Blade: You have Advantage on Attack Rolls against Lightly or Heavily Obscured targets when using this blade. | Backbreaker: Put extra force behind your strike to possibly knock your enemy Prone. (Recharge: Short rest.) | Flourish: Feint an attack to possibly throw your opponent Off Balance. (Recharge: Short rest.) | Shadowsoaked Blow: Strike an enemy, adding your proficiency bonus to the damage. Moreover, if the attack hits, it deals an additional 1d6 PsychicDRS damage. This attack doesn't break concealment. (Recharge: Short rest.)
- How to get:
  - Gauntlet of Shar X: -713 Y: -732: Carried by Lyrthindor
  - Carried by Lyrthindor
- Notes:
  - This weapon does not have a proficiency classification, and does not require proficiency in Scimitars to use.
  - Despite the tooltip not stating so, Shadow-Blinding applies only to attacks made with the weapon that has this feature.
  - While active, Shadow Blade provides Advantage to both mainhand and off-hand equipped melee weapons.
  - Prior to Patch 8 Hotfix 1, Shadow Blade granted advantage to all attack rolls when active. This was changed to only melee weapon attacks.
  - "Not breaking concealment" means that the attacker can remain Hidden after performing the attack, though it still ends Invisibility. A solo character can use this attack while hidden without entering combat. This lets them get two attacks off before their opponent is aware of them, making it an excellent candidate for use in assassinating isolated NPCs.
  - The psychic damage of Shadowsoaked blow works as DRS even in honor mode.
- Bugs:
  - Due to the missing proficiency classification, this weapon cannot be used to activate Bladesong when equipped in the mainhand weapon slot, although equipping it does not apply Bladesong Impeded (Condition). This issue does not occur when equipped in the offhand weapon slot.
  - This weapon has a hidden version of the Shadow Blade applied to it, which grants advantage on all melee weapon attack rolls while active, including weapon attack rolls for another equipped melee weapon while dual-wielding.
  - In Honour mode, this feature is non-functional.

### Killer's Sweetheart
- Rarity: Very Rare | Slot: Ring | Act: Act Two
- Description: Killer's Sweetheart is a very rare Ring that makes the wearer's next Attack Roll a critical hit after killing a creature, once per Long Rest.
- Effect: Executioner: When you kill a creature, your next Attack Roll will be a Critical Hit. Once spent, this effect refreshes after a Long Rest.
- How to get:
  - Gauntlet of Shar X: -833 Y: -729: On the ground where the shadow copy appearing next to the Brazier is defeated in the Self-Same Trial
  - On the ground where the shadow copy appearing next to the Brazier is defeated in the Self-Same Trial
- Notes:
  - After a creature is killed, the Executioner critical hit can be set to 'Ask' or disabled entirely in the Reactions tab, allowing it to be saved for later. Using it does not consume a Reaction resource.
  - The automatic critical hit from Executioner can be applied to every target hit by a single AOE attack, such as Whirlwind Attack or Razor Gale.
- Bugs:
  - Despite the tooltip suggesting otherwise, Executioner only applies to weapon attack rolls.
  - When using weapon specific abilities that impose a saving throw such as Pushing Attack (Melee) and Lacerate, Executioner attempts to apply its 'Natural 20' effect to the enemy's saving throw as well as the character's attack. This creates a risk of wasting the Executioner condition to help the enemy.
  - If the Executioner reaction is set to 'Automatic': the game forces the character's attack roll to a 20 (a Critical Hit) but also forces the target’s Saving Throw to a 20. This grants the enemy a high probability of resisting the secondary effect (e.g., they take the damage but are not pushed). If the Executioner reaction is set to 'Ask': The game triggers two separate prompts: First Prompt: asks to turn the character's attack roll into a 20. (Recommend: Yes)
  - Second Prompt: asks to turn the enemy's Saving Throw into a 20. (Recommend: No) If the character accepts the second prompt, the Executioner condition is consumed, and the enemy receives a large bonus to their save.
  - Note: While Saving Throws do not technically 'critically succeed' on a 20, the high roll often results in the enemy resisting the effect.
  - Wasted Charges: due to a scripting error, Executioner fails to check if the attacking character has already rolled a Natural 20 normally. If the character lands a critical hit on their own, the reaction can still trigger (and be consumed) if they either accept the reaction prompt or have it set to 'Automatic'.

### Least Expected
- Rarity: Rare | Slot: Weapon (Shortbows) | Act: Act Two
- Description: Least Expected is a rare + 2 Shortbow which grants the Blinding Shot weapon action, and increases Attack Rolls while Obscured.
- Effect: Damage: 1d6 + 2 (3~8) + Dexterity modifier Piercing | Darkveil Precision: While obscured in shadow, the wielder has a +1d4 bonus to their ranged weapon attacks. | Hamstring Shot: Shoot an enemy in the thigh and possibly reduce their movement speed by 50%. (Recharge: Short rest.) | Blinding Shot: Weave the lost magic of the children of Deep Duerra into your shot and possibly Blind your target. (Recharge: Short rest.)
- How to get:
  - Gauntlet of Shar X: -730 Y: -800: In a gilded chest beyond the locked puzzle door
  - In a gilded chest beyond the locked puzzle door
- Notes:
  - Darkveil Precision, when active, places a condition upon the wielder by the same name which has the following description: "As long as it remains obscured, the affected entity has a +1d4 bonus to ranged Attack Rolls." This may be confusing as it does not specify "ranged weapons" as the passive does, but the 1d4 bonus is indeed limited to ranged weapon attack rolls.
- Bugs:
  - Darkveil Precision is not automatically applied to the wielder when first equipped while already Lightly Obscured or Heavily Obscured. The wielder must first either move to Clear Area and back, or Hide.

### Merregon Halberd
- Rarity: Uncommon | Slot: Weapon (Halberds) | Act: Act Two
- Description: Merregon Halberd is an uncommon, lightly enchanted (+1) Halberd.
- Effect: Damage: 1d10 + 1 (2~11) + Strength modifier Slashing | Rush Attack: Charge forward and attack the first enemy in your way, possibly pushing them Off Balance. (Recharge: Short rest.) | Lacerate: Slash at your target's vital points to make it Bleed. (Recharge: Short rest.) | Cleave: Swing your weapon in a large arc to attack up to 3 enemies at once. They each take half the damage your weapon usually deals. (Recharge: Short rest.)
- How to get:
  - Grymforge X: -574 Y: 377: Carried by a Merregon Legionnaire in the hallway with the Hellsboars
  - Grymforge X: -643 Y: 215: Laying around the Crumbling Island
  - Grymforge X: -601 Y: 199: Laying around the Crumbling Island
  - Gauntlet of Shar X: -658 Y: 753: Carried by the Merregons accompanying Yurgir
  - Carried by the Merregons accompanying Yurgir

### Spear of Night
- Rarity: Rare | Slot: Weapon (Spears) | Act: Act Two
- Description: Spear of Night is a rare, lightly enchanted (+1) variant of the Spears family of weapons. It is a simple melee weapon that can be wielded in one hand, or with both hands for extra damage. Its design lends itself well to be thrown at enemies as a projectile.
- Effect: One-handed damage: 1d6 + 1 (2~7) + Strength modifier Piercing | Two-handed damage: 1d8 + 1 (2~9) + Strength modifier Piercing | Shar's Blessing: If Shar allows it, use this spear to kill Nightsong. | Rush Attack: Charge forward and attack the first enemy in your way, possibly pushing them Off Balance. (Recharge: Short rest.)
- How to get:
  - Gauntlet of Shar X: -820 Y: -756: On a shrine in the Silent Library, beyond the riddle door
  - On a shrine in the Silent Library, beyond the riddle door
- Notes:
  - Acquiring the weapon grants the inspiration Made of Shadows to party members with the Guild Artisan background.
  - This item is critical to the quest The Chosen of Shar and Shadowheart turns hostile if the party attempt to enter the Shadowfell without it. Depending on the choices made in the quest, this item is replaced by one of the following: Selûne's Spear of Night
  - Shar's Spear of Evening
  - This item is not tagged as a story item in the game files.
  - This item has no description flavour text.
  - If Shadowheart has lost the spear while already in the Shadowfell, Aylin mocks her for losing the only weapon that could kill her. The story then progresses as if Shadowheart chose to spare the Nightsong.


## Grand Mausoleum

### Vivacious Cloak
- Rarity: Uncommon | Slot: Cloak | Act: Act Two
- Description: Vivacious Cloak is an uncommon Cloak that grants the wearer 8 temporary Hit Points when casting a spell in melee.
- Effect: Arcane Vivaciousness: You gain 8 temporary hit points after casting a spell while in melee.
- How to get:
  - Grand Mausoleum X: -257 Y: -886: In a locked traveller's chest in the south-east corner
  - In a locked traveller's chest in the south-east corner
- Notes:
  - Spells with attack rolls or saving throws will trigger Arcane Vivaciousness if they miss/fail.
  - In melee means that the wearer must be in range of a melee enemy and under the Threatened condition. Enemies wielding ranged weapons do not impose this condition and thus do not trigger Arcane Vivaciousness.


## House in Deep Shadows

### Ring of Mental Inhibition
- Rarity: Uncommon | Slot: Ring | Act: Act Two
- Description: Ring of Mental Inhibition is an uncommon Ring that places a mentally weakening condition on enemies who fail to Save against the wearer's spells and abilities.
- Effect: Mental Inhibition: When a foe fails a Saving Throw against one of your spells or actions, they gain Mental Fatigue for 2 turns.
- How to get:
  - House in Deep Shadows X: 76 Y: 40: in a locked chest, just east of the Waypoint of the Shadowed Battlefield
  - in a locked chest, just east of the Waypoint of the Shadowed Battlefield
- Notes:
  - Mental Fatigue is not applied on saving throws made to shake off an effect. For example, if a creature is under the effect of Hold Person, it makes a Wisdom saving throw at the end of each turn to end the effect. Failing that saving throw does not apply Mental Fatigue.
  - As of Patch 2 Hotfix 5, the condition is not applied to failed saves from weapon passive effects, coatings, clouds, or wall spells, such as Cloudkill, Stinking Cloud, or Wall of Fire. In these cases, the saving throw appears to be against the area of effect instead of the caster.[verify]
- Bugs:
  - Despite the description, Mental Inhibition also applies to allies.

### Ring of Shadows
- Rarity: Uncommon | Slot: Ring | Act: Act Two
- Description: The Ring of Shadows is an uncommon Ring that grants its wearer the ability to cast Pass Without Trace once per Long Rest.
- Effect: Pass Without Trace: Call forth a veil of shadow and silence that gives you and nearby allies a +10 bonus to Stealth Checks. (Recharge: Long rest.)
- How to get:
  - House in Deep Shadows X: 76 Y: 37: Rewarded by Oliver, for playing both rounds of hide and seek with him (regardless of winning or losing)
  - Rewarded by Oliver, for playing both rounds of hide and seek with him (regardless of winning or losing)
- Notes:
  - This ring can also be obtained by knocking out Oliver out or through pick-pocketing him at the exact moment the encounter becomes a tactical turn based encounter and before he vanishes, or if invisible creatures such as he can be seen. Pick-pocketing Oliver does not change how he interacts with the party.
- Bugs:
  - This item can be unequipped after casting Pass Without Trace from it; the caster will still receive the use of Pass Without Trace until long rest or concentration is broken.


## House of Healing

### Artificial Leech (+1)
- Rarity: Uncommon | Slot: Weapon (Daggers) | Act: Act Two
- Description: Artificial Leech is an uncommon +1 Dagger which grants non player characters the Bloodletting weapon action.
- Effect: Damage: 1d4 + 1 (2~5) + Strength or Dexterity modifier Piercing | Piercing Strike: Stab an enemy and possibly inflict Gaping Wounds. (Recharge: Short rest.) | Bloodletting: Pierce an enemy's flesh and possible make them Bleed. Some undead and constructs can't suffer bleeding. (Recharge: Short rest.)
- How to get:
  - House of Healing X: -201 Y: 50: Carried by Sister Geanne
  - Carried by Sister Geanne
- Notes:
  - Collecting one of each of the nurses' tools grants the inspiration Right Tool for the Job to party members with the Criminal background.
  - When wielded by any nurse, this weapon deals an additional 1d6 Necrotic damage.

### Bonesaw (+1)
- Rarity: Uncommon | Slot: Weapon (Longswords) | Act: Act Two
- Description: Bonesaw is an uncommon +1 Longsword which grants non player characters the weapon action Incise Ligaments.
- Effect: One-handed damage: 1d8 + 1 (2~9) + Strength modifier Slashing | Two-handed damage: 1d10 + 1 (2~11) + Strength modifier Slashing | Flourish: Feint an attack to possibly throw your opponent Off Balance. (Recharge: Short rest.) | Lacerate: Slash at your target's vital points to make it Bleed. (Recharge: Short rest.) | Incise Ligaments: Grind your saw's blackest teeth into an enemy's calves and possibly Slow them. (Recharge: Short rest.)
- How to get:
  - House of Healing X: -201 Y: 50: Carried by Sister Hunna
  - Carried by Sister Hunna
- Notes:
  - Collecting one of each of the nurses' tools grants the inspiration Right Tool for the Job to party members with the Criminal background.
  - When wielded by any nurse, this weapon deals an additional 1d6 Necrotic damage.

### Poisoner's Gloves
- Rarity: Rare | Slot: Gloves | Act: Act Two
- Description: Poisoner's Gloves are a rare set of Gloves. They afford their wearer a chance to poison a target (DC 13) every time it receives Poison damage.
- Effect: Envenom: Whenever you deal Poison damage, the target needs to succeed a Constitution Saving Throw or become Poisoned.
- How to get:
  - House of Healing X: -199 Y: 78: in a chest at the back of the building
  - in a chest at the back of the building
- Notes:
  - Envenom is triggered by Trickery Domain Divine Strike: Poison.
  - Poisoned successfully applied by Envenom triggers Deadly Derivation on the Derivation Cloak. Because of this, this passive has combat synergy with Broodmother's Revenge, especially when used in conjunction with Bestow Curse: Constitution Disadvantage and by those with high attack ratings and / or multiple attacks per round.

### Shar's Temptation
- Rarity: Uncommon | Slot: Amulet | Act: Act Two
- Description: Shar's Temptation is an Amulet that allows its wearer to cast Charm Person once per Short Rest.
- Effect: Charm Person: Cast as a level 1 spell (Recharge: Short rest.)
- How to get:
  - House of Healing X: -193 Y: 9: In a crate with a note on top, next to the wooden ladder on the ground floor
  - In a crate with a note on top, next to the wooden ladder on the ground floor

### Surgeon's Subjugation Amulet
- Rarity: Rare | Slot: Amulet | Act: Act Two
- Description: The Surgeon's Subjugation Amulet is a rare Amulet that, once per Long Rest, paralyses a humanoid on a Critical Hit.
- Effect: Paralysing Critical: Once per Long Rest, when scoring a Critical Hit on a humanoid, the wearer can Paralyse the target for 2 turns.
- How to get:
  - House of Healing X: -201 Y: 49: Worn by Malus Thorm
  - Worn by Malus Thorm

### Syringe (+1)
- Rarity: Uncommon | Slot: Weapon (Daggers) | Act: Act Two
- Description: Syringe is an uncommon +1 Dagger which grants the Inject Nostrum weapon action to non player characters only.
- Effect: Damage: 1d4 + 1 (2~5) + Strength or Dexterity modifier Piercing | Piercing Strike: Stab an enemy and possibly inflict Gaping Wounds. (Recharge: Short rest.) | Inject Nostrum: Inject an enemy with the mysterious liquid in your syringe and possibly Poison them. (Recharge: Short rest.)
- How to get:
  - House of Healing X: -201 Y: 50: Carried by Sister Anya
  - Carried by Sister Anya
- Notes:
  - Collecting one of each of the nurses' tools grants the inspiration Right Tool for the Job to party members with the Criminal background.
  - When wielded by any nurse, this weapon deals an additional 1d6 Necrotic damage.

### Trepan (+1)
- Rarity: Uncommon | Slot: Weapon (Shortswords) | Act: Act Two
- Description: Trepan is an uncommon +1 Shortsword which grants the weapon action Trephination to non player characters only.
- Effect: Damage: 1d6 + 1 (2~7) + Strength or Dexterity modifier Piercing | Flourish: Feint an attack to possibly throw your opponent Off Balance. (Recharge: Short rest.) | Piercing Strike: Stab an enemy and possibly inflict Gaping Wounds. (Recharge: Short rest.) | Trephination: Make a burr hole into an enemy's skull and possibly knock them Prone. (Recharge: Short rest.)
- How to get:
  - House of Healing X: -201 Y: 50: Carried by Sister Vanessa
  - Carried by Sister Vanessa
- Notes:
  - Collecting one of each of the nurses' tools grants the inspiration Right Tool for the Job to party members with the Criminal background.
  - When wielded by any nurse, this weapon deals an additional 1d6 Necrotic damage.

### True Love's Embrace
- Rarity: Rare | Slot: Ring | Act: Act Two
- Description: True Love's Embrace is one of a matching pair of Rings that lets the wearer cast Warding Bond.
- Effect: Intimate Embrace: One of a magical pair of rings, this allows the wearer to cast Warding Bond once per Long Rest on a creature wearing the matching ring.
- How to get:
  - House of Healing X: -212 Y: 0: On a skeleton laying on a mattress on the ground
  - On a skeleton laying on a mattress on the ground
- Notes:
  - The matching ring is True Love's Caress, found on a skeleton leaning up against a large tree in the Shadow-Cursed Lands X: -147 Y: 43.
  - This ring is found on the same corpse as Bonded By Love - Husband's Diary, which describes a newlywed man who is taken to the House of Healing after suffering from a myriad of mysterious injuries. The husband describes how, prior to receiving these injuries, his wife went to battle against an entire troop of Harpers and defeated them without getting a single scratch.
  - See also: Bonded By Love - Husband's Diary
  - Bonded By Love - Wife's Diary
  - After casting Warding Bond, the condition persists even if both party members unequip the rings. It lasts until death or a Long Rest.


## Last Light Inn

### Acrobat Shoes
- Rarity: Rare | Slot: Boots | Act: Act Two
- Description: Acrobat Shoes is a pair of rare Boots that grants a bonus to Acrobatics and Advantage on Dexterity Saving Throws.
- Effect: Acrobatics +1 | Advantage on Dexterity Saving Throws.
- How to get:
  - Last Light Inn X: -56 Y: 133: Sold by Barcus Wroot at his workshop
  - Sold by Barcus Wroot at his workshop
- Bugs:
  - In what is likely a typo, the in-game description states these shoes grant "Advantage on Dexterity Saving Throws Checks".

### Amulet of the Harpers
- Rarity: Rare | Slot: Amulet | Act: Act Two
- Description: Amulet of the Harpers is a rare Amulet that allows the wearer to cast Shield once per Long Rest and grants Advantage with Wisdom Saving Throws.
- Effect: Shield: Cast as a level 1 spell (Recharge: Long rest.) | Advantage with Wisdom Saving Throws.
- How to get:
  - Last Light Inn X: -31 Y: 130: Sold by Quartermaster Talli near the Last Light Inn waypoint
  - Sold by Quartermaster Talli near the Last Light Inn waypoint
- Bugs:
  - The in-game description for this item ("advantage on wisdom saving throws checks") is likely a typo; it provides advantage on saving throws, not checks.

### Barkskin Armour
- Rarity: Rare | Slot: Medium Armour (Medium) | Act: Act Two
- Description: Barkskin Armour is a rare Medium Armour that sets the user's Armour Class to 16 and grants Advantage on Constitution Saving Throws.
- Effect: AC 12 | Forest Aegis: You are invested with the power of the meadows and woods of the land, and have the effect of Barkskin, increasing your Armour Class to 16. | File ARM_Hide_A_1_Body | Advantage on Constitution Saving Throws.
- How to get:
  - Last Light Inn X: -31 Y: 130: Sold by Quartermaster Talli near the Last Light Inn waypoint
  - Sold by Quartermaster Talli near the Last Light Inn waypoint
- Notes:
  - Barkskin from Forest Aegis does not remain active while in Wild Shape.

### Charge-Bound Warhammer
- Rarity: Rare | Slot: Weapon (Warhammers) | Act: Act Two
- Description: Charge-Bound Warhammer is a rare +1 Warhammer with +1 bonus to damage and Attack Rolls, and deals additional 1d6 Lightning damage. This hammer's magical powers only function if it's Bound to an Eldritch Knight or is a Warlock's Pact Weapon.
- Effect: One-handed damage: 1d8 + 1 (2~9) + Strength modifier Bludgeoning | Two-handed damage: 1d10 + 1 (2~11) + Strength modifier Bludgeoning | Favoured Weapon: This weapon has a +1 bonus to damage and Attack Rolls. | Galvanic Currents: This weapon deals an additional 1d6 Lightning damage. | Backbreaker: Put extra force behind your strike to possibly knock your enemy Prone. (Recharge: Short rest.) | Concussive Smash: Hit an enemy with all your might to deal damage and possibly Daze them. (Recharge: Short rest.) | Weakening Strike: Target an enemy's hands with a non-lethal attack and possibly inflict Weak Grip. (Recharge: Short rest.) | This hammer's magical powers only function if it's bound to an Eldritch Knight or is a Warlock's Pact or Hexed weapon. These effects are in addition to the weapon's +1 enchantment. Due to both the enchantment and the favoured weapon bonus stacking, this weapon is effectively a +2 weapon when bound.
- How to get:
  - Last Light Inn X: -33 Y: 164: Sold by Dammon
  - Sold by Dammon
- Notes:
  - These effects are in addition to the weapon's +1 enchantment. Due to both the enchantment and the favoured weapon bonus stacking, this weapon is effectively a +2 weapon when bound.
- Bugs:
  - If this weapon is bound by an Eldritch Knight or Pact of the Blade Warlock, this weapon will permanently retain the lightning damage bonus from Galvanic Currents even if the character binds another weapon. The weapon will even retain this passive if the weapon is used by another character, different from the one who bound it.

### Cindersnap Gloves
- Rarity: Rare | Slot: Gloves | Act: Act Two
- Description: Cindersnap Gloves are a rare pair of Gloves that grant the spell Protection from Missiles.
- Effect: Protection from Missiles: Amplify your reflexes to better contend with incoming missiles. Ranged weapon attacks against you have Disadvantage, and their damage is halved. (Recharge: Short rest.)
- How to get:
  - Last Light Inn X: -31 Y: 130: Sold by Quartermaster Talli near the Last Light Inn waypoint
  - Sold by Quartermaster Talli near the Last Light Inn waypoint

### Cloak of Cunning Brume
- Rarity: Uncommon | Slot: Cloak | Act: Act Two
- Description: Cloak of Cunning Brume is an uncommon Cloak which grants the user a smokescreen cloud effect when trying to Disengage.
- Effect: Cunning Brume: When the wearer Disengages, they also create a foggy cloud with 2 m (7 ft) radius that lasts for 1 turn.
- How to get:
  - Last Light Inn X: -56 Y: 141: Sold by Mattis
  - Sold by Mattis
- Notes:
  - The effect produces a miniature fog cloud, obscuring and blinding all creatures within. This makes it very useful for thievery and getting Advantage on enemies threatening the user.
  - This effect triggers when using one of the disengage actions: Cunning Action: Disengage
  - Disengage
  - Disengage: Bonus Action
  - Step of the Wind: Disengage
  - It does not trigger when disengaging through Cautious Healer

### Cloak of Protection
- Rarity: Uncommon | Slot: Cloak | Act: Act Two
- Description: Cloak of Protection is an uncommon Cloak which grants the wearer +1 Armour Class and +1 to Saving Throws
- Effect: Armour Class +1 | Saving Throw +1
- How to get:
  - Last Light Inn X: -31 Y: 130: Sold by Quartermaster Talli near the Last Light Inn waypoint
  - Sold by Quartermaster Talli near the Last Light Inn waypoint

### Darkfire Shortbow
- Rarity: Rare | Slot: Weapon (Shortbows) | Act: Act Two
- Description: Darkfire Shortbow is a rare +2 Shortbow that grants Resistance to Fire and Cold and grants the ability to cast Haste.
- Effect: Damage: 1d6 + 2 (3~8) + Dexterity modifier Piercing | Haste: Cast as a level 3 spell (Recharge: Long rest.) | Hamstring Shot: Shoot an enemy in the thigh and possibly reduce their movement speed by 50%. (Recharge: Short rest.) | Resistance to Fire damage. | Resistance to Cold damage.
- How to get:
  - Last Light Inn X: -33 Y: 164: Sold by Dammon in Act Two
  - Sold by Dammon in Act Two

### Defender Greataxe
- Rarity: Rare | Slot: Weapon (Greataxes) | Act: Act Two
- Description: Defender Greataxe is a rare +2 Greataxe that can be reduced in its enchantment on the first attack of the round to increase wielder's Armour Class and saving throw bonus.
- Effect: Damage: 1d12 + 2 (3~14) + Strength modifier Slashing | Defensive Attack: When making your first attack of the round, you can reduce this weapon's enchantment by 1 to increase your Armour Class and Saving Throw bonus by 1. | Cleave: Swing your weapon in a large arc to attack up to 3 enemies at once. They each take half the damage your weapon usually deals. (Recharge: Short rest.) | Lacerate: Slash at your target's vital points to make it Bleed. (Recharge: Short rest.) | Prepare: Spend 6 m (20 ft) of your movement to deal an additional Strength modifier PhysicalDRS damage (minimum 1) on each successful melee weapon attack for the rest of the turn. (Recharge: Short rest.)
- How to get:
  - Last Light Inn X: -31 Y: 130: Sold by Quartermaster Talli near the Last Light Inn waypoint
  - Sold by Quartermaster Talli near the Last Light Inn waypoint
- Notes:
  - This provided reaction is only triggered when making the first attack with Defender Greataxe in a round. Subsequent attacks do not give an opportunity to activate this action.
  - The -1 penalty to attack rolls from Defensive Attack is applied to the attack that triggers the reaction. The confirmation prompt for the reaction shows the attack roll as well as AC of the target, so the weilder can decline the reaction if it would turn a hit into a miss.

### Evasive Shoes
- Rarity: Rare | Slot: Boots | Act: Act Two
- Description: The Evasive Shoes are a rare pair of Boots that give a small bonus to Acrobatics and Armour Class.
- Effect: Acrobatics +1 | Armour Class +1
- How to get:
  - Last Light Inn X: -56 Y: 141: Sold by Mattis
  - Sold by Mattis

### Flawed Helldusk Armour
- Rarity: Rare | Slot: Heavy Armour (Heavy) | Act: Act Two
- Description: Flawed Helldusk Armour is a rare Heavy Armour that reduces Piercing damage by 1 and possibly deals 1d4 Fire damage to attackers.
- Effect: AC 18 | Lesser Infernal Retribution: When you are hit by a foe within 2 m (7 ft), it might take 1d4 Fire damage. | Superior Plate: You take 1 less Piercing damage. | Disadvantage on Stealth checks.
- How to get:
  - Last Light Inn X: -33 Y: 164: Crafted by Dammon
  - Crafted by Dammon
- Notes:
  - The party must give Dammon one piece of Infernal Iron. Upon obtaining the first piece, he crafts this item.
  - Asking Dammon to create Flawed Helldusk Armour, the Flawed Helldusk Helmet or Flawed Helldusk Gloves requires a piece of Infernal Iron for each piece of equipment.
  - Lesser Infernal Retribution requires a DC 13 Dexterity Saving Throw in order to deal damage.
  - This does not trigger Heat while wearing Thermoarcanic Gloves or having Gripped by Kereska's Flame.
- Bugs:
  - The required saving throw for Lesser Infernal Retribution is attributed in the combat log to the wearer of the armour, rather than the attacker, but is correctly rolled by the attacker.
  - Though Lesser Infernal Retribution states an attacker must be within 2 m (7 ft), it actually only triggers on a melee attack.

### Flawed Helldusk Gloves
- Rarity: Rare | Slot: Gloves | Act: Act Two
- Description: Flawed Helldusk Gloves are a rare pair of gloves that grant +1d4 Fire damage to weapon attacks. Unarmed attacks deal +1d4 Necrotic damage and have a chance to inflict Bleeding.
- Effect: Lesser Infernal Touch: Your weapon attacks deal an additional 1d4 Fire damage. Your unarmed attacks deal an additional 1d4 Necrotic damage, and can possibly inflict Bleeding. | Strength Saving Throws +1
- How to get:
  - Last Light Inn X: -33 Y: 164: Crafted by Dammon after giving him a third piece of Infernal Iron
  - Crafted by Dammon after giving him a third piece of Infernal Iron
- Notes:
  - Asking Dammon to create Flawed Helldusk Armour, the Flawed Helldusk Helmet or Flawed Helldusk Gloves requires a piece of Infernal Iron for each piece of equipment.
- Bugs:
  - On thrown weapon attacks, Lesser Infernal Touch applies both the extra fire damage meant for weapon attacks and the Bleeding effect meant for unarmed attacks.
  - The target's DC 13 Constitution Saving Throw to resist the Bleeding condition from Lesser Infernal Touch does not appear in the combat log.

### Flawed Helldusk Helmet
- Rarity: Rare | Slot: Helmet | Act: Act Two
- Description: Flawed Helldusk Helmet is a rare Helmet crafted from Infernal Iron that improves the wearer's saving throws against spells by 2.
- Effect: Magical Durability: The wielder has a +2 bonus to Saving Throws against spells. | Constitution Saving Throws +1
- How to get:
  - Last Light Inn X: -33 Y: 164: Crafted by Dammon
  - Crafted by Dammon
- Notes:
  - The party must give Dammon two pieces of Infernal Iron. Upon obtaining the second piece, he crafts this item.
  - Asking Dammon to create Flawed Helldusk Armour, the Flawed Helldusk Helmet or Flawed Helldusk Gloves requires a piece of Infernal Iron for each piece of equipment.

### Gloves of the Automaton
- Rarity: Rare | Slot: Gloves | Act: Act Two
- Description: The Gloves of the Automaton are a rare pair of Gloves which, when activated, cause the wearer to be treated as a Construct and grant Advantage on weapon attacks for 10 turns.
- Effect: Circuitry Interface: You are considered a construct. Your weapon Attack rolls have Advantage, and you have resistance to Lightning damage. (Recharge: Short rest.) | Strength Saving Throws +1.
- How to get:
  - Last Light Inn X: -56 Y: 133: Sold by Barcus Wroot at his workshop
  - Sold by Barcus Wroot at his workshop
- Notes:
  - Being treated as a construct via Circuitry Interface prevents the wearer from being targeted by healing spells. However, they can still be healed by drinking healing potions or having allies Throw these potions at them.
  - While active, Circuitry Interface prevents Light of Creation from Stunning its wielder.
  - If unequipped after activation, the remaining duration of Circuitry Interface still applies to the wearer.

### Gloves of the Balanced Hands
- Rarity: Rare | Slot: Gloves | Act: Act Two
- Description: Gloves of the Balanced Hands are a rare pair of Gloves that add the wearer's Ability Modifier to damage when they make an attack with their off-hand weapon.
- Effect: Two-Weapon Fighting: When you make an offhand attack, you can add your Ability Score Modifier to the damage of the attack.
- How to get:
  - Last Light Inn X: -31 Y: 130: Sold by Quartermaster Talli near the Last Light Inn waypoint
  - Sold by Quartermaster Talli near the Last Light Inn waypoint
- Notes:
  - The gloves work with both melee and ranged weapons.
  - These gloves do not stack with other sources of Two-Weapon Fighting.
  - Despite the name, these are actually bracers which cover the wearer's forearms and leave their hands bare.
  - Multiple sources of Two-Weapon Fighting do not provide additional damage to off-hand attacks.
  - Not to be confused with the Dual Wielder feat.
  - During level up, the character will always have only one weapon visible at their back, even if two are equipped.
  - Unlike tabletop 5e, the Two-Weapon Fighting Style provides no benefit to Thrown weapons in Baldur's Gate 3. While dual-wielding still allows for an off-hand throw attack via Bonus Action, BG3's game engine automatically adds the user's Ability Modifier to throw damage by default. Therefore, this Fighting Style '"`UNIQ--nowiki-00000148-QINU`"' which grants the same modifier to off-hand strikes '"`UNIQ--nowiki-00000148-QINU`"' is redundant for throwing. In tabletop D&D, this style is required to add Ability Modifier damage to an off-hand throw (PHB, p. 195).

### Harmonium Halberd
- Rarity: Rare | Slot: Weapon (Halberds) | Act: Act Two
- Description: Harmonium Halberd is a rare +1 Halberd that grants its wielder additional Strength at the cost of some Intelligence and Wisdom.
- Effect: Damage: 1d10 + 1 (2~11) + Strength modifier Slashing | Rush Attack: Charge forward and attack the first enemy in your way, possibly pushing them Off Balance. (Recharge: Short rest.) | Lacerate: Slash at your target's vital points to make it Bleed. (Recharge: Short rest.) | Cleave: Swing your weapon in a large arc to attack up to 3 enemies at once. They each take half the damage your weapon usually deals. (Recharge: Short rest.) | Strength +2 (up to 23) | Intelligence -1 | Wisdom -1
- How to get:
  - Last Light Inn X: -33 Y: 164: Sold by Dammon in Act Two
  - Sold by Dammon in Act Two
- Notes:
  - Harmonium Halberds are enchanted polearms wielded by the members of the Harmonium faction in the planar city of Sigil. It also previously appeared in Baldur's Gate II: Shadows of Amn.

### Hat of Fire Acuity
- Rarity: Uncommon | Slot: Helmet | Act: Act Two
- Description: Hat of Fire Acuity is an uncommon hat that grants the wearer Arcane Acuity whenever they deal Fire damage.
- Effect: Fire Acuity: Whenever you deal Fire damage, you gain Arcane Acuity for 2 turns.
- How to get:
  - Last Light Inn X: -28 Y: 170: Carried by the Strange Ox in Dammon's blacksmith in Act Two
  - Rivington X: 38 Y: -149: Carried by the Strange Ox on a hill west of the requisitioned barn at the beginning of Act Three
  - Carried by the Strange Ox in Dammon's blacksmith in Act Two
- Notes:
  - Slaying the Strange Ox at the Druid Grove will only reward the Shapeshifter's Boon Ring, because it does not have the Hat of Fire Acuity until reaching the Last Light Inn at the beginning of Act Two.
  - Killing the Strange Ox will prevent summoning them during the Gather Your Allies quest in Act 3. However, there is no other way to acquire this hat.
- Bugs:
  - Fire Acuity only functions once per attack, despite the in-game tooltip stating "whenever" you deal fire damage. It does however work for every ray of Scorching Ray, since each ray makes a separate attack roll.

### Hat of Uninhibited Kushigo
- Rarity: Rare | Slot: Helmet | Act: Act Two
- Description: The Hat of Uninhibited Kushigo is a rare hat that grants +1 bonus to their Spell Save DC after dealing damage with an unarmed attack.
- Effect: Lay Bare Their Weakness: After dealing damage with an unarmed attack, the wearer gains a +1 bonus to their spell save DC until the end of their turn.
- How to get:
  - Last Light Inn X: -31 Y: 130: Sold by Quartermaster Talli near the Last Light Inn waypoint
  - Sold by Quartermaster Talli near the Last Light Inn waypoint
- Notes:
  - This only triggers on melee unarmed attacks, not on Throws.
  - Though seemingly a great choice for Way of the Four Elements Elemental Disciplines, the effect only lasts until the beginning of the wearer's next turn and as a result requires Flurry of Blows to trigger each turn before the use of an action with a saving throw.

### Incandescent Staff
- Rarity: Very Rare | Slot: Weapon (Quarterstaves) | Act: Act Two
- Description: Incandescent Staff is a very rare Quarterstaff which grants the wielder a bonus to ranged spell Attack Rolls and resistance to Fire damage. It also grants the ability to cast the Fire Bolt and Fireball spells.
- Effect: One-handed damage: 1d6 (1~6) + Strength modifier Bludgeoning | Two-handed damage: 1d8 (1~8) + Strength modifier Bludgeoning | Fire Bolt: Cast as a cantrip at will. | Fireball: Cast as a level 3 spell (Recharge: Long rest.) | Topple: Swipe at a creature to knock it Prone. (Recharge: Short rest.) | Ranged Spell Attack +1 | Resistance to Fire damage
- How to get:
  - Last Light Inn X: -31 Y: 130: Sold by Quartermaster Talli near the Last Light Inn waypoint
  - Sold by Quartermaster Talli near the Last Light Inn waypoint

### Jhannyl's Gloves
- Rarity: Rare | Slot: Gloves | Act: Act Two
- Description: Jhannyl's Gloves are a rare pair of Gloves that let the wearer automatically cast Lesser Restoration on themselves when they become Blinded, Paralysed or Poisoned.
- Effect: Defy Villainy: When the wearer becomes Blinded, Paralysed or Poisoned, they automatically cast Lesser Restoration on themselves. | Saving Throws +1
- How to get:
  - Last Light Inn X: -60 Y: 158: Worn by Isobel if she is killed after dealing with the Nightsong but before completing the assault on Moonrise
  - Mind Flayer Colony X: 861 Y: -23: Worn by Isobel if she is kidnapped by Marcus or killed at Last Light Inn before dealing with the Nightsong
  - Ramazith's Tower: Worn by Isobel if the Nightsong is killed or imprisoned by Lorroakan
  - Campsite (Act Two): Worn by Isobel if she joins the camp
  - Worn by Isobel if she is killed after dealing with the Nightsong but before completing the assault on Moonrise
- Notes:
  - Likely related to Jhannyl's wristlet, a magic item also used by the Harpers.
  - Despite the description, this passive protects from every condition in Diseased, Poisoned, Paralyzed, and Blinded condition groups, plus Bloodless.
  - Prior to Patch 8, this passive had a once-per-long-rest limit, but it was removed and can now trigger an unlimited number of times.
  - Although Jhannyl's Gloves are associated with Isobel (and equipped by her in certain Act Two encounters) the passive from these gloves is hardcoded to function only for player characters, recruited companions, and hirelings. Therefore Isobel cannot make use of this passive's benefits.
- Bugs:
  - This passive emulates Lesser Restoration spell effects without actually casting it, which would trigger effects like Tempestuous Magic: Flight or restore Arcane Ward charges.

### Moon Devotion Robe
- Rarity: Very Rare | Slot: Clothing | Act: Act Two
- Description: Moon Devotion Robe is a very rare piece of Clothing. It grants Advantage on Constitution Saving Throws as well as the ability to cast Produce Flame and Lunar Bulwark.
- Effect: AC 10 | Lunar Bulwark: Bathe yourself in the shielding magic of Selûne's watchful gaze. (Recharge: Long rest.) | Produce Flame: A flame in your hand sheds a light in a 9 m (30 ft) radius and deals 1d8 Fire damage when thrown. | Selûne's Protection: While the wearer has Mage Armour, each successful Saving Throw causes the source of the Saving Throw to take 1d4 Radiant damage. | File ARM_Isobel_A_Pants | File ARM_Isobel_A_Robe_Skirt_B | Advantage on Constitution Saving Throws. | Saving Throws +1
- How to get:
  - Last Light Inn X: -60 Y: 158: Worn by Isobel after dealing with the Nightsong but before completing the assault on Moonrise Towers
  - Mind Flayer Colony X: 861 Y: -23: Worn by Isobel after being kidnapped by Marcus
  - Ramazith's Tower: Worn by Isobel if the Nightsong is killed or imprisoned by Lorroakan
  - Campsite (Act Two): Worn by Isobel as Camp Follower
  - Worn by Isobel after dealing with the Nightsong but before completing the assault on Moonrise Towers
- Notes:
  - The Produce Flame cantrip granted by the robes always uses Wisdom as the casting ability, regardless of the class' casting ability.
- Bugs:
  - Although Selûne's Protection should be activated by Lunar Bulwark, it is not; the wearer must instead have the regular version of Mage Armour cast on them for its radiant damage to function.
  - Additionally, although the tooltip mentions saving throws without any additional qualifiers, this does not work for saving throws rolled against non-spell effects such as weapon actions. As mentioned in the summary on this page, only successful saves against spells trigger the radiant damage.

### Moonlantern
- Rarity: Story Item | Slot: Weapon (Clubs) | Act: Act Two
- Description: The Moonlantern is a special utility item that sheds a magical Light in a large radius while equipped.
- Effect: One-handed damage: 1d4 (1~4) + Strength modifier Bludgeoning | Two-handed damage: 1d6 (1~6) + Strength modifier Bludgeoning
- How to get:
  - Ruined Battlefield X: 0 Y: -15: Carried by Kar'niss, either after the Harper ambush or at the top of Moonrise Towers
  - Last Light Inn X: -63 Y: 172: Given by Isobel if letting the Harpers take the Moonlantern
  - Moonrise Towers: In Balthazar's room in Moonrise Towers
  - Given by Isobel if letting the Harpers take the Moonlantern
- Notes:
  - The Moonlantern carried by Kar'niss contains a foul-mouthed pixie Dolly Dolly Dolly who wants out. If freed using Inspect Moonlantern, she grants the party a Pixie Blessing.
  - If Dolly is freed, her Moonlantern remains in the inventory of the character who freed her, but its inventory icon changes to a broken version and the lantern cannot be equipped anymore.
  - If Kar'niss arrives at Moonrise Towers with the lantern (whether he escorted the party or not), Dolly dies inside it.
  - If Kar'niss is killed at the ambush and the lantern is taken by the Harpers, the party can follow them back to Last Light Inn. There Isobel gives the party the same Moonlantern with Dolly Dolly Dolly alive inside; she can be freed and the Pixie Blessing may then still be obtained.
  - Switching to ranged weapons while having a Moonlantern equipped retains the Moonshield effect but removes the illumination, allowing darkness-requiring effects such as Covert Critical and Shadow Step to be safely used within the Shadow-Cursed Lands.
  - See also: Broken Moonlantern
  - Dead Pixie
  - Filigreed Feywild Bell
  - Shadow Lantern
- Bugs:
  - The Moonlantern containing Dolly Dolly Dolly still produces a stationary Moonshield Aura when dropped on the ground even after she has been freed from it.

### Obsidian Laced Robe
- Rarity: Rare | Slot: Clothing | Act: Act Two
- Description: Obsidian Laced Robe is rare piece of Clothing that deals Fire damage to enemies on successful Saving Throws against their spells, and grants its wearer resistance to Fire damage.
- Effect: Flaming Revenge: On a successful Saving Throw against a foe's spell, deal 1d4 + proficiency bonus Fire damage to them. | Grants Resistance to Fire damage.
- How to get:
  - Last Light Inn X: -31 Y: 130: Sold by Quartermaster Talli near the Last Light Inn waypoint
  - Sold by Quartermaster Talli near the Last Light Inn waypoint
- Notes:
  - When Flaming Revenge fires, the wearer is not considered the source of damage. This means it does not break Sanctuary, but also does not trigger features from items, like the Braindrain Gloves.

### Potent Robe
- Rarity: Very Rare | Slot: Clothing | Act: Act Two
- Description: The Potent Robe is a very rare piece of Clothing that uses the wearer's Charisma modifier to increase their cantrips' damage as well as give them temporary hit points.
- Effect: AC 10 | Gregarious Caster: Your cantrips deal additional damage equal to your Charisma Modifier. | Well-Liked and Well-Fortified: At the beginning of the wearer's turn, the robe activates, granting them Temporary Hit Points equal to their Charisma Modifier. | Armour Class +1
- How to get:
  - Last Light Inn X: -56 Y: 141: Rewarded by Alfira for successfully completing Rescue the Tieflings
  - Rewarded by Alfira for successfully completing ⁠Rescue the Tieflings
- Notes:
  - Alfira must be alive to receive this item. Although the quest can technically be completed with her dead, there is no one else to provide this specific reward. The only way to obtain this robe as the Dark Urge is to knock Alfira out (in Act One) by using non-lethal attacks prior to actually going to sleep on the night she appears at camp, thereby forcing a substitute, Quil, to appear and be murdered in her place as a victim of the Dark Urge.
  - The Mellow Fruit Dye often matches the colour of Handwear to this item.
  - Gregarious Caster stacks with similar effects such as the Draconic Bloodline Sorcerer's Elemental Affinity feature and the Necklace of Elemental Augmentation, leading to the ability modifier potentially being added to the damage of certain spells several times. It also stacks with Warlock's Agonising Blast.
- Bugs:
  - The temporary hit points from Well-Liked and Well-Fortified only have a Stack Priority of 1, and as such are overridden by any other source of temporary hit points that have a Stack Priority of 1 or higher, even if the new source is of a lesser value.

### Ring of Geniality
- Rarity: Uncommon | Slot: Ring | Act: Act Two
- Description: Ring of Geniality is an uncommon Ring that grants a boost to Persuasion and Deception.
- Effect: Persuasion +1 | Deception +1
- How to get:
  - Last Light Inn X: -56 Y: 133: Sold by Barcus Wroot at his workshop
  - Sold by Barcus Wroot at his workshop

### Rippling Force Mail
- Rarity: Rare | Slot: Heavy Armour (Heavy) | Act: Act Two
- Description: Rippling Force Mail is a rare Heavy Armour that reduces physical damage taken and causes its wearer to deal force damage around them after being struck with physical attacks enough times.
- Effect: AC 17 | Force Absorption: Gain 2 turns of Force Conduit when taking Slashing, Piercing, or Bludgeoning damage. | File ARM_Chain Mail_A_1_Shoulderpads | File ARM_Chain Mail_A_Pants | Disadvantage on Stealth checks.
- How to get:
  - Last Light Inn X: -22 Y: 175: in a locked Rustic Chest on the second floor of Dammon's blacksmith
  - in a locked Rustic Chest on the second floor of Dammon's blacksmith
- Notes:
  - Force Absorption adds 2 turns of Force Conduit when the character takes at least 1 point of Slashing, Piercing, or Bludgeoning damage, including damage from falling, Warding Bond redirected damage, or self-damage effects (such as Blood Sacrifice and The Scourge Mistress' Bane).
  - If the incoming damage is reduced to zero by a damage reduction effect, such as Force Conduit or Heavy Armour Master, no turns are added.
  - When Force Conduit triggers its 1d4 Force area damage, it normally reduces its own stacks to zero. With Force Absorption, however, the character immediately regains 2 stacks, keeping some damage reduction.

### Shadeclinger Armour
- Rarity: Rare | Slot: Light Armour (Light) | Act: Act Two
- Description: Shadeclinger Armour is a rare Light Armour that grants Advantage on Saving Throws while Obscured.
- Effect: AC 12 | Shadeclinger: While obscured, the wearer has Advantage on Saving Throws. | File ARM_Leather_A_1_Kneepad | File ARM_Leather_A_1_Pants | File ARM_Leather_A_1_Shoulderpads | File ARM_Leather_A_Sleeves | Stealth +1
- How to get:
  - Last Light Inn X: -31 Y: 130: Sold by Quartermaster Talli near the Last Light Inn waypoint
  - Sold by Quartermaster Talli near the Last Light Inn waypoint
- Bugs:
  - The Clinging Shadows condition granted by this armour remains even when it is removed. This bug can be exploited to give this condition to the entire active party by having each character equip and then remove this item, one by one.

### Shapeshifter's Boon Ring
- Rarity: Uncommon | Slot: Ring | Act: Act Two
- Description: Shapeshifter's Boon Ring is an uncommon Ring that grants the wearer +1d4 on all checks made while shapeshifted or disguised.
- Effect: Shapeshifter's Boon: While shapeshifting or disguising yourself, gain a +1d4 bonus to all Ability Checks.
- How to get:
  - Emerald Grove X: 217 Y: 540: Carried by the Strange Ox in the Druid Grove
  - Last Light Inn X: -28 Y: 170: Carried by the Strange Ox at Dammon's blacksmith
  - Rivington X: 39 Y: -149: Reward for completing Help the Devilish Ox or looted from Strange Ox
  - Carried by the Strange Ox at Dammon's blacksmith
- Notes:
  - This ring is one of few pieces of equipment that works while under the effect of wild shape. Note that it works with a Circle of Stars Druid's Starry Form, but not with a Circle of Spores Druid's Symbiotic Entity.
  - Two ways among many to trade for this item are:
  - Have the player character stand next to the entrance to the Tiefling Hideout and use a ranged attack, then immediately enter the hideout; upon climbing back up the ladder, the attacker will be able to speak with the Ox and trade to "...smooth things over".
  - Have the attacking character flee via stealth and / or invisibility.
  - The Mark of the Shifter condition is only applied during transformation and lasts until Long Rest; it will not be applied if this ring is put on after the wearer has already shapeshifted.
  - Shapeshifter's Boon does not take effect if the party member is shape changed via a Seeming spell cast by a different party member. However, the targeted party member can then gain this effect by casting Adjust Seeming themselves and picking a different appearance.
- Bugs:
  - After application of Mark of the Shifter, the wearer can unequip this ring for others to use without losing the condition.

### Shield of Devotion
- Rarity: Very Rare | Slot: Shield | Act: Act Two
- Description: Shield of Devotion is a very rare Shield that grants a Level 1 Spell Slot, Shield Bash, and allows the wielder to cast Shield of Devotion: Aid at Level 3 Spell once per Long Rest.
- Effect: AC +2 | Shield of Devotion: Aid: Heal yourself and increase your hit point maximum by 10 hit points. (Recharge: Long rest.) | Additional Spell Slot: You gain 1 Level 1 Spell Slot. | Shield Bash: When a foe hits you with a melee attack, you can use your reaction to knock it Prone unless they succeed a Dexterity Saving Throw.
- How to get:
  - Last Light Inn X: -31 Y: 130: Sold by Quartermaster Talli near the Last Light Inn waypoint
  - Sold by Quartermaster Talli near the Last Light Inn waypoint
- Notes:
  - The version of Aid granted by this item only affects the wielder and is always cast at level 3.
  - This reaction triggers the class action Shield Blow against the attacker.
- Bugs:
  - Additional Spell Slot can grant an extra spell slot once per character per long rest, despite the Spell Slot Depleted condition on the item.
  - Additional Spell Slot can grant an extra spell slot multiple times to the same character if that spell slot is used to create a Sorcery Point.
  - The description of this passive incorreclty states it requires a Dexterity saving throw; it instead requires a Strength saving throw.

### Shield of Scorching Reprisal
- Rarity: Rare | Slot: Shield | Act: Act Two
- Description: Shield of Scorching Reprisal is a rare Shield that grants Fire Resistance, allows one to Shield Bash, and also apply Blazing Retaliation.
- Effect: AC +2 | Blazing Retaliation: Huddle behind your shield to increase your Armour Class by 1 and reap scorching retaliation upon attacks who miss you. (Recharge: Short rest.) | Shield Bash: When a foe hits you with a melee attack, you can use your reaction to knock it Prone unless they succeed a Dexterity Saving Throw. | Grants Resistance to Fire damage.
- How to get:
  - Last Light Inn X: -3 Y: 215: on a buried Flaming Fist's corpse directly east of the "Open Graves" beyond the northern bridge
  - on a buried Flaming Fist's corpse directly east of the "Open Graves" beyond the northern bridge
- Notes:
  - A successful DC 18 Perception Check is needed to detect some rubble. It can be then uncovered by a character with at least 15 Strength. The perception check can be bypassed if a party member uses Speak with Dead on Marcus Falgor and asks him if he left any valuable behind:"Did you leave anything valuable behind?"
  - Blazing Retaliation persists when the shield is unequipped.
  - This reaction triggers the class action Shield Blow against the attacker.
- Bugs:
  - The description of this passive incorreclty states it requires a Dexterity saving throw; it instead requires a Strength saving throw.

### Shifting Corpus Ring
- Rarity: Rare | Slot: Ring | Act: Act Two
- Description: The Shifting Corpus Ring is a rare Ring that grants the ability to cast Invisibility and Blur once per Long Rest.
- Effect: Invisibility: Cast as a level 2 spell (Recharge: Long rest.) | Blur: Cast as a level 2 spell (Recharge: Long rest.)
- How to get:
  - Last Light Inn X: -63 Y: 163: Worn by Fist Marcus
  - Worn by Fist Marcus

### Snowburst Ring
- Rarity: Uncommon | Slot: Ring | Act: Act Two
- Description: Snowburst Ring is an uncommon Ring that causes the wearer to create a 4.5m / 15ft circle of ice around their target when dealing Cold damage.
- Effect: Snowburst: When the wearer deals Cold damage, they also create a 4.5 m (15 ft) circle of Ice around the target(s).
- How to get:
  - Last Light Inn X: -80 Y: 158: Inside a loose plank in the bedroom north of the bar
  - Inside a loose plank in the bedroom north of the bar
- Notes:
  - A DC 10 Perception Check is required to spot the plank.
  - Snowburst does not work with some spell effects that deal Cold damage after the initial casting, such as Hunger of Hadar and the retaliation damage from Armour of Agathys and Fire Shield: Chill.
  - Snowburst does not work with thrown weapons.

### Sword of Clutching Umbra
- Rarity: Rare | Slot: Weapon (Shortswords) | Act: Act Two
- Description: Sword of Clutching Umbra is a rare, lightly enchanted (+1) Shortsword that grants the wielder the unique weapon action Shadowsoaked Blow.
- Effect: Damage: 1d6 + 1 (2~7) + Strength or Dexterity modifier Piercing | Flourish: Feint an attack to possibly throw your opponent Off Balance. (Recharge: Short rest.) | Piercing Strike: Stab an enemy and possibly inflict Gaping Wounds. (Recharge: Short rest.) | Shadowsoaked Blow: Strike an enemy, adding your proficiency bonus to the damage. Moreover, if the attack hits, it deals an additional 1d6 PsychicDRS damage. This attack doesn't break concealment. (Recharge: Short rest.)
- How to get:
  - Last Light Inn X: -33 Y: 164: Sold by Dammon
  - Sold by Dammon
- Notes:
  - "Not breaking concealment" means that the attacker can remain Hidden after performing the attack, though it still ends Invisibility. A solo character can use this attack while hidden without entering combat. This lets them get two attacks off before their opponent is aware of them, making it an excellent candidate for use in assassinating isolated NPCs.
  - The psychic damage of Shadowsoaked blow works as DRS even in honor mode.

### Sword of Life Stealing
- Rarity: Very Rare | Slot: Weapon (Shortswords) | Act: Act Two
- Description: The Sword of Life Stealing is a very rare +2 shortsword which deals an extra 10 Necrotic damage on a critical hit, and heals the wielder for the same amount.
- Effect: Damage: 1d6 + 2 (3~8) + Strength or Dexterity modifier Piercing | Life Stealing Critical: On a Critical Hit, the target takes an extra 10 NecroticDRS damage as long as it isn't a construct or an undead. You also gain 10 temporary hit points. | Piercing Strike: Stab an enemy and possibly inflict Gaping Wounds. (Recharge: Short rest.) | Flourish: Feint an attack to possibly throw your opponent Off Balance. (Recharge: Short rest.)
- How to get:
  - Last Light Inn X: -33 Y: 164: Sold by Dammon
  - Sold by Dammon
- Notes:
  - Despite the ambiguity of the description, only a critical hit from the Sword of Life Stealing triggers this effect; it does not trigger from attacks with other equipped weapons.
- Bugs:
  - The temporary hit points only have a Stack Priority of 1, and as such are overridden by any other source of temporary hit points that have a Stack Priority of 1 or higher, even if the new source is of a lesser value.

### Swordmaster Gloves
- Rarity: Rare | Slot: Gloves | Act: Act Two
- Description: The Swordmaster Gloves are a rare pair of Gloves which grant proficiency with three types of swords and provide a bonus to melee Attack Rolls.
- Effect: Sword Mastery: You gain Proficiency with shortswords, longswords, and greatswords. In addition, you gain a +1 bonus to melee Attack Rolls.
- How to get:
  - Last Light Inn X: -33 Y: 164: Sold by Dammon in Act Two
  - Sold by Dammon in Act Two
- Notes:
  - Despite the description, the +1 attack bonus only applies to weapon attacks, not all melee attacks, and so does not apply to unarmed melee attacks.
- Bugs:
  - Sword Mastery does not increase the damage of off-hand melee attacks.

### Sylvan Scimitar
- Rarity: Uncommon | Slot: Weapon (Scimitars) | Act: Act Two
- Description: Sylvan Scimitar is an uncommon +1 Scimitar that allows its wielder to use their Spellcasting Ability modifier instead of their Dexterity modifier to determine their Attack Roll bonus.
- Effect: Damage: 1d6 + 1 (2~7) + Strength or Dexterity modifier Slashing | Melee Caster: Instead of its Dexterity ability score modifier, the affected entity add its spellcasting modifier to attack rolls. | Lacerate: Slash at your target's vital points to make it Bleed. (Recharge: Short rest.) | Flourish: Feint an attack to possibly throw your opponent Off Balance. (Recharge: Short rest.) | Cleave: Swing your weapon in a large arc to attack up to 3 enemies at once. They each take half the damage your weapon usually deals. (Recharge: Short rest.)
- How to get:
  - Last Light Inn X: -28 Y: 129: Carried by Jaheira
  - Carried by Jaheira
- Notes:
  - Despite this weapon's description, the spell-caster's ability modifier applies to Attack Rolls and Damage Rolls made with this weapon.
  - Like Shillelagh and Infernal Rapier, this weapon uses the character's highest available spellcasting ability rather than the most recent, or their default spellcasting ability if no other is available.
  - Melee Caster does not benefit other equipped weapons.

### The Mighty Cloth
- Rarity: Rare | Slot: Clothing | Act: Act Two
- Description: The Mighty Cloth is a rare piece of Clothing that gives its wearer +2 Strength (up to 20) and the Bull's Strength condition. Also grants the wearer the Bull Rush class action.
- Effect: AC 10 | Bull Rush (+): Charge forward and possibly knock your foes back 3 m (10 ft). (Recharge: Per turn.) | Bull's Strength: You gain Bull's Strength and increase your Strength by 2, to a maximum of 20. | Unwavering Bull: You cannot be pushed against your will and you have an Advantage on Saving Throws against being Restrained.
- How to get:
  - Last Light Inn X: -31 Y: 130: Sold by Quartermaster Talli near the Last Light Inn waypoint
  - Sold by Quartermaster Talli near the Last Light Inn waypoint

### Thermodynamo Axe
- Rarity: Rare | Slot: Weapon (Battleaxes) | Act: Act Two
- Description: Thermodynamo Axe is a rare, lightly enchanted (+1) Battleaxe that grants Heat whenever the wielder deals damage with this weapon.
- Effect: One-handed damage: 1d8 + 1 (2~9) + Strength modifier Slashing | Two-handed damage: 1d10 + 1 (2~11) + Strength modifier Slashing | Thermodynamo: Whenever you deal damage with this weapon, you gain 2 turns of Heat. | Cleave: Swing your weapon in a large arc to attack up to 3 enemies at once. They each take half the damage your weapon usually deals. (Recharge: Short rest.) | Lacerate: Slash at your target's vital points to make it Bleed. (Recharge: Short rest.) | Maiming Strike: Possibly Maims your target. They can't move. (Recharge: Short rest.)
- How to get:
  - Last Light Inn X: -33 Y: 164: Sold by Dammon in Act Two
  - High Hall X: 235 Y: 44: On a table of goods, owned by Koll
  - Sold by Dammon in Act Two
- Notes:
  - It is not listed in-game, but Thermodynamo can only activate once per attack, even when hitting multiple targets with Cleave or similar abilities.

### Thorn Blade
- Rarity: Rare | Slot: Weapon (Scimitars) | Act: Act Two
- Description: Thorn Blade is a rare, lightly enchanted (+1) Scimitar that deals 1d4 Poison damage with melee weapons attacks while Concentrating and grants the ability to cast Ensnaring Strike (Melee).
- Effect: Damage: 1d6 + 1 (2~7) + Strength or Dexterity modifier Slashing | Ensnaring Strike (Melee) (+): Cast as a level 1 spell (Recharge: Long rest.) | Poisonous Synergy: While concentrating, your melee weapon attacks deal an additional 1d4 Poison. | Flourish: Feint an attack to possibly throw your opponent Off Balance. (Recharge: Short rest.) | Lacerate: Slash at your target's vital points to make it Bleed. (Recharge: Short rest.)
- How to get:
  - Last Light Inn X: -33 Y: 164: Sold by Dammon
  - Sold by Dammon
- Notes:
  - Thorn Blade has a chance to reappear in Dammon's merchant stock whenever it resets, like non-unique equipment, and can be acquired multiple times.
  - If a character has two copies of Thorn Blade equipped, their damage bonus while concentrating stacks, resulting in additional 2d4 damage instead of 1d4. This behaviour only applies outside of Honour mode.
- Bugs:
  - The description in Honour Mode is erroneous. Whereas the extra damage normally applies to all melee attacks (as per the description of the weapon), the extra damage in Honour Mode only applies to attacks with the weapon itself. This is because in the normal base game the extra damage is added via the passive, whereas in Honour Mode the damage is derived directly from the weapon itself. The fact that this is at odds with the description of the weapon is likely an oversight.

### Yuan-Ti Scale Mail
- Rarity: Rare | Slot: Medium Armour (Medium) | Act: Act Two
- Description: Yuan-Ti Scale Mail is a rare Medium Armour that adds the wearer's Dexterity Modifier to their Armour Class and also grants a +1 bonus to Initiative.
- Effect: AC 15 | Exotic Material: Add your full Dexterity Modifier to your Armour Class. Additionally, this armour does not impose Disadvantage on Stealth Ability Checks. | Ambusher: Gain a +1 bonus to Initiative Rolls. | File ARM_Scalemail_A_2_Shoulderpads | File ARM_Scalemail_A_Pants_B
- How to get:
  - Last Light Inn X: -31 Y: 130: Sold by Quartermaster Talli near the Last Light Inn waypoint
  - Sold by Quartermaster Talli near the Last Light Inn waypoint
- Bugs:
  - Exotic Material does not work if either the Medium Armour Master or Magic Initiate: Cleric feat is gained. The Magic Initiate: Cleric feat has an unlisted effect that increases the maximum AC bonus from Dexterity while wearing Medium Armour from +2 to +3.


## Last Light Inn Cellar

### Coruscation Ring
- Rarity: Uncommon | Slot: Ring | Act: Act Two
- Description: Coruscation Ring is an uncommon ring that inflicts Radiating Orb on creatures that the wearer deals spell damage to. The wearer must be illuminated for this effect to occur.
- Effect: Arcane Radiance: When the wearer deals spell damage while illuminated by a light source, they also inflict Radiating Orb upon the target for 2 turns.
- How to get:
  - Last Light Inn - Cellar X: 44 Y: -734: in a trapped heavy chest in the cellar of the Last Light Inn
  - in a trapped heavy chest in the cellar of the Last Light Inn
- Notes:
  - The chest is in a secret area, which is reached by going through a set of Double Oak Doors that are blocked by a destructible spiderweb and a pile of crates. The room beyond has a Cracked Wall, which, if broken, grants access to a cavernous area guarded by a pack of Meenlocks. In its far corner, behind another door, stands the chest. Alternatively, the chest can also be reached by going through the cell next to the Evidence Chest. Its left wall can be broken to gain entry into another room with a door that opens into the area with the chest.
  - The chest can be disarmed with a DC 10 Sleight of Hand Check and unlocked with a DC 14 Sleight of Hand Check.
  - This item has great synergy with the Callous Glow Ring. When an enemy receives Radiating Orb from Arcane Radiance, they become illuminated, which causes them to take an additional 2 Radiant damage from the Callous Glow Ring.
  - Multi-hit spells like Eldritch Blast, Magic Missile, and Scorching Ray apply the effect numerous times.
  - Booming Blade is treated as spell damage and thus inflicts Radiating Orb.
- Bugs:
  - Arcane Radiance inflicts Radiating Orb regardless of the wearer's light level.


## Mason's Guild

### Helmet of Arcane Acuity
- Rarity: Uncommon | Slot: Helmet | Act: Act Two
- Description: The Helmet of Arcane Acuity is an uncommon Helmet that imparts Arcane Acuity upon the wearer when they deal damage with a weapon attack.
- Effect: Battle Acuity: Whenever you deal damage with a weapon attack, you gain Arcane Acuity for 2 turns. | Dexterity Saving Throws +1
- How to get:
  - Mason's Guild X: 107 Y: -758: in a locked and trapped Gilded Chest in a secret basement area
  - in a locked and trapped Gilded Chest in a secret basement area
- Notes:
  - The chest can be opened with a DC 14 Sleight of Hand Check, and can be perceived as trapped with a DC 15 Perception Check, then disarmed with a DC 21 Sleight of Hand Check. If lockpicked before disarming, the trap triggers a level 4 Guiding Bolt with a save DC of 15 to negate it.
  - The basement is accessed through a trapdoor in the Mason's Guild, and the secret area can be opened by lockpicking or using the Tower-Shaped Key on the Keyholed Herald.
  - This helmet pairs well with the (bugged) passive Mortal Reminder.
  - Although not explicitly stated in the description, Battle Acuity triggers upon dealing weapon damage to objects as well as creatures.
- Bugs:
  - Battle Acuity triggers multiple times per attack with spells that are considered weapon attacks and include multiple Deal Damage functions, such as Booming Blade and the various Smite spells.


## Mind Flayer Colony

### Blade of Oppressed Souls
- Rarity: Rare | Slot: Weapon (Longswords) | Act: Act Two
- Description: Blade of Oppressed Souls is a rare, lightly enchanted (+1) variant of the Longswords family of weapons. It is a martial melee weapon that can be wielded in one hand, or with both hands for extra damage.
- Effect: One-handed damage: 1d8 + 1 (2~9) + Strength modifier Slashing | Two-handed damage: 1d10 + 1 (2~11) + Strength modifier Slashing | Extra damage: 1d4 (1~4) Psychic | Lacerate: Slash at your target's vital points to make it Bleed. (Recharge: Short rest.) | Pommel Strike: Make a non-lethal attack against an enemy and possibly Daze them. (Recharge: Short rest.) | Rush Attack: Charge forward and attack the first enemy in your way, possibly pushing them Off Balance. (Recharge: Short rest.) | Crowning Strike: Unleash the wails of the dead that fell to your blade, and possibly instil Crown of Madness in the target. (Recharge: Short rest.)
- How to get:
  - Mind Flayer Colony X: 747 Y: -138: In an area unlocked by the Necrotic Laboratory puzzle
  - High Hall X: 235 Y: 44: On a table of goods, owned by Koll
  - In an area unlocked by the Necrotic Laboratory puzzle

### Braindrain Gloves
- Rarity: Uncommon | Slot: Gloves | Act: Act Two
- Description: Braindrain Gloves are an uncommon pair of Gloves that inflicts Mental Fatigue on a foe whenever the wearer deals Psychic damage to them.
- Effect: Mental Interference: When you deal Psychic damage, you also inflict Mental Fatigue for 2 turns.
- How to get:
  - Mind Flayer Colony X: 748 Y: -141: On a skeleton in the Necrotic Laboratory, next to the Blade of Oppressed Souls
  - On a skeleton in the Necrotic Laboratory, next to the Blade of Oppressed Souls
- Notes:
  - In Honour mode, the Psychic damage from Flurry of Moths: Attack does not trigger Mental Interference. However, the separate psychic damage from Prey's Scent against a marked target does trigger it. Both damage instances apply Mental Fatigue outside of the Honour mode ruleset.

### Circle of Bones
- Rarity: Rare | Slot: Helmet | Act: Act Two
- Description: Circle of Bones is a rare Circlet that grants all nearby allied undead Resistance to physical damage, and the wearer can cast Animate Dead once per Long Rest.
- Effect: Animate Dead: Cast as a level 3 spell (Recharge: Long rest.) | Undead Ward: Allied undead within 6 m (20 ft) are Resistant to Bludgeoning, Slashing, and Piercing damage.
- How to get:
  - Gauntlet of Shar X: -845 Y: -793: Carried by Balthazar, at his altar
  - Shadowfell X: -604 Y: -1431: Carried by Balthazar, if he is later confronted near the Nightsong
  - Mind Flayer Colony X: 715 Y: -49: Carried by Balthazar, if he is allowed to abduct the Nightsong
  - Carried by Balthazar, if he is allowed to abduct the Nightsong
- Notes:
  - The Undead Ward feature does not apply to Astarion but does apply to another vampire if one is in the party, even though they do not have the Undead tag.
- Bugs:
  - Summoning a zombie via this item's version of Animate Dead incorrectly summons a Newborn Zombie, which begins decaying, instead of the normal Zombie.
  - Though it is not stated in the tooltip, Undead Ward applies to summoned fiends, such as Shovel, Cambion (Planar Ally), and Conjured Imp.
  - Though Undead Ward states it has a radius of 6 m (20 ft), it actually has a radius of 9 m (30 ft).

### Circlet of Mental Anguish
- Rarity: Rare | Slot: Helmet | Act: Act Two
- Description: The Circlet of Mental Anguish is a rare Circlet that heals the wearer for 1d4 hit points when an enemy fails a Charisma, Intelligence, or Wisdom Saving Throw against one of the wearer's spells or cantrips.
- Effect: Psychic Leech: When an enemy fails a Charisma, Intelligence, or Wisdom Saving Throw against one of your spells or cantrips, you regain 1d4 Hit Points.
- How to get:
  - Mind Flayer Colony X: 748 Y: -141: On a skeleton in the Necrotic Laboratory
  - On a skeleton in the Necrotic Laboratory
- Notes:
  - The healing effect can only heal the caster once per spell, even if multiple creatures fail their saving throws.

### Infernal Rapier
- Rarity: Very Rare | Slot: Weapon (Rapiers) | Act: Act Two
- Description: The Infernal Rapier is a very rare +2 rapier and a possible reward for following Wyll's companion quest. It raises the wielder's Spell Save DC and, unlike other rapiers, uses their Spellcasting Modifier for Attack Rolls and Damage Rolls instead of Strength or Dexterity.
- Effect: Damage: 1d8 + 2 (3~10) + spellcasting modifier Piercing | Planar Ally: Cambion: Cast as a level 6 spell (Recharge: Long rest.) | High Spellcasting: You gain a +1 bonus to Spell Save DC. | Melee Caster: Instead of its Dexterity ability score modifier, the affected entity add its spellcasting modifier to attack rolls. | Piercing Strike: Stab an enemy and possibly inflict Gaping Wounds. (Recharge: Short rest.) | Weakening Strike: Target an enemy's hands with a non-lethal attack and possibly inflict Weak Grip. (Recharge: Short rest.) | Flourish: Feint an attack to possibly throw your opponent Off Balance. (Recharge: Short rest.)
- How to get:
  - Mind Flayer Colony X: 676 Y: 39: Possibly rewarded by Mizora to Wyll if freed during his companion quest, The Blade of Frontiers
  - Possibly rewarded by Mizora to Wyll if freed during his companion quest, ⁠The Blade of Frontiers
- Notes:
  - The party must bring Wyll along when entering the Tadpoling Centre, free Mizora, then pass a DC 14 Persuasion Check check to convince her to give a reward.
  - The summoned Cambion from Planar Ally: Cambion is immediately dismissed if the Infernal Rapier is unequipped.
  - Like Shillelagh and Sylvan Scimitar, this weapon uses the character's highest available spellcasting ability rather than the most recent, or their default spellcasting ability if no other is available.
  - Melee Caster does not benefit other equipped weapons.
- Bugs:
  - Despite not stating such anywhere, and unlike most summons, the Cambion is automatically dismissed if the summoner is Knocked Out.

### Jhannyl's Gloves
- Rarity: Rare | Slot: Gloves | Act: Act Two
- Description: Jhannyl's Gloves are a rare pair of Gloves that let the wearer automatically cast Lesser Restoration on themselves when they become Blinded, Paralysed or Poisoned.
- Effect: Defy Villainy: When the wearer becomes Blinded, Paralysed or Poisoned, they automatically cast Lesser Restoration on themselves. | Saving Throws +1
- How to get:
  - Last Light Inn X: -60 Y: 158: Worn by Isobel if she is killed after dealing with the Nightsong but before completing the assault on Moonrise
  - Mind Flayer Colony X: 861 Y: -23: Worn by Isobel if she is kidnapped by Marcus or killed at Last Light Inn before dealing with the Nightsong
  - Ramazith's Tower: Worn by Isobel if the Nightsong is killed or imprisoned by Lorroakan
  - Campsite (Act Two): Worn by Isobel if she joins the camp
  - Worn by Isobel if she is kidnapped by Marcus or killed at Last Light Inn before dealing with the Nightsong
- Notes:
  - Likely related to Jhannyl's wristlet, a magic item also used by the Harpers.
  - Despite the description, this passive protects from every condition in Diseased, Poisoned, Paralyzed, and Blinded condition groups, plus Bloodless.
  - Prior to Patch 8, this passive had a once-per-long-rest limit, but it was removed and can now trigger an unlimited number of times.
  - Although Jhannyl's Gloves are associated with Isobel (and equipped by her in certain Act Two encounters) the passive from these gloves is hardcoded to function only for player characters, recruited companions, and hirelings. Therefore Isobel cannot make use of this passive's benefits.
- Bugs:
  - This passive emulates Lesser Restoration spell effects without actually casting it, which would trigger effects like Tempestuous Magic: Flight or restore Arcane Ward charges.

### Ketheric's Shield
- Rarity: Rare | Slot: Shield | Act: Act Two
- Description: Ketheric's Shield is a rare Shield. It grants the Shield Bash action, improves the wielder's spellcasting-related rolls, and also gives them Advantage on Dexterity Saving Throws.
- Effect: AC +2 | Arcane Enchantment: You gain a +1 bonus to Spell Save DC and Spell Attack rolls. | Shield Bash: When a foe hits you with a melee attack, you can use your reaction to knock it Prone unless they succeed a Dexterity Saving Throw. | Advantage on Dexterity Saving Throws
- How to get:
  - Mind Flayer Colony X: 861 Y: -23: Carried by Ketheric Thorm when fought atop Moonrise Towers and in the Mind Flayer Colony (see notes)
  - Carried by Ketheric Thorm when fought atop Moonrise Towers and in the Mind Flayer Colony (see notes)
- Notes:
  - This shield can be obtained early – while fighting Ketheric Thorm atop Moonrise Towers – by disarming him, placing any two-handed weapon near him, waiting for him to equip that weapon, then pickpocketing the shield while he is still invulnerable.
  - This reaction triggers the class action Shield Blow against the attacker.
- Bugs:
  - The description of this passive incorreclty states it requires a Dexterity saving throw; it instead requires a Strength saving throw.

### Ketheric's Warhammer
- Rarity: Rare | Slot: Weapon (Warhammers) | Act: Act Two
- Description: Ketheric's Warhammer is a rare, lightly enchanted (+1) variant of the Warhammers family of weapons. It is a martial melee weapon that can be wielded in one hand, or with both hands for extra damage.
- Effect: One-handed damage: 1d8 + 1 (2~9) + Strength modifier Bludgeoning | Two-handed damage: 1d10 + 1 (2~11) + Strength modifier Bludgeoning | Extra damage: 1d4 (1~4) Psychic | Backbreaker: Put extra force behind your strike to possibly knock your enemy Prone. (Recharge: Short rest.) | Concussive Smash: Hit an enemy with all your might to deal damage and possibly Daze them. (Recharge: Short rest.) | Weakening Strike: Target an enemy's hands with a non-lethal attack and possibly inflict Weak Grip. (Recharge: Short rest.)
- How to get:
  - Mind Flayer Colony X: 861 Y: -23: Carried by Ketheric Thorm while fighting in either conflict with him (see notes)
  - Carried by Ketheric Thorm while fighting in either conflict with him (see notes)
- Notes:
  - This weapon can also be obtained by disarming Ketheric Thorm while fighting him atop Moonrise Towers or in the Mind Flayer Colony.

### Moon Devotion Robe
- Rarity: Very Rare | Slot: Clothing | Act: Act Two
- Description: Moon Devotion Robe is a very rare piece of Clothing. It grants Advantage on Constitution Saving Throws as well as the ability to cast Produce Flame and Lunar Bulwark.
- Effect: AC 10 | Lunar Bulwark: Bathe yourself in the shielding magic of Selûne's watchful gaze. (Recharge: Long rest.) | Produce Flame: A flame in your hand sheds a light in a 9 m (30 ft) radius and deals 1d8 Fire damage when thrown. | Selûne's Protection: While the wearer has Mage Armour, each successful Saving Throw causes the source of the Saving Throw to take 1d4 Radiant damage. | File ARM_Isobel_A_Pants | File ARM_Isobel_A_Robe_Skirt_B | Advantage on Constitution Saving Throws. | Saving Throws +1
- How to get:
  - Last Light Inn X: -60 Y: 158: Worn by Isobel after dealing with the Nightsong but before completing the assault on Moonrise Towers
  - Mind Flayer Colony X: 861 Y: -23: Worn by Isobel after being kidnapped by Marcus
  - Ramazith's Tower: Worn by Isobel if the Nightsong is killed or imprisoned by Lorroakan
  - Campsite (Act Two): Worn by Isobel as Camp Follower
  - Worn by Isobel after being kidnapped by Marcus
- Notes:
  - The Produce Flame cantrip granted by the robes always uses Wisdom as the casting ability, regardless of the class' casting ability.
- Bugs:
  - Although Selûne's Protection should be activated by Lunar Bulwark, it is not; the wearer must instead have the regular version of Mage Armour cast on them for its radiant damage to function.
  - Additionally, although the tooltip mentions saving throws without any additional qualifiers, this does not work for saving throws rolled against non-spell effects such as weapon actions. As mentioned in the summary on this page, only successful saves against spells trigger the radiant damage.

### Myrkulite Scourge
- Rarity: Uncommon | Slot: Weapon (Flails) | Act: Act Two
- Description: Myrkulite Scourge is an uncommon +1 Flail that deals an additional 1d6 Necrotic damage on a strike.
- Effect: Damage: 1d8 + 1 (2~9) + Strength modifier Bludgeoning | Extra damage: 1d6 (1~6) Necrotic | Tenacity: When you miss a melee attack, you deal Strength Modifier Bludgeoning damage (minimum of 1) anyway. | Concussive Smash: Hit an enemy with all your might to deal damage and possibly Daze them. (Recharge: Short rest.) | Weakening Strike: Target an enemy's hands with a non-lethal attack and possibly inflict Weak Grip. (Recharge: Short rest.)
- How to get:
  - Moonrise Towers X: -162 Y: -203: Carried by Radija on the first floor
  - Moonrise Towers Rooftop X: -146 Y: -213: Carried by Susdera on the rooftop
  - Mind Flayer Colony X: 727 Y: 41: Carried by Kressa Bonedaughter in the barracks
  - Moonrise Towers Prison X: 597 Y: -655: Carried by Sarabayle after confronting Ketheric Thorm
  - Moonrise Towers Prison X: 596 Y: -651: Carried by Willinx Jindlebee after confronting Ketheric Thorm
  - Carried by Kressa Bonedaughter in the barracks
- Notes:
  - If a weapon action misses, using Tenacity does not trigger its effects.
  - As Tenacity deals weapon damage even if an attack misses, it can trigger many on-hit effects from equipment. For example, from the Gloves of Power, the Callous Glow Ring, weapon coatings, or any infusion from the Ring of Elemental Infusion.
- Bugs:
  - When dual-wielding a flail or morningstar with a non-Tenacity weapon using the Dual Wielder feat, Tenacity can be triggered by missing an attack with the non-Tenacity weapon, dealing Bludgeoning damage regardless of the weapon used. Some non-Tenacity weapons can trigger their on-hit effects via Tenacity as well, such as the Ritual Dagger and Loviatar's Scourge.
  - As Horde Breaker (Melee) rolls invisible, zero-damage weapon attacks against all enemies in the Horde Breaker area of effect, Tenacity can be prompted to trigger against them even if the first attack hits. It is therefore possible to score 2 hits in one attack: the full attack against the original Horde Breaker target and a Tenacity hit against another target.

### Reaper's Embrace
- Rarity: Very Rare | Slot: Heavy Armour (Heavy) | Act: Act Two
- Description: Reaper's Embrace is a very rare heavy Armour that reduces incoming damage by 2 and makes the wearer immune to being moved by force. It also grants the Howl of the Dead class action.
- Effect: AC 19 | Howl of the Dead: Let out a bone-chilling howl that Numbs all nearby creatures. (Recharge: Short rest.) | Magical Plate: All incoming damage is reduced by 2. | Reaper's Rigidity: When activated, you can't be moved against your will by any spell or action, but have Disadvantage on Dexterity Saving Throws. | Disadvantage on Stealth checks.
- How to get:
  - Mind Flayer Colony X: 861 Y: -23: Worn by Ketheric Thorm
  - Worn by Ketheric Thorm
- Bugs:
  - When equipped on characters who have Body Type 4 the shoulder pauldrons of this armour may appear stretched or distorted, particularly when viewed from the side. Body Type 4 is Strong Masculine, and is available for Humans (e.g., Minsc), Elves, Drow, Half-Elves (e.g., Halsin), and Tieflings.


## Moonrise Towers

### Absolute's Protector
- Rarity: Rare | Slot: Shield | Act: Act Two
- Description: Absolute's Protector is a rare Shield that reduces damage from spells by 1 if the user bears the mark of the Absolute, grants Shield Bash, and allows the wielder to cast Fire Shield: Chill once per Long Rest.
- Effect: AC +2 | Fire Shield: Chill: Cast as a level 4 spell (Recharge: Long rest.) | Absolute's Aegis: If the wielder bears the Absolute's Brand, all damage received from spells is reduced by 1. | Shield Bash: When a foe hits you with a melee attack, you can use your reaction to knock it Prone unless they succeed a Dexterity Saving Throw.
- How to get:
  - Moonrise Towers X: -150 Y: -202: Carried by Z'rell
  - Carried by Z'rell
- Notes:
  - This reaction triggers the class action Shield Blow against the attacker.
- Bugs:
  - The description of this passive incorreclty states it requires a Dexterity saving throw; it instead requires a Strength saving throw.

### Argument Solver
- Rarity: Uncommon | Slot: Weapon (Melee weapon) | Act: Act Two
- Description: Argument Solver is an uncommon +1 Greatclub that grants the wielder the Poison Mist weapon action, which deals extra Poison damage and creates a poison cloud.
- Effect: Damage: 1d8 + 1 (2~9) + Strength modifier Bludgeoning | Greatclubs | Tenacity: When you miss a melee attack, you deal Strength Modifier Bludgeoning damage (minimum of 1) anyway. | Concussive Smash: Hit an enemy with all your might to deal damage and possibly Daze them. (Recharge: Short rest.) | Backbreaker: Put extra force behind your strike to possibly knock your enemy Prone. (Recharge: Short rest.) | Poison Mist: On a hit, deal extra Poison damage equal to your proficiency bonus and surround the target in a noxious cloud that possibly Poisons those within it. (Recharge: Short rest.)
- How to get:
  - Moonrise Towers X: -196 Y: -195: Carried by Mig on the main floor
  - Carried by Mig on the main floor
- Notes:
  - If a weapon action misses, using Tenacity does not trigger its effects.
  - As Tenacity deals weapon damage even if an attack misses, it can trigger many on-hit effects from equipment. For example, from the Gloves of Power, the Callous Glow Ring, weapon coatings, or any infusion from the Ring of Elemental Infusion.
  - Targets inside the Poison Cloud created by Poison Mist roll their saving throws against your spell save DC rather than your weapon action DC.
  - This action is actually an AoE attack. After striking the main target, an additional attack is made against every creature and object within the 1.5 m (5 ft) cloud radius around that target, including allies. Additional poison clouds are then spawned for each creature and object struck this way.
- Bugs:
  - As Horde Breaker (Melee) rolls invisible, zero-damage weapon attacks against all enemies in the Horde Breaker area of effect, Tenacity can be prompted to trigger against them even if the first attack hits. It is therefore possible to score 2 hits in one attack: the full attack against the original Horde Breaker target and a Tenacity hit against another target.

### Armour of Devotion
- Rarity: Rare | Slot: Heavy Armour (Heavy) | Act: Act Two
- Description: Armour of Devotion is a set of rare Full Plate Heavy Armour that allows the wearer to cast Eternal Devotion, restoring a charge of their Paladin Channel Oath ability.
- Effect: AC 18 | Eternal Devotion: Recite your Oath to regain 1 Channel Oath Charge. (Recharge: Long rest.) | Disadvantage on Stealth checks.
- How to get:
  - Moonrise Towers X: -174 Y: -179: Sold by Roah Moonglow on the main floor
  - Sold by Roah Moonglow on the main floor

### Bigboy's Chew Toy
- Rarity: Rare | Slot: Weapon (Quarterstaves) | Act: Act Two
- Description: Bigboy's Chew Toy is a rare +1 Quarterstaff that grants its wielder the ability to cast Enlarge on themselves once per Long Rest.
- Effect: One-handed damage: 1d6 + 1 (2~7) + Strength modifier Bludgeoning | Two-handed damage: 1d8 + 1 (2~9) + Strength modifier Bludgeoning | Whossa Large Fellow?: Grow in size to become stronger. (Recharge: Long rest.) | Concussive Smash: Hit an enemy with all your might to deal damage and possibly Daze them. (Recharge: Short rest.) | Flourish: Feint an attack to possibly throw your opponent Off Balance. (Recharge: Short rest.) | Topple: Swipe at a creature to knock it Prone. (Recharge: Short rest.)
- How to get:
  - Moonrise Towers X: -164 Y: -167: Sold by Lann Tarv on the main floor of Moonrise Towers
  - Sold by Lann Tarv on the main floor of Moonrise Towers

### Boots of Arcane Bolstering
- Rarity: Rare | Slot: Boots | Act: Act Two
- Description: Boots of Arcane Bolstering is a pair of rare Boots that grants Arcane Charge each time the wearer Dashes, adding +1 bonus to damage with spells while Threatened.
- Effect: Rapid Caster: Each time they Dash, the wearer gains Arcane Charge for 2 turns.
- How to get:
  - Moonrise Towers X: -128 Y: -193: Sold by Araj Oblodra on the main floor
  - Lower City X: -92 Y: -78: Sold by Araj Oblodra in Crimson Draughts if not acquired from her in Act Two
  - Sold by Araj Oblodra on the main floor
- Notes:
  - Using Dash repeatedly does not increase Arcane Charge above 2 turns.

### Circlet of Hunting
- Rarity: Very Rare | Slot: Helmet | Act: Act Two
- Description: The Circlet of Hunting is a very rare circlet which grants a +1d4 bonus to Attack Rolls against marked creatures.
- Effect: Hunter's Eye: You gain a +1d4 bonus to Attack Rolls against creatures marked by Hunter's Mark, True Strike, Faerie Fire, or Guiding Bolt.
- How to get:
  - Moonrise Towers X: -128 Y: -193: Sold by Araj Oblodra on the main floor
  - Lower City X: -92 Y: -78: Sold by Araj Oblodra in Crimson Draughts if not acquired from her in Act Two
  - Sold by Araj Oblodra on the main floor
- Notes:
  - Though not stated in the description, Hunter's Eye also functions with Hex.
- Bugs:
  - Hunter's Eye requires the wearer to be the source of the mentioned conditions on the target; it does not provide an attack roll bonus if another character is the source of the conditions.

### Cloak of Elemental Absorption
- Rarity: Uncommon | Slot: Cloak | Act: Act Two
- Description: Cloak of Elemental Absorption is an uncommon Cloak that allows the wearer to absorb a small amount of magical damage, and add it to their next attack.
- Effect: Absorb Elements: Absorb elemental damage once per Short Rest. Take half damage from the next elemental attack targeting you, and deal an additional 1d6 of that element type on your next attack.
- How to get:
  - Moonrise Towers X: -170 Y: -171: In an opulent chest in Ketheric Thorm's chambers on the second floor
  - In an opulent chest in Ketheric Thorm's chambers on the second floor
- Notes:
  - Absorb Elements additional elemental damage applies only to weapon attacks, and can apply its damage bonus multiple times to a single weapon attack.
  - This reaction halves damage by granting resistance to the elemental damage type when triggered. Since resistances do not stack, this will not reduce the damage further if the user already has the applicable resistances.
  - Absorb Elements can apply its damage bonus multiple times to a single weapon attack.
- Bugs:
  - Due to a coding error, Absorb Elements only functions once per Long Rest instead of once per Short Rest.
  - This reaction cannot be used while affected by Starry Form.

### Coldbrim Hat
- Rarity: Uncommon | Slot: Helmet | Act: Act Two
- Description: Coldbrim Hat is an uncommon Hat where, once per turn, if a condition is inflicted on the target, the hat also applies 2 turns of Encrusted with Frost.
- Effect: Coldbrim Chill: Once per turn, any condition inflicted on a target, also applies 2 turns of Encrusted with Frost.
- How to get:
  - Moonrise Towers X: -155 Y: -173: In a locked chest in a hidden room behind a bookcase in Balthazar's Chambers
  - Sorcerous Sundries: On a table by the Lava Elemental
  - In a locked chest in a hidden room behind a bookcase in Balthazar's Chambers
- Notes:
  - Coldbrim Chill only affects a single target per turn.
  - The wording of the description may be slightly confusing. Specifically, the fact that the Coldbrim Chill effect only applies once throughout the turn, meaning that an area of effect spell like Hypnotic Pattern only applies to the first target hit and only once that turn, not to all targets. Applying Encrusted with Frost to a target is specifically excluded from conditions that trigger this passive.
- Bugs:
  - Coldbrim Chill triggers under many circumstances even though it appears it should not, due to hidden technical conditions, such as when a ranged weapon attack misses, when Sanctuary is cast near enemies, or when revealing an invisible enemy with See Invisibility.

### Derivation Cloak
- Rarity: Rare | Slot: Cloak | Act: Act Two
- Description: Derivation Cloak is a rare Cloak which heals the wearer for 1d4 Hit Points when they Poison a foe.
- Effect: Deadly Derivation: When you Poison a foe, heal yourself for 1d4 Hit Points.
- How to get:
  - Moonrise Towers X: -132 Y: -175: In a heavy chest in Balthazar's chambers on the First Floor
  - In a heavy chest in Balthazar's chambers on the First Floor
- Notes:
  - There are four Poisoned conditions reusing the same icon, which can be confusing. The most general one is Poisoned, and it's the only one considered by this passive. That means there will be no healing via the following similar conditions: Poisoned (Basic Poison) condition caused by a weapon coated in Basic Poison. But the same item when thrown generates a Poison Cloud, which can cause the correct Poisoned condition, triggering this passive.
  - Poisoned (Suspicious Poison) condition caused by drinking or throwing Suspicious Poison.
  - Poisoned (Spider Meat) condition caused by consuming Spider meat.
  - This passive has great synergy when combined with Poisoner's Gloves and Broodmother's Revenge. Every attack can cause Poisoned, healing the character and refreshing the poison coating.

### Drakethroat Glaive
- Rarity: Rare | Slot: Weapon (Glaives) | Act: Act Two
- Description: Drakethroat Glaive is a rare +2 Glaive that grants its wielder the Draconic Elemental Weapon weapon action and a bonus to Dragonborn breath racial actions.
- Effect: Damage: 1d10 + 2 (3~12) + Strength modifier Slashing | Draconic Elemental Weapon: Cast as a level 3 spell (Recharge: Long rest.) | Vicious Dragon Breath: Enemies have Disadvantage on Saving Throws against your dragonborn breath weapon. | Rush Attack: Charge forward and attack the first enemy in your way, possibly pushing them Off Balance. (Recharge: Short rest.) | Lacerate: Slash at your target's vital points to make it Bleed. (Recharge: Short rest.) | Cleave: Swing your weapon in a large arc to attack up to 3 enemies at once. They each take half the damage your weapon usually deals. (Recharge: Short rest.)
- How to get:
  - Moonrise Towers X: -174 Y: -179: Sold by Roah Moonglow on the main floor
  - Sold by Roah Moonglow on the main floor
- Notes:
  - The Draconic Elemental Weapon spell can be used to enchant a weapon other than the Drakethroat Glaive. This can be done by either dropping the intended weapon on the ground and then casting the spell on it or by having another party member equip that weapon and casting the spell on them. A sorcerer of level 3 or higher can target two weapons using Metamagic: Twinned Spell.
  - Vicious Dragon Breath only affects a dragonborn's racial breath weapon, not a Circle of the Stars druid's Dazzling Breath.

### Dwarven Splintmail
- Rarity: Rare | Slot: Heavy Armour (Heavy) | Act: Act Two
- Description: Dwarven Splintmail is a rare heavy armour that reduces Piercing damage by 1 and grants a +1 bonus to Strength Saving Throws and Ability Checks. In addition, it also boosts the user's Constitution by 2.
- Effect: AC 19 | Superior Plate: You take 1 less Piercing damage. | Body Aid: Gain a +1 bonus to Strength Saving Throws and Ability Checks. | Constitution +2 (Max 20) | Disadvantage on Stealth checks.
- How to get:
  - Moonrise Towers X: -164 Y: -167: Sold by Lann Tarv on the main floor
  - Sold by Lann Tarv on the main floor
- Notes:
  - Disciple Z'rell must be convinced to give additional aid in finding Ketheric's relic.
  - This item refreshes in Lann Tarv's inventory after every long rest, allowing the purchase of multiple copies.
  - This armour bears some rather distinctive rear-facing heraldry on its front. When worn (particularly by larger body types such the Male Human/Elf "Body 2" or "Body 4"), a set of six dwarven figures are depicted. While five of the figures are shown in traditional, often stoic poses, the figure on the middle of wearer's right side is bent over, facing away from the observer with his trousers lowered, effectively 'mooning' anyone looking at it.
  - The bonus to Strength ability checks from Body Aid does not appear on the character, but is correctly added when rolled.

### Enraging Heart Garb
- Rarity: Rare | Slot: Clothing | Act: Act Two
- Description: The Enraging Heart Garb is a rare piece of Clothing that grants Wrath while the wearer is Raging. It also increases Constitution by 2.
- Effect: AC 10 | Ruintamer Heart: While Raging, the wearer generates 2 turns of Wrath. | File ARM_Barbarian Magical_A_Body | File ARM_Barbarian Magical_A_Chest | File ARM_Barbarian Magical_A_Pants | Constitution +2 (up to 20)
- How to get:
  - Moonrise Towers X: -164 Y: -167: Sold by Lann Tarv on the main floor
  - Sold by Lann Tarv on the main floor
- Bugs:
  - Switching from camp clothing to default view briefly (about 4 frames) shows the character from the waist up with no clothing.
  - Ruintamer Heart has no effect, and does not function in-game.

### Fistbreaker Helm
- Rarity: Rare | Slot: Helmet | Act: Act Two
- Description: Fistbreaker Helm is an rare Helmet that grants a +1 bonus to Spell Save DC and +1 to Initiative Rolls.
- Effect: High Spellcasting: You gain a +1 bonus to Spell Save DC. | Seldom Caught Unawares: You gain a +1 bonus to Initiative rolls.
- How to get:
  - Moonrise Towers X: -164 Y: -167: Sold by Lann Tarv on the main floor
  - Sold by Lann Tarv on the main floor

### Gauntlets of Surging Accuracy
- Rarity: Rare | Slot: Gloves | Act: Act Two
- Description: Gauntlets of Surging Accuracy are a rare pair of gloves that give the wearer a +1d4 bonus to Attack Rolls for the rest of their turn when using Action Surge.
- Effect: Surge Accuracy: When you use Action Surge, gain a +1d4 bonus to Attack Rolls for the rest of your turn. | Strength Saving Throws +1
- How to get:
  - Moonrise Towers X: -164 Y: -167: Sold by Lann Tarv on the main floor
  - Sold by Lann Tarv on the main floor
- Notes:
  - Disciple Z'rell must be convinced to give additional aid in finding Ketheric's relic.

### Gloves of Crushing
- Rarity: Rare | Slot: Gloves | Act: Act Two
- Description: Gloves of Crushing are a rare pair of gloves that enhance unarmed attack rolls and grant bonus Bludgeoning damage to unarmed attacks.
- Effect: Crushing Blows: The wearer gains a +1 bonus to unarmed Attack Rolls and their unarmed attacks deal an additional 2 Bludgeoning damage.
- How to get:
  - Moonrise Towers X: -174 Y: -179: Sold by Roah Moonglow on the main floor
  - Sold by Roah Moonglow on the main floor
- Notes:
  - Crushing Blows affects both melee unarmed strikes and Throw attacks, but provides no extra damage on Throws.
- Bugs:
  - Crushing Blows applies its attack roll bonus twice.

### Gloves of The Duellist
- Rarity: Rare | Slot: Gloves | Act: Act Two
- Description: Gloves of The Duellist are a rare pair of Gloves that enhance melee weapon Attack Rolls when the wearer only holds one weapon in their main hand.
- Effect: Duelling Gloves: While only holding one weapon in your main hand and nothing in your free hand, gain a +2 bonus to melee weapon Attack Rolls.
- How to get:
  - Moonrise Towers X: -164 Y: -167: Sold by Lann Tarv on the main floor
  - Sold by Lann Tarv on the main floor
- Notes:
  - The description of effect is misleading. Like the Duelling fighting style, the bonus from Duelling Gloves remains active even if the wearer has a shield in their offhand, as long as they do not have a weapon in their offhand. It also deactivates if the wearer uses a versatile weapon alone (in two-hand mode), but remains active if they wield a versatile weapon alongside a shield.

### Halberd of Vigilance
- Rarity: Very Rare | Slot: Weapon (Halberds) | Act: Act Two
- Description: Halberd of Vigilance is a very rare +2 Halberd that deals additional Force damage, gives a bonus to Initiative, and grants Advantage on Perception checks and Reactions.
- Effect: Damage: 1d10 + 2 (3~12) + Strength modifier Slashing | Extra damage: 1d4 (1~4) Force | Sentinel Weapon: Gain a +1 bonus to Initiative rolls and Advantage on Perception Ability Checks. | Adroit Reflexes: When you make an Attack Roll as a Reaction, you make it with Advantage. | Rush Attack: Charge forward and attack the first enemy in your way, possibly pushing them Off Balance. (Recharge: Short rest.) | Lacerate: Slash at your target's vital points to make it Bleed. (Recharge: Short rest.) | Cleave: Swing your weapon in a large arc to attack up to 3 enemies at once. They each take half the damage your weapon usually deals. (Recharge: Short rest.)
- How to get:
  - Moonrise Towers X: -164 Y: -167: Sold by Lann Tarv on the main floor
  - Sold by Lann Tarv on the main floor

### Hat of Storm Scion's Power
- Rarity: Uncommon | Slot: Helmet | Act: Act Two
- Description: Hat of Storm Scion's Power is an uncommon hat that grants Arcane Acuity whenever the wearer deals Thunder damage.
- Effect: Thunderous Acuity: Whenever the wearer deals Thunder damage, they gain Arcane Acuity.
- How to get:
  - Moonrise Towers X: -128 Y: -193: Sold by Araj Oblodra on the main floor
  - Lower City X: -92 Y: -78: Sold by Araj Oblodra in Crimson Draughts if not acquired from her in Act Two
  - Sold by Araj Oblodra on the main floor
- Notes:
  - If the Drakethroat Glaive is used to enchant a weapon with Thunder damage and the weapon's wielder is wearing the Hat of Storm Scion's Power, then Thunderous Acuity becomes functionally identical to Battle Acuity from the Helmet of Arcane Acuity, a beneficial feature for classes without light armour proficiency.
  - The Thunder damage must directly originate from the wearer, so conditions like Singing Sword: Shrieking (outside of Honour mode) and Thunder damage caused by Reverberation does not trigger the passive.
- Bugs:
  - Though not stated, Thunderous Acuity only functions once per attack and applies 2 turns of Arcane Acuity.

### Iron-Banded Shield +1
- Rarity: Rare | Slot: Shield | Act: Act Two
- Description: Iron-Banded Shield +1 is a rare Shield with an enchantment increasing its Armour Class bonus.
- Effect: AC +3 | Enchantment: + 1 | No special properties, beyond the Armour Class enchantment.
- How to get:
  - Moonrise Towers X: -164 Y: -163: leaning against a rack next to the bugbear merchant Lann Tarv
  - Wyrm's Rock Fortress X: 20 Y: 202: on a table outside the Audience Hall
  - leaning against a rack next to the bugbear merchant Lann Tarv

### Iron-Banded Shield +1
- Rarity: Rare | Slot: Shield | Act: Act Two
- Description: Iron-Banded Shield +1 is a rare Shield with an enchantment increasing its Armour Class bonus.
- Effect: AC +3 | Enchantment: + 1 | No special properties, beyond the Armour Class enchantment.
- How to get:
  - Moonrise Towers X: -164 Y: -163: leaning against a rack next to the bugbear merchant Lann Tarv
  - Wyrm's Rock Fortress X: 20 Y: 202: on a table outside the Audience Hall
  - leaning against a rack next to the bugbear merchant Lann Tarv

### Marksmanship Hat
- Rarity: Uncommon | Slot: Helmet | Act: Act Two
- Description: Marksmanship Hat is an uncommon hat that grants its wearer a bonus to ranged and thrown attack rolls.
- Effect: Marksmanship: You gain a +1 bonus to Ranged Attack Rolls and Thrown Attack Rolls.
- How to get:
  - Moonrise Towers X: -174 Y: -179: Sold by Roah Moonglow on the main floor
  - Sold by Roah Moonglow on the main floor
- Notes:
  - The bonus also applies to spell attack rolls.
- Bugs:
  - Marksmanship only applies to ranged weapons in the main hand, thus Hand Crossbows equipped in the off-hand are unaffected.

### Moonlantern
- Rarity: Story Item | Slot: Weapon (Clubs) | Act: Act Two
- Description: The Moonlantern is a special utility item that sheds a magical Light in a large radius while equipped.
- Effect: One-handed damage: 1d4 (1~4) + Strength modifier Bludgeoning | Two-handed damage: 1d6 (1~6) + Strength modifier Bludgeoning
- How to get:
  - Ruined Battlefield X: 0 Y: -15: Carried by Kar'niss, either after the Harper ambush or at the top of Moonrise Towers
  - Last Light Inn X: -63 Y: 172: Given by Isobel if letting the Harpers take the Moonlantern
  - Moonrise Towers: In Balthazar's room in Moonrise Towers
  - In Balthazar's room in Moonrise Towers
- Notes:
  - The Moonlantern carried by Kar'niss contains a foul-mouthed pixie Dolly Dolly Dolly who wants out. If freed using Inspect Moonlantern, she grants the party a Pixie Blessing.
  - If Dolly is freed, her Moonlantern remains in the inventory of the character who freed her, but its inventory icon changes to a broken version and the lantern cannot be equipped anymore.
  - If Kar'niss arrives at Moonrise Towers with the lantern (whether he escorted the party or not), Dolly dies inside it.
  - If Kar'niss is killed at the ambush and the lantern is taken by the Harpers, the party can follow them back to Last Light Inn. There Isobel gives the party the same Moonlantern with Dolly Dolly Dolly alive inside; she can be freed and the Pixie Blessing may then still be obtained.
  - Switching to ranged weapons while having a Moonlantern equipped retains the Moonshield effect but removes the illumination, allowing darkness-requiring effects such as Covert Critical and Shadow Step to be safely used within the Shadow-Cursed Lands.
  - See also: Broken Moonlantern
  - Dead Pixie
  - Filigreed Feywild Bell
  - Shadow Lantern
- Bugs:
  - The Moonlantern containing Dolly Dolly Dolly still produces a stationary Moonshield Aura when dropped on the ground even after she has been freed from it.

### Myrkulite Scourge
- Rarity: Uncommon | Slot: Weapon (Flails) | Act: Act Two
- Description: Myrkulite Scourge is an uncommon +1 Flail that deals an additional 1d6 Necrotic damage on a strike.
- Effect: Damage: 1d8 + 1 (2~9) + Strength modifier Bludgeoning | Extra damage: 1d6 (1~6) Necrotic | Tenacity: When you miss a melee attack, you deal Strength Modifier Bludgeoning damage (minimum of 1) anyway. | Concussive Smash: Hit an enemy with all your might to deal damage and possibly Daze them. (Recharge: Short rest.) | Weakening Strike: Target an enemy's hands with a non-lethal attack and possibly inflict Weak Grip. (Recharge: Short rest.)
- How to get:
  - Moonrise Towers X: -162 Y: -203: Carried by Radija on the first floor
  - Moonrise Towers Rooftop X: -146 Y: -213: Carried by Susdera on the rooftop
  - Mind Flayer Colony X: 727 Y: 41: Carried by Kressa Bonedaughter in the barracks
  - Moonrise Towers Prison X: 597 Y: -655: Carried by Sarabayle after confronting Ketheric Thorm
  - Moonrise Towers Prison X: 596 Y: -651: Carried by Willinx Jindlebee after confronting Ketheric Thorm
  - Carried by Radija on the first floor
- Notes:
  - If a weapon action misses, using Tenacity does not trigger its effects.
  - As Tenacity deals weapon damage even if an attack misses, it can trigger many on-hit effects from equipment. For example, from the Gloves of Power, the Callous Glow Ring, weapon coatings, or any infusion from the Ring of Elemental Infusion.
- Bugs:
  - When dual-wielding a flail or morningstar with a non-Tenacity weapon using the Dual Wielder feat, Tenacity can be triggered by missing an attack with the non-Tenacity weapon, dealing Bludgeoning damage regardless of the weapon used. Some non-Tenacity weapons can trigger their on-hit effects via Tenacity as well, such as the Ritual Dagger and Loviatar's Scourge.
  - As Horde Breaker (Melee) rolls invisible, zero-damage weapon attacks against all enemies in the Horde Breaker area of effect, Tenacity can be prompted to trigger against them even if the first attack hits. It is therefore possible to score 2 hits in one attack: the full attack against the original Horde Breaker target and a Tenacity hit against another target.

### Ne'er Misser
- Rarity: Rare | Slot: Weapon (Hand_Crossbows) | Act: Act Two
- Description: The Ne'er Misser is a rare + 1 Hand Crossbow that deals Force damage on its attacks and grants the wearer the ability to cast Magic Missile once per short rest as a 3rd level Spell.
- Effect: Damage: 1d6 + 1 (2~7) + Dexterity modifier Force | Magic Missile: Cast as a level 3 spell (Recharge: Short rest.) | Piercing Shot: Deal regular damage and possibly inflict Gaping Wounds which cause extra damage on attacks. (Recharge: Short rest.) | Mobile Shot: After using Dash or Disengage this turn, you can make a ranged attack as a bonus action. (Recharge: Short rest.)
- How to get:
  - Moonrise Towers X: -174 Y: -179: Sold by Roah Moonglow on the main floor
  - Sold by Roah Moonglow on the main floor
- Notes:
  - The version of Magic Missile granted by this crossbow has a unique casting animation where the player shoots the darts directly from the crossbow itself.

### Poisoner's Ring
- Rarity: Uncommon | Slot: Ring | Act: Act Two
- Description: The Poisoner's Ring is an uncommon Ring which allows the wearer to cast Virulent Venom.
- Effect: Virulent Venom: Point your ringed finger at a target to make it vulnerable to Poison damage, unless it is immune to Poison damage. (Recharge: Long rest.)
- How to get:
  - Moonrise Towers X: -174 Y: -179: Sold by Roah Moonglow on the main floor
  - Sold by Roah Moonglow on the main floor
- Notes:
  - Contrary to the description, Virulent Venom may be cast on up to three targets, or up to three times on the same target.
  - A target does not automatically receive Poison vulnerability. It must first fail a DC 14 Constitution Saving Throw. Targets that have Poison resistance lose the resistance (instead of becoming vulnerable).
  - Targets that have Poison immunity will see no change, despite being able to be targeted by this effect.

### Render of Mind and Body
- Rarity: Uncommon | Slot: Weapon (Shortswords) | Act: Act Two
- Description: Render of Mind and Body is an uncommon +1 Shortsword that deals additional Psychic damage whenever the attack is made at Advantage.
- Effect: Damage: 1d6 + 1 (2~7) + Strength or Dexterity modifier Piercing | Psychic Steel Virtuoso: When the wielder attacks with Advantage, they deal an additional 1d8 Psychic. | Flourish: Feint an attack to possibly throw your opponent Off Balance. (Recharge: Short rest.) | Piercing Strike: Stab an enemy and possibly inflict Gaping Wounds. (Recharge: Short rest.)
- How to get:
  - Moonrise Towers X: -164 Y: -167: Sold by Lann Tarv on the main floor
  - Sold by Lann Tarv on the main floor
- Notes:
  - Disciple Z'rell needs to be convinced to give additional aid in finding Ketheric's relic.
  - Psychic Steel Virtuoso works only for attacks made by a weapon with this Psychic Steel Virtuoso.
  - Psychic Steel Virtuoso requires an attack to have Advantage prior to the attack being made, and as such will not function with Reckless Attack.

### Ring of Free Action
- Rarity: Rare | Slot: Ring | Act: Act Two
- Description: Ring of Free Action is a rare Ring which allows the wearer to ignore the effects of Difficult Terrain and confers immunity to Paralysis and being Restrained.
- Effect: Unwavering: You ignore the effects of Difficult Terrain, and cannot be Paralysed or Restrained.
- How to get:
  - Moonrise Towers X: -128 Y: -193: Sold by Araj Oblodra on the main floor
  - Lower City X: -92 Y: -78: Sold by Araj Oblodra in Crimson Draughts if not acquired from her in Act Two
  - Sold by Araj Oblodra on the main floor
- Notes:
  - This passive grants immunity to the following conditions: All conditions in the Paralyzed status group
  - All conditions in the Restrained status group
  - Some[verify] conditions in the Difficult Terrain status group Difficult Terrain
  - Difficult Terrain: Lava
  - Difficult Terrain: Mud
  - Difficult Terrain: Vines
  - Difficult Terrain: Web
  - Plant Growth
  - Hamstrung
  - Maimed
  - Pinned Down
  - This passive does not prevent the wearer from slipping on Ice or Grease surfaces.
- Bugs:
  - Unwavering does not prevent Difficult Terrain: Deep Water.

### Ring of Spiteful Thunder
- Rarity: Uncommon | Slot: Ring | Act: Act Two
- Description: The Ring of Spiteful Thunder is a uncommon Ring that may Daze Reverberating creatures upon which the wearer deals Thunder damage.
- Effect: Spiteful Thunder: When the wearer deals damage to a Reverberating creature, it becomes Dazed unless it succeeds a Constitution Saving Throw.
- How to get:
  - Moonrise Towers X: -174 Y: -179: Sold by Roah Moonglow on the main floor
  - Sold by Roah Moonglow on the main floor
- Notes:
  - This ring pairs well with conditions which inflict disadvantage on constitution saving throws (e.g., Bleeding), and items which inflict reverberation (e.g., Boots of Stormy Clamour).
  - Spiteful Thunder can be used to inflict Dazed every turn with minimal effort. Dazed makes it more difficult for enemies to save against certain spells like Tasha's Hideous Laughter. This can be very helpful against boss enemies with Legendary Resistance and Magic Resistance.
  - The saving throw is hidden and not shown in the combat log.
- Bugs:
  - If a hireling is dismissed with the Ring of Spiteful Thunder equipped, then they are later resummoned, the ring will have turned into a nonmagical version of itself. This is due to the item template not including the ring's Stats entry.
  - Spiteful Thunder requires targets affected by Reverberation to make a save upon receiving any type of damage from the wearer, not just Thunder.

### Risky Ring
- Rarity: Rare | Slot: Ring | Act: Act Two
- Description: The Risky Ring is a rare Ring. The wearer gains Advantage on Attack Rolls but receives Disadvantage on Saving Throws.
- Effect: Risky Attack: You gain Advantage on Attack Rolls and receive Disadvantage on Saving Throws.
- How to get:
  - Moonrise Towers X: -128 Y: -193: Sold by Araj Oblodra on the main floor
  - Lower City X: -92 Y: -78: Sold by Araj Oblodra in Crimson Draughts if not acquired from her in Act Two
  - Sold by Araj Oblodra on the main floor

### Robe of Exquisite Focus
- Rarity: Rare | Slot: Clothing | Act: Act Two
- Description: The Robe of Exquisite Focus is a rare article of Clothing that increases its wearer's Spell Save DC.
- Effect: AC 10 | High Spellcasting: You gain a +1 bonus to Spell Save DC.
- How to get:
  - Moonrise Towers X: -128 Y: -193: Sold by Araj Oblodra on the main floor
  - Lower City X: -92 Y: -78: Sold by Araj Oblodra in Crimson Draughts if not acquired from her in Act Two
  - Sold by Araj Oblodra on the main floor
- Notes:
  - Despite having less features, this robe sells for more than three times the value of The Protecty Sparkswall.

### Sentinel Shield
- Rarity: Rare | Slot: Shield | Act: Act Two
- Description: Sentinel Shield is a rare Shield that provides the user +3 to Initiative rolls and advantage on Perception checks
- Effect: AC +2 | Shield Blow: When struck by a melee attack, your attacker must succeed a Dexterity Saving Throw or fall Prone. | Heightened Awareness: Gain a +3 bonus to Initiative rolls and Advantage on Perception Checks.
- How to get:
  - Moonrise Towers X: -164 Y: -167: Sold by Lann Tarv on the main floor
  - Sold by Lann Tarv on the main floor

### Shadow Lantern
- Rarity: Rare | Slot: Weapon (Clubs) | Act: Act Two
- Description: The Shadow Lantern is a unique type of Moonlantern which provides a Moonshield and grants the unique Conjure Shadow Lantern Wraith spell.
- Effect: One-handed damage: 1d4 (1~4) + Strength modifier Bludgeoning | Two-handed damage: 1d6 (1~6) + Strength modifier Bludgeoning | Conjure Shadow Lantern Wraith: Cast as a level 6 spell (Recharge: Long rest.)
- How to get:
  - Moonrise Towers X: -150 Y: -165: Gale can craft one from a Broken Moonlantern and Dead Pixie at the table within Balthazar's hidden room.
  - Gale can craft one from a Broken Moonlantern and Dead Pixie at the table within Balthazar's hidden room.
- Notes:
  - Both ingredients can be found in Baltazar's hidden room.
  - See Balthazar's Experiment for more information. While in-game dialogue also allows the slim possibility for the player character to craft this item, the option is only available if Gale is present.
  - Merely equipping the lantern in the light source slot is not sufficient to gain the Conjure Shadow Lantern Wraith ability and the Moonshield condition; it must be actively wielded, such as by switching to it via the light source toggle button or equipping it directly in the weapon slot.
  - Although not clear from the flavour text's description, the lantern emits a bright sphere of light when used in a weapon slot, providing full protection from the Shadow Curse.
  - Unequipping the lantern or switching back to active weapons via the light source toggle button automatically dismisses the conjured Shadow.
- Bugs:
  - Despite being tagged as a Rare item, the in-game tooltip for the lantern is coloured as a Story Item, like any other Moonlantern.
  - Despite this spell's name, the creature summoned is a Shadow, not the more powerful Wraith. It is is unable to climb surfaces such as ladders and knotted roots, and is unable to Jump, Fly, or Warp, meaning it may be unable to follow the party to certain areas. Regrouping is possible by entering a new area or using Waypoints.

### Sharpened Snare Cuirass
- Rarity: Very Rare | Slot: Medium Armour (Medium) | Act: Act Two
- Description: Sharpened Snare Cuirass is a very rare Medium Armour that adds your full Dexterity Modifier to your Armour Class. Enemies also have Disadvantage when resisting your attacks and Saving Throws that inflict Restrained.
- Effect: AC 14 | Exotic Material: Add your full Dexterity Modifier to your Armour Class. Additionally, this armour does not impose Disadvantage on Stealth Ability Checks. | Sharpened Snare: Creatures have Disadvantage on Saving Throws when resisting your attacks and spells that inflict Restrained.
- How to get:
  - Moonrise Towers X: -174 Y: -179: Sold by Roah Moonglow on the main floor
  - Sold by Roah Moonglow on the main floor
- Notes:
  - Sharpened Snare only functions as described with Ensnaring Strike, Ensnaring Strands, and Garrotte.
- Bugs:
  - Exotic Material does not work if either the Medium Armour Master or Magic Initiate: Cleric feat is gained. The Magic Initiate: Cleric feat has an unlisted effect that increases the maximum AC bonus from Dexterity while wearing Medium Armour from +2 to +3.
  - Sharpened Snare does not affect Fly Trap and Entangle when trying to apply them for the first time, it only affects when the target tries to shake off their effects.
  - No other attacks or spells work with this passive, including Hamstring Shot, Evard's Black Tentacles, and Nature's Wrath.

### Shield +1
- Rarity: Rare | Slot: Shield | Act: Act Two
- Description: A Shield +1 is a rare Shield with an enchantment increasing its Armour Class bonus.
- Effect: AC +3 | Enchantment: + 1 | No special properties, beyond the Armour Class enchantment.
- How to get:
  - Flymm Cargo: Carried by Redhammer
  - Hhune Mausoleum: In a Sarcophagus
  - Moonrise Towers: Sold by Quartermaster Talli after Ketheric Thorm is defeated
  - Rivington General: On a shelf behind Exxvikyap
  - Rivington General: On a shelf on the second floor of Rivington General
  - Sold by Quartermaster Talli after Ketheric Thorm is defeated

### Slicing Shortsword
- Rarity: Rare | Slot: Weapon (Shortswords) | Act: Act Two
- Description: The Slicing Shortsword is a rare +1 shortsword that inflicts Bleeding when the wielder attacks with advantage.
- Effect: Damage: 1d6 + 1 (2~7) + Strength or Dexterity modifier Piercing | Deepflesh Slice: When the wielder attacks with Advantage, the attack inflicts Bleeding. | Flourish: Feint an attack to possibly throw your opponent Off Balance. (Recharge: Short rest.) | Piercing Strike: Stab an enemy and possibly inflict Gaping Wounds. (Recharge: Short rest.)
- How to get:
  - Moonrise Towers X: -164 Y: -167: Sold by Lann Tarv on the main floor
  - Sold by Lann Tarv on the main floor
- Notes:
  - The condition is only applied to attacks made with a weapon that has Deepflesh Slice.

### Spineshudder Amulet
- Rarity: Uncommon | Slot: Amulet | Act: Act Two
- Description: Spineshudder Amulet is an uncommon Amulet that allows the wearer to inflict Reverberation when dealing damage with ranged spell attacks.
- Effect: Crackling Resonance: When the wearer deals damage with a ranged Spell Attack, inflict 2 turns of Reverberation on the target(s).
- How to get:
  - Moonrise Towers X: -171 Y: -195: in the Mimic in Isobel's bedroom on the upper floor
  - in the Mimic in Isobel's bedroom on the upper floor
- Notes:
  - There are non-obvious ways to apply spell attacks. The blasts from Fungal Bamboozler, Merregon Potion, and Noxious Spore Grenade are examples which count as spell attacks.

### Thunderskin Cloak
- Rarity: Uncommon | Slot: Cloak | Act: Act Two
- Description: Thunderskin Cloak is an uncommon Cloak which has a chance to Daze creatures that are Reverberating when they damage the wearer.
- Effect: Dazing Echo: When a creature with Reverberation deals damage to the wearer, the creature needs to make a DC 13 Constitution Saving Throw or become Dazed.
- How to get:
  - Moonrise Towers X: -128 Y: -193: Sold by Araj Oblodra on the main floor
  - Lower City X: -92 Y: -78: Sold by Araj Oblodra in Crimson Draughts if not acquired from her in Act Two
  - Sold by Araj Oblodra on the main floor
- Notes:
  - Dazing Echo may be activated by intentionally triggering an opponent's Opportunity Attack.

### Titanstring Bow
- Rarity: Rare | Slot: Weapon (Longbows) | Act: Act Two
- Description: Titanstring Bow is a rare +1 Longbow that allows its wielder to add their Strength Modifier to damage dealt with this weapon.
- Effect: Damage: 1d8 + 1 (2~9) + Dexterity modifier Piercing | Titan Weapon: This weapon deals additional damage equal to your Strength Modifier. | Brace (Ranged): Spend 6 m (20 ft) of your movement. For the rest of your turn, roll ranged damage twice and use the highest result. (Recharge: Short rest.) | Hamstring Shot: Shoot an enemy in the thigh and possibly reduce their movement speed by 50%. (Recharge: Short rest.) | Pushing Attack (Ranged): Pushes your target back 4.5 m (15 ft). (Recharge: Short rest.)
- How to get:
  - Zhentarim Basement X: 295 Y: -250: Sold by Brem after completing the quest Find the Missing Shipment
  - Moonrise Towers X: -164 Y: -167: Sold by Lann Tarv on the main floor, only if Brem's special stock was not unlocked before by completing Find the Missing Shipment
  - Sold by Lann Tarv on the main floor, only if Brem's special stock was not unlocked before by completing ⁠Find the Missing Shipment
- Notes:
  - Titan Weapon adds a minimum of +1 to the damage roll, even if the attacker has a Strength of 11 or lower. The bonus damage is in addition to the normal Dexterity bonus for ranged weapons.
  - The bonus damage can be applied multiple times to a single ranged weapon attack. For example, special arrows with additional damage will receive the bonus to its additional damage, e.g. the additional Necrotic damage from Arrow of Ilmater will also receive bonus Necrotic damage equal to your Strength modifier. Another example is a rogue's Sneak Attack when used as a reaction. This is mostly changed in Honour mode, but the bonus damage can still apply to special arrows.
  - The bonus damage applies to most Arcane Shots. Notably, Arcane Shot: Seeking Arrow and Arcane Shot: Piercing Arrow do not apply the bonus damage due to the lack of attack rolls for these actions.
  - The knockback is a separate Weapon Action DC Strength Saving Throw which can fail even if the attack roll succeeds.
  - This weapon action can still be used even if the wielder is not proficient with Longbows.
- Bugs:
  - Titan Weapon has an extra description that states "The weapon only adds the modifier if it improves your chance to hit." but this has no actual function/relevance.
  - The bonus damage from Strength is not reflected on the character sheet or Ranged Attack tooltip.
  - Despite the game's tooltip mentioning Superiority Dice, this ability neither requires nor consumes them.

### Very Heavy Greataxe
- Rarity: Uncommon | Slot: Weapon (Greataxes) | Act: Act Two
- Description: Very Heavy Greataxe is an uncommon +1 Greataxe. It grants its wielder the Gargantuan Cleave weapon action, which can strike multiple targets but leaves the wielder Off-Balance for 1 turn.
- Effect: Damage: 1d12 + 1 (2~13) + Strength modifier Slashing | Lacerate: Slash at your target's vital points to make it Bleed. (Recharge: Short rest.) | Prepare: Spend 6 m (20 ft) of your movement to deal an additional Strength modifier PhysicalDRS damage (minimum 1) on each successful melee weapon attack for the rest of the turn. (Recharge: Short rest.) | Gargantuan Cleave: Swing your weapon with all your might. You can attack multiple targets, dealing bonus 1d6 SlashingDRS damage, but become Off Balanced. (Recharge: Short rest.)
- How to get:
  - Blighted Village X: 10 Y: 420: Carried by Fezzerk in front of the windmill in Act One
  - Moonrise Towers X: -152 Y: -191: Carried by Fezzerk on the main floor
  - Carried by Fezzerk on the main floor
- Notes:
  - True to its name, this weapon is about three times heavier than most Greataxes.
  - As with the regular Cleave, the maximum number of targets hit by this action is 3, targeting the closest ones first.
  - The 1d6 Slashing weapon action bonus damage is dealt whether or not the attack hits.
  - The Off Balance condition applied by this weapon is different from the regular Off Balance with the same name. It is applied to the attacker, not the targets of the attack.
- Bugs:
  - The tooltip shows this action applying full weapon damage when in fact it deals half the weapon damage.


## Moonrise Towers Prison

### Browbeaten Circlet
- Rarity: Uncommon | Slot: Helmet | Act: Act Two
- Description: Browbeaten Circlet is an uncommon piece of Headwear that grants the wearer a bonus to spell save DC while being threatened.
- Effect: Browbeaten: The wearer gains a +1 bonus to spell save DC while Threatened.
- How to get:
  - Moonrise Towers Prison X: 569 Y: -652: in the evidence chest on the top floor of the Warden's tower
  - in the evidence chest on the top floor of the Warden's tower

### Myrkulite Scourge
- Rarity: Uncommon | Slot: Weapon (Flails) | Act: Act Two
- Description: Myrkulite Scourge is an uncommon +1 Flail that deals an additional 1d6 Necrotic damage on a strike.
- Effect: Damage: 1d8 + 1 (2~9) + Strength modifier Bludgeoning | Extra damage: 1d6 (1~6) Necrotic | Tenacity: When you miss a melee attack, you deal Strength Modifier Bludgeoning damage (minimum of 1) anyway. | Concussive Smash: Hit an enemy with all your might to deal damage and possibly Daze them. (Recharge: Short rest.) | Weakening Strike: Target an enemy's hands with a non-lethal attack and possibly inflict Weak Grip. (Recharge: Short rest.)
- How to get:
  - Moonrise Towers X: -162 Y: -203: Carried by Radija on the first floor
  - Moonrise Towers Rooftop X: -146 Y: -213: Carried by Susdera on the rooftop
  - Mind Flayer Colony X: 727 Y: 41: Carried by Kressa Bonedaughter in the barracks
  - Moonrise Towers Prison X: 597 Y: -655: Carried by Sarabayle after confronting Ketheric Thorm
  - Moonrise Towers Prison X: 596 Y: -651: Carried by Willinx Jindlebee after confronting Ketheric Thorm
  - Carried by Willinx Jindlebee after confronting Ketheric Thorm
- Notes:
  - If a weapon action misses, using Tenacity does not trigger its effects.
  - As Tenacity deals weapon damage even if an attack misses, it can trigger many on-hit effects from equipment. For example, from the Gloves of Power, the Callous Glow Ring, weapon coatings, or any infusion from the Ring of Elemental Infusion.
- Bugs:
  - When dual-wielding a flail or morningstar with a non-Tenacity weapon using the Dual Wielder feat, Tenacity can be triggered by missing an attack with the non-Tenacity weapon, dealing Bludgeoning damage regardless of the weapon used. Some non-Tenacity weapons can trigger their on-hit effects via Tenacity as well, such as the Ritual Dagger and Loviatar's Scourge.
  - As Horde Breaker (Melee) rolls invisible, zero-damage weapon attacks against all enemies in the Horde Breaker area of effect, Tenacity can be prompted to trigger against them even if the first attack hits. It is therefore possible to score 2 hits in one attack: the full attack against the original Horde Breaker target and a Tenacity hit against another target.

### Myrkulite Scourge
- Rarity: Uncommon | Slot: Weapon (Flails) | Act: Act Two
- Description: Myrkulite Scourge is an uncommon +1 Flail that deals an additional 1d6 Necrotic damage on a strike.
- Effect: Damage: 1d8 + 1 (2~9) + Strength modifier Bludgeoning | Extra damage: 1d6 (1~6) Necrotic | Tenacity: When you miss a melee attack, you deal Strength Modifier Bludgeoning damage (minimum of 1) anyway. | Concussive Smash: Hit an enemy with all your might to deal damage and possibly Daze them. (Recharge: Short rest.) | Weakening Strike: Target an enemy's hands with a non-lethal attack and possibly inflict Weak Grip. (Recharge: Short rest.)
- How to get:
  - Moonrise Towers X: -162 Y: -203: Carried by Radija on the first floor
  - Moonrise Towers Rooftop X: -146 Y: -213: Carried by Susdera on the rooftop
  - Mind Flayer Colony X: 727 Y: 41: Carried by Kressa Bonedaughter in the barracks
  - Moonrise Towers Prison X: 597 Y: -655: Carried by Sarabayle after confronting Ketheric Thorm
  - Moonrise Towers Prison X: 596 Y: -651: Carried by Willinx Jindlebee after confronting Ketheric Thorm
  - Carried by Sarabayle after confronting Ketheric Thorm
- Notes:
  - If a weapon action misses, using Tenacity does not trigger its effects.
  - As Tenacity deals weapon damage even if an attack misses, it can trigger many on-hit effects from equipment. For example, from the Gloves of Power, the Callous Glow Ring, weapon coatings, or any infusion from the Ring of Elemental Infusion.
- Bugs:
  - When dual-wielding a flail or morningstar with a non-Tenacity weapon using the Dual Wielder feat, Tenacity can be triggered by missing an attack with the non-Tenacity weapon, dealing Bludgeoning damage regardless of the weapon used. Some non-Tenacity weapons can trigger their on-hit effects via Tenacity as well, such as the Ritual Dagger and Loviatar's Scourge.
  - As Horde Breaker (Melee) rolls invisible, zero-damage weapon attacks against all enemies in the Horde Breaker area of effect, Tenacity can be prompted to trigger against them even if the first attack hits. It is therefore possible to score 2 hits in one attack: the full attack against the original Horde Breaker target and a Tenacity hit against another target.

### Spellcrux Amulet
- Rarity: Very Rare | Slot: Amulet | Act: Act Two
- Description: Spellcrux Amulet is a very rare Amulet that allows the wearer to restore any one spell slot once per Long Rest.
- Effect: Spell Slot Restoration: Replenish an expended spell slot of any level as a Bonus Action once per Long Rest.
- How to get:
  - Moonrise Towers Prison X: 569 Y: -650: Worn by the Warden
  - Worn by the Warden
- Notes:
  - The amulet cannot create new spell slots, only restore used ones. If you do not have a used spell slot of the level you chose, the amulet has no effect.
  - The amulet can recover spell slots that the caster does not innately have from their class, such as ones gained from Create Spell Slot, or ones from gear, such as Shield of Devotion.
  - It is capable of recovering both Warlock spell slots and regular spell slots. If you have empty spell slots of both types for the chosen level, it restores one slot for each type.
  - Likewise, if the amulet is equipped by Gale and he has the Consumed Shadow Weave feature, selecting third level will restore both a normal third-level spell slot and the third-level "shadow spell slot" granted by this feature.
  - The spell slot is not lost when the amulet is removed, meaning you can put the amulet on, restore a slot, and switch back to another amulet of your choice. The recharge is still tied to the amulet, so this cannot be done with multiple characters at once.

### Wulbren's Hammer
- Rarity: Uncommon | Slot: Weapon (Melee weapon) | Act: Act Two
- Description: Wulbren's Hammer is an uncommon +1 Light Hammer that deals an extra 2d4 Force damage on each hit against constructs and world objects.
- Effect: Damage: 1d4 + 1 (2~5) + Strength modifier Bludgeoning | Light Hammers | Concussive Smash: Hit an enemy with all your might to deal damage and possibly Daze them. (Recharge: Short rest.) | 2d4 Force damage against items and world objects (unlisted).
- How to get:
  - Moonrise Towers Prison X: 575 Y: -647: On a table up the ladder in the Warden's room
  - On a table up the ladder in the Warden's room
- Notes:
  - This weapon can be given to Wulbren Bongle as part of Rescue Wulbren, in which case he recognizes it and rejoices at getting it back.


## Moonrise Towers Rooftop

### Myrkulite Scourge
- Rarity: Uncommon | Slot: Weapon (Flails) | Act: Act Two
- Description: Myrkulite Scourge is an uncommon +1 Flail that deals an additional 1d6 Necrotic damage on a strike.
- Effect: Damage: 1d8 + 1 (2~9) + Strength modifier Bludgeoning | Extra damage: 1d6 (1~6) Necrotic | Tenacity: When you miss a melee attack, you deal Strength Modifier Bludgeoning damage (minimum of 1) anyway. | Concussive Smash: Hit an enemy with all your might to deal damage and possibly Daze them. (Recharge: Short rest.) | Weakening Strike: Target an enemy's hands with a non-lethal attack and possibly inflict Weak Grip. (Recharge: Short rest.)
- How to get:
  - Moonrise Towers X: -162 Y: -203: Carried by Radija on the first floor
  - Moonrise Towers Rooftop X: -146 Y: -213: Carried by Susdera on the rooftop
  - Mind Flayer Colony X: 727 Y: 41: Carried by Kressa Bonedaughter in the barracks
  - Moonrise Towers Prison X: 597 Y: -655: Carried by Sarabayle after confronting Ketheric Thorm
  - Moonrise Towers Prison X: 596 Y: -651: Carried by Willinx Jindlebee after confronting Ketheric Thorm
  - Carried by Susdera on the rooftop
- Notes:
  - If a weapon action misses, using Tenacity does not trigger its effects.
  - As Tenacity deals weapon damage even if an attack misses, it can trigger many on-hit effects from equipment. For example, from the Gloves of Power, the Callous Glow Ring, weapon coatings, or any infusion from the Ring of Elemental Infusion.
- Bugs:
  - When dual-wielding a flail or morningstar with a non-Tenacity weapon using the Dual Wielder feat, Tenacity can be triggered by missing an attack with the non-Tenacity weapon, dealing Bludgeoning damage regardless of the weapon used. Some non-Tenacity weapons can trigger their on-hit effects via Tenacity as well, such as the Ritual Dagger and Loviatar's Scourge.
  - As Horde Breaker (Melee) rolls invisible, zero-damage weapon attacks against all enemies in the Horde Breaker area of effect, Tenacity can be prompted to trigger against them even if the first attack hits. It is therefore possible to score 2 hits in one attack: the full attack against the original Horde Breaker target and a Tenacity hit against another target.

### Ring of Exalted Marrow
- Rarity: Rare | Slot: Ring | Act: Act Two
- Description: Ring of Exalted Marrow is a rare Ring that grants the wearer the ability to cast Exhort the Risen and Ghoulish Touch.
- Effect: Exhort the Risen: Cast as a level 1 spell (Recharge: Long rest.) | Ghoulish Touch: Cast as a level 1 spell (Recharge: Long rest.)
- How to get:
  - Moonrise Towers Rooftop X: -153 Y: -170: In a heavy chest at the altar
  - In a heavy chest at the altar


## Reithwin Tollhouse

### Club +1
- Rarity: Uncommon | Slot: Weapon (Clubs) | Act: Act Two
- Description: Club +1 is an uncommon, lightly enchanted (+1) variant of the Clubs family of weapons. It is a simple melee weapon wielded in one hand. It is a light weapon that anyone can dual-wield without special training.
- Effect: Damage: 1d4 + 1 (2~5) + Strength modifier Bludgeoning | Concussive Smash: Hit an enemy with all your might to deal damage and possibly Daze them. (Recharge: Short rest.)
- How to get:
  - Reithwin Tollhouse X: -95 Y: -92: On a skeleton at top of the building
  - On a skeleton at top of the building

### Gloves of Battlemage's Power
- Rarity: Rare | Slot: Gloves | Act: Act Two
- Description: Gloves of Battlemage's Power is a rare pair of Gloves. They allow the wearer to gain Arcane Acuity whenever they hit a target with a spell or cantrip that uses a weapon.
- Effect: Battlemage's Power: When you hit a target with a spell or cantrip that uses a weapon, you gain Arcane Acuity. | Strength Saving Throws +1
- How to get:
  - Reithwin Tollhouse X: -84 Y: -88: in a locked opulent chest on the second floor in the room with two locked doors
  - in a locked opulent chest on the second floor in the room with two locked doors
- Notes:
  - DC 10 Sleight of Hand Check can be used to unlock the chest that contains these gloves.
  - These Gloves' functions were redesigned in Patch 8.
  - The spells that can trigger this effect are: Any smite spell (and also Divine Smite). Casting a smite spell and then reacting with Divine Smite will trigger Battlemage's Power twice.
  - Booming Blade
  - Ensnaring Strike (Melee) and Ensnaring Strike (Ranged)
  - Hail of Thorns
  - Any damage dealt while wielding a normal, non-permanent Flame Blade in the main hand. The damage can be from any source such as weapon attacks, spell damage (including each dart from Magic Missile), or even damage from status effects like Burning. Battlemage's Power does not trigger if the conjured weapon is in the off-hand, even if attacking with the conjured weapon.
  - Weapon attacks with Shadow Blade (weapon)
- Bugs:
  - The reader is advised that Battlemage's Power appears to have some of the most complex and unintuitive behaviour in the game, making it difficult to distinguish what is actually a bug. Any damage dealt while wielding a normal, non-permanent Flame Blade in the main hand triggers Battlemage's Power. The damage can be from any source such as weapon attacks, spell damage (including each dart from Magic Missile and each blast from Eldritch Blast), or even damage from status effects like Burning. Battlemage's Power does not trigger if the conjured weapons are in the off-hand, even if attacking with the conjured weapon. This only works with a normal, temporary Flame Blade summoned by the corresponding spell and not with a permanent Flame Blade acquired through hireling exploit. This effect also used to work while wielding a Shadow Blade in the main hand, but this was removed in a hotfix after Patch 8.
  - Battlemage's Power does not function with the Mephistopheles Tiefling version of Flame Blade, as this version has a different condition applied to it which is not listed in the Arcane AcuityGloves Condition() .khn script.
  - Throwing Healing Potions and Grenades triggers Battlemage's Power, even without hitting any target.
  - Reaction Smites provide acuity if and only if the triggering attack provided acuity. If the source attack does trigger Battlemage's Power, reaction smite triggers them a second time, for a total of +4 Acuity.
  - All of the following provide Acuity: Persistent AoE spell effects like Cloudkill and Wall of Fire
  - Every status in the game which deals damage attributed to the wearer triggers Battlemage's Power. For example, Burning and Electrocuted.
  - Fall damage caused by the wearer
  - Some miscellaneous effects like the Holy Lance Helm
  - Retaliation effects do not trigger Battlemage's Power. This includes on Hit effects such as Armour of Agathys and Fire Shield; on Damage effects such as Fleshmelter Cloak; and on Miss effects such as Shield of Scorching Reprisal.
  - Battlemage's Power is meant to have a Once PerAttack restriction, meaning they should only provide Acuity once per damaging event. However, the Once PerAttack limit gets reset every time the player character performs any effect which targets any in-game entity, whether that entity is an enemy, an ally, or the wearer themself. This includes regular attacks as well as self-target abilities like Dash and Rage.
  - This also includes effects the game considers an "attack" (due to underlying code) such as: using the Perform action (including in combat), speaking with the Sentient Amulet (including in combat), targeting someone with the ability check version of Bend Luck, and provoking an attack of opportunity (though if the wearer takes damage from it, they lose 2 Acuity).
  - Explosions also reset the gloves' once per attack limit. This includes the AOE "explosions" from Hamarhraft and Luminous Armour as well as grenades like Alchemist's Fire and Caustic Bulb.

### Ironvine Shield
- Rarity: Uncommon | Slot: Shield | Act: Act Two
- Description: Ironvine Shield is an uncommon Shield that damages the attacker if the wielder is using a weapon empowered with Shillelagh.
- Effect: AC +2 | Ironvine: While the wielder is holding a weapon empowered with Shillelagh, and when they are hit by a melee attack, the attacker takes Piercing Damage equal to the wielder's Wisdom modifier. | Enchantment:
- How to get:
  - Reithwin Tollhouse X: -127 Y: -95: In a chest
  - In a chest
- Notes:
  - Ironvine only activates if the wearer takes damage. For example when damage is reduced to 0 by Arcane Ward, no damage is done to the attacker.
- Bugs:
  - Ironvine activates on any attack, not just melee attacks.

### Twist of Fortune
- Rarity: Rare | Slot: Weapon (Morningstars) | Act: Act Two
- Description: Twist of Fortune is a rare +1 Morningstar with the unique weapon action, Blood Money. When the wielder rolls 2 or less with this weapon's damage die, they reroll and take the new result.
- Effect: Damage: 1d8 + 1 (2~9) + Strength modifier Piercing | Twist of Fortune: When you roll 2 or less with this weapon's damage die, reroll it and take the new result. | Tenacity: When you miss a melee attack, you deal Strength Modifier Bludgeoning damage (minimum of 1) anyway. | Heartstopper: Smash an enemy's chest in and possibly inflict Chest Trauma. (Recharge: Short rest.) | Concussive Smash: Hit an enemy with all your might to deal damage and possibly Daze them. (Recharge: Short rest.) | Blood Money: Strike out greedily, dealing an additional proficiency bonus Piercing damage per 300 gold that the target possesses. The gold will be consumed. (Recharge: Short rest.)
- How to get:
  - Reithwin Tollhouse X: -112 Y: -92: Carried by Gerringothe Thorm
  - Carried by Gerringothe Thorm
- Notes:
  - The Twist of Fortune passive affects all melee damage rolls while equipped, not just damage with Twist of Fortune itself.
  - This passive stacks with itself (via a second copy of the weapon using the Invoke Duplicity exploit) or by dual wielding with the Knife of the Undermountain King. The damage improvement of the second reroll is smaller than the first one.
  - If a weapon action misses, using Tenacity does not trigger its effects.
  - As Tenacity deals weapon damage even if an attack misses, it can trigger many on-hit effects from equipment. For example, from the Gloves of Power, the Callous Glow Ring, weapon coatings, or any infusion from the Ring of Elemental Infusion.
  - As of Patch 5, this ability consumes gold the target carries in increments of 300 as it is converted to proficiency bonus Piercing damage, so a target with 99,999 gold hit by a level 9 character will have around 99 gold left in their inventory after being dealt approximately [99,900/4]=1330 damage from a hit (before any applicable reductions).
  - Many bosses and tough enemies in the game can be assassinated with this action by "reverse-pickpocketing" large sums of gold into their inventory.
- Bugs:
  - When dual-wielding a flail or morningstar with a non-Tenacity weapon using the Dual Wielder feat, Tenacity can be triggered by missing an attack with the non-Tenacity weapon, dealing Bludgeoning damage regardless of the weapon used. Some non-Tenacity weapons can trigger their on-hit effects via Tenacity as well, such as the Ritual Dagger and Loviatar's Scourge.
  - As Horde Breaker (Melee) rolls invisible, zero-damage weapon attacks against all enemies in the Horde Breaker area of effect, Tenacity can be prompted to trigger against them even if the first attack hits. It is therefore possible to score 2 hits in one attack: the full attack against the original Horde Breaker target and a Tenacity hit against another target.


## Reithwin Town

### Assassin's Shortsword
- Rarity: Uncommon | Slot: Weapon (Shortswords) | Act: Act Two
- Description: Assassin's Shortsword is an uncommon +1 Shortsword that grants the wielder Advantage on Stealth checks.
- Effect: Damage: 1d6 + 1 (2~7) + Strength or Dexterity modifier Piercing | Flourish: Feint an attack to possibly throw your opponent Off Balance. (Recharge: Short rest.) | Piercing Strike: Stab an enemy and possibly inflict Gaping Wounds. (Recharge: Short rest.) | Advantage on Stealth Checks.
- How to get:
  - Reithwin Town X: -252 Y: 36: on one of a pair of skeletons along the cliffs west of the House of Healing
  - on one of a pair of skeletons along the cliffs west of the House of Healing
- Notes:
  - The tooltip for this sword also contains the text 'Shortsword of Stealth' (likely a placeholder name that was never removed).

### Fireheart
- Rarity: Uncommon | Slot: Amulet | Act: Act Two
- Description: Fireheart is an uncommon Amulet that grants the wearer 2 turns of Heat when they take Fire damage.
- Effect: Fervent Flames: Whenever you take Fire damage dealt by another creature, you gain 2 turns of Heat.
- How to get:
  - Reithwin Town X: -127 Y: -78: Inside a Heavy Chest
  - Inside a Heavy Chest
- Notes:
  - The party must break a vine or jump through a window from the outside to enter the hidden room containing this amulet. This room can also be accessed by breaking some old planks on the roof section.
  - Looting this item grants the Confiscated Works inspiration to party members with the Guild Artisan background.
  - Damage from Warding Bond will activate Fervant Flames for every damage source separately.
- Bugs:
  - The fire damage from the Heat condition applied by Fervent Flames will retrigger Fervent Flames, which will then add more turns of Heat.

### Hr'a'cknir Bracers
- Rarity: Very Rare | Slot: Gloves | Act: Act Two
- Description: Hr'a'cknir Bracers is a very rare pair of Gloves that allows the wearer to cast Mage Hand as a Bonus Action and cast Telekinesis once per Short Rest.
- Effect: Telekinesis: Cast as a level 5 spell (Recharge: Short rest.) | Quickened Mage Hand: You can cast Mage Hand as a Bonus Action. | Strength Saving Throws +1
- How to get:
  - Reithwin Town X: -249 Y: -33: Worn by Ch'r'ai Tska'an near the bridge leading to the To Baldur's Gate waypoint
  - Worn by Ch'r'ai Tska'an near the bridge leading to the To Baldur's Gate waypoint
- Notes:
  - Quickened Mage Hand does not grant the Mage Hand spell, but instead unlocks a spell variant - swapping the Action Point cost for a Bonus Action Point.

### Lightning Jabber
- Rarity: Uncommon | Slot: Weapon (Spears) | Act: Act Two
- Description: Lightning Jabber is an uncommon +1 Spear that deals extra Lightning damage when thrown, and also has a chance to Shock a target on hit.
- Effect: One-handed damage: 1d6 + 1 (2~7) + Strength modifier Piercing | Two-handed damage: 1d8 + 1 (2~9) + Strength modifier Piercing | Extra damage: 1d4 (1~4) Lightning | Shocking Sting: On a hit, possibly Shock your target. | Throwing: Lightning Damage: When launched at a target, deal an additional 1d4 Lightning damage. | Rush Attack: Charge forward and attack the first enemy in your way, possibly pushing them Off Balance. (Recharge: Short rest.)
- How to get:
  - Reithwin Town X: -148 Y: 115: Carried by the Cursed Kuo-Toa Chief in the Cursed Kuo-toa ambush North East of the Grand Mausoleum entrance
  - Carried by the Cursed Kuo-Toa Chief in the Cursed Kuo-toa ambush North East of the Grand Mausoleum entrance
- Notes:
  - The description of Throwing: Lightning Damage is somewhat misleading, as the spear does the same 1d4 Lightning damage when thrown as when used in a melee attack. However most thrown weapons do not apply their extra damage when thrown, which is what the passive enables.
  - When the Lightning Jabber is dipped into a dippable surface, it receives the coating but it also removes the dippable surface.
  - This 1d4 Lightning bonus damage is dealt when thrown even on miss.
- Bugs:
  - Despite being labelled as a Spear, the Root Template is erroneously tagged as a Javelin and as such does not work with the Polearm Master feat.
  - The in-game tooltip for Shocking Sting says it has chance to apply Shocked, but the condition actually applied is the similar but less potent Shocking Grasp.
  - There is a saving throw for the Shocking Grasp condition, but the combat log does not show it.

### Psionic Ward Armour
- Rarity: Rare | Slot: Medium Armour (Medium) | Act: Act Two
- Description: Psionic Ward Armour is a set of rare Medium Armour. It heals the wearer if they if they pass a Saving Throw against a spell, and gives them Resistance to Psychic damage if they are Githyanki.
- Effect: AC 15 | Psionic Ward: If the item detects that the wearer is gith, they have Resistance to Psychic damage. Whenever the wearer succeeds on a Saving Throw against a spell, they regain 1d4 Hit Points. | Disadvantage on Stealth checks.
- How to get:
  - Reithwin Town X: -249 Y: -33: Worn by Ch'r'ai Tska'an near the bridge leading to the To Baldur's Gate waypoint
  - Worn by Ch'r'ai Tska'an near the bridge leading to the To Baldur's Gate waypoint

### Watcher's Shield
- Rarity: Uncommon | Slot: Shield | Act: Act Two
- Description: Watcher's Shield is an uncommon Shield that gives the wielder Advantage on Perception Checks.
- Effect: AC +2 | Advantage on Perception Checks
- How to get:
  - Reithwin Town X: -250 Y: 36: On one of a pair of skeletons along the cliffs west of the House of Healing
  - On one of a pair of skeletons along the cliffs west of the House of Healing


## Ruined Battlefield

### Cruel Sting
- Rarity: Rare | Slot: Weapon (Longswords) | Act: Act Two
- Description: Cruel Sting is a rare +1 Longsword that deals extra Poison damage against Restrained targets if the wielder is a drow elf. It also grants the Ensnaring Strands spell.
- Effect: One-handed damage: 1d8 + 1 (2~9) + Strength modifier Slashing | Two-handed damage: 1d10 + 1 (2~11) + Strength modifier Slashing | Ensnaring Strands: Your attack conjures thick sticky webbing that possibly Enwebs your target(s). (Recharge: Short rest.) | Sting The Helpless: A Drow wielding this weapon deals an additional 1d4 Poison against Restrained targets. | Lacerate: Slash at your target's vital points to make it Bleed. (Recharge: Short rest.) | Pommel Strike: Make a non-lethal attack against an enemy and possibly Daze them. (Recharge: Short rest.) | Rush Attack: Charge forward and attack the first enemy in your way, possibly pushing them Off Balance. (Recharge: Short rest.)
- How to get:
  - Ruined Battlefield X: 0 Y: -15: Carried by Kar'niss
  - Carried by Kar'niss
- Notes:
  - Being disguised as a Drow when equipping a weapon with Sting The Helpless also activates the effect.
  - Sting The Helpless deals extra poison damage to a creature under any condition in the Restrained status group, which includes (but is not limited to): Black Tentacles, via Evard's Black Tentacles
  - Ensnared, via Ensnaring Strike and all its variations
  - Entangled, via Entangle or Umbral Tangle
  - Enwebbed, via Web or Ensnaring Strands
  - Hamstrung, via Hamstring Shot weapon action, available for longbows and shortbows
- Bugs:
  - When this sword is looted from Kar'niss, it retains Spindleweb Fanatic until Long Rest, granting additional 1d6 Psychic damage to weapon attacks. Spindleweb Fanatic can be retained indefinitely by dropping the weapon on the ground or stashing it in a container prior to each long rest.

### Dark Justiciar Mask
- Rarity: Uncommon | Slot: Helmet | Act: Act Two
- Description: Dark Justiciar Mask is an uncommon Helmet that grants the wearer a bonus to Intimidation checks.
- Effect: Intimidation +1
- How to get:
  - Abandoned Refuge X: -606 Y: 282: on a skeleton near the Ancient Forge Waypoint
  - Ruined Battlefield X: -35 Y: -88: next to a skeleton, presumably of Inquisitor Verzen Wranlock
  - next to a skeleton, presumably of Inquisitor Verzen Wranlock

### Family Ring
- Rarity: Uncommon | Slot: Ring | Act: Act Two
- Description: The Family Ring is an uncommon Ring that grants +2 to Death Saving Throws.
- Effect: Death Saving Throws +2
- How to get:
  - Ruined Battlefield X: 108 Y: 128: In a burrow, down the cliff from Ellie May's grave and the camp
  - In a burrow, down the cliff from Ellie May's grave and the camp
- Notes:
  - A DC 10 Perception Check reveals the burrow.
  - The nearby campsite was used by Ellie May's husband to mourn by her grave.
  - Ellie was buried with the ring, but some small creature has since dug it up and brought it to its burrow. A successful Perception check near the grave will reveal a set of "beast tracks" leading to the cliff.
  - The ring is mentioned in Unsent Letter. Ellie May's husband asked a robber to retrieve the ring for him, but they died before they could find it.

### Frost Prince
- Rarity: Uncommon | Slot: Amulet | Act: Act Two
- Description: Frost Prince is an uncommon Amulet which grants the wearer the ability to cast the Ice Knife spell.
- Effect: Ice Knife: Cast as a level 1 spell (Recharge: Long rest.)
- How to get:
  - Ruined Battlefield X: 80 Y: -96: In gilded chest in the southeast, near an ambush of Shadow-Cursed Needle Blights and Shadow-Cursed Vine Blights
  - In gilded chest in the southeast, near an ambush of Shadow-Cursed Needle Blights and Shadow-Cursed Vine Blights
- Notes:
  - The frost prince may be a reference to the Prince of Frost, a mighty archfey of the Vale of the Long Night in the Feywild.

### Gloomstrand Shield
- Rarity: Uncommon | Slot: Shield | Act: Act Two
- Description: Gloomstrand Shield is an uncommon Shield that adds +1 to Stealth
- Effect: AC +2 | Stealth +1
- How to get:
  - Ruined Battlefield X: -60 Y: -114: In a locked traveller's chest on a pier across the Reithwin Tollhouse, next to the half-ruined wooden bridge. The chest can be opened with the Key (Reithwin Tollhouse).
  - In a locked traveller's chest on a pier across the Reithwin Tollhouse, next to the half-ruined wooden bridge. The chest can be opened with the Key (Reithwin Tollhouse).

### Hammergrim Mist Amulet
- Rarity: Uncommon | Slot: Amulet | Act: Act Two
- Description: The Hammergrim Mist Amulet is an uncommon Amulet that grants the wearer the ability to cast the Fog Cloud spell.
- Effect: Fog Cloud: Cast as a level 1 spell (Recharge: Long rest.)
- How to get:
  - Ruined Battlefield X: -12 Y: -7: In a locked chest tucked away in ruined house in the Shadow-Cursed Lands, east of the tollhouse
  - In a locked chest tucked away in ruined house in the Shadow-Cursed Lands, east of the tollhouse
- Notes:
  - This version of Fog Cloud does not require concentration.

### Ironwood Club
- Rarity: Uncommon | Slot: Weapon (Clubs) | Act: Act Two
- Description: Ironwood Club is an uncommon +1 Club that deals extra Bludgeoning damage when Shillelagh is cast on it.
- Effect: Damage: 1d4 + 1 (2~5) + Strength modifier Bludgeoning | Concussive Smash: Hit an enemy with all your might to deal damage and possibly Daze them. (Recharge: Short rest.) | Backbreaker: Put extra force behind your strike to possibly knock your enemy Prone. (Recharge: Short rest.) | When Shillelagh is cast on this weapon, it gains Ironwood Harmony.
- How to get:
  - Ruined Battlefield X: 40 Y: 60: Carried by by the Shadow-Cursed Shambling Mound
  - Carried by by the Shadow-Cursed Shambling Mound
- Bugs:
  - Ironwood Harmony is not displayed on the weapon, and is only visible in the combat log.

### Luminous Gloves
- Rarity: Uncommon | Slot: Gloves | Act: Act Two
- Description: The Luminous Gloves are an uncommon pair of Gloves that causes the wearer's Radiant damage to afflict struck foes with the Radiating Orb condition.
- Effect: Radiating Orb Gloves: When the wearer deals Radiant damage, the target receives 2 turns of Radiating Orb. | Strength Saving Throws +1
- How to get:
  - Ruined Battlefield X: -52 Y: 11: in the potter's chest
  - in the potter's chest
- Notes:
  - In earlier versions, Radiating Orb Gloves applied 1 turn of Radiating Orb instead of 2. This may explain the current typo in the tooltip for this passive feature, which reads "the target receives 2 turn of Radiating Orb", rather than "the target receives 2 turns of Radiating Orb".
  - Radiating Orb Gloves does not work with Moonbeam.

### Moonlantern
- Rarity: Story Item | Slot: Weapon (Clubs) | Act: Act Two
- Description: The Moonlantern is a special utility item that sheds a magical Light in a large radius while equipped.
- Effect: One-handed damage: 1d4 (1~4) + Strength modifier Bludgeoning | Two-handed damage: 1d6 (1~6) + Strength modifier Bludgeoning
- How to get:
  - Ruined Battlefield X: 0 Y: -15: Carried by Kar'niss, either after the Harper ambush or at the top of Moonrise Towers
  - Last Light Inn X: -63 Y: 172: Given by Isobel if letting the Harpers take the Moonlantern
  - Moonrise Towers: In Balthazar's room in Moonrise Towers
  - Carried by Kar'niss, either after the Harper ambush or at the top of Moonrise Towers
- Notes:
  - The Moonlantern carried by Kar'niss contains a foul-mouthed pixie Dolly Dolly Dolly who wants out. If freed using Inspect Moonlantern, she grants the party a Pixie Blessing.
  - If Dolly is freed, her Moonlantern remains in the inventory of the character who freed her, but its inventory icon changes to a broken version and the lantern cannot be equipped anymore.
  - If Kar'niss arrives at Moonrise Towers with the lantern (whether he escorted the party or not), Dolly dies inside it.
  - If Kar'niss is killed at the ambush and the lantern is taken by the Harpers, the party can follow them back to Last Light Inn. There Isobel gives the party the same Moonlantern with Dolly Dolly Dolly alive inside; she can be freed and the Pixie Blessing may then still be obtained.
  - Switching to ranged weapons while having a Moonlantern equipped retains the Moonshield effect but removes the illumination, allowing darkness-requiring effects such as Covert Critical and Shadow Step to be safely used within the Shadow-Cursed Lands.
  - See also: Broken Moonlantern
  - Dead Pixie
  - Filigreed Feywild Bell
  - Shadow Lantern
- Bugs:
  - The Moonlantern containing Dolly Dolly Dolly still produces a stationary Moonshield Aura when dropped on the ground even after she has been freed from it.

### Penumbral Armour
- Rarity: Rare | Slot: Light Armour (Light) | Act: Act Two
- Description: Penumbral Armour is a rare Light Armour that enhances Stealth when the wearer is Obscured.
- Effect: AC 12 | Stealthier: While obscured, the wearer gains a +3 bonus to Stealth Checks. | File ARM_Drow Leather_A_Pants | File ARM_Drow Leather_A_Shoulderpads
- How to get:
  - Ruined Battlefield X: 33 Y: 145: In a locked opulent chest in the abandoned house by the river east of the Last Light Inn
  - In a locked opulent chest in the abandoned house by the river east of the Last Light Inn

### Raven Gloves
- Rarity: Rare | Slot: Gloves | Act: Act Two
- Description: Raven Gloves are rare Gloves that allow the wearer to summon a Raven.
- Effect: Summon Quothe the Raven: Summon a raven familiar that can Blind enemies with its beak. (Recharge: Short rest.)
- How to get:
  - Ruined Battlefield X: 126 Y: 106: Given by He Who Was as a reward for completing the quest Punish the Wicked
  - Given by He Who Was as a reward for completing the quest Punish the Wicked

### Ring of Self Immolation
- Rarity: Uncommon | Slot: Ring | Act: Act Two
- Description: The Ring of Self Immolation is an uncommon Ring that grants its wearer the ability to use the Self Immolation ability to gain the Heat condition.
- Effect: Self Immolation: Set yourself on fire to gain Heat. (Recharge: Short rest.)
- How to get:
  - Ruined Battlefield X: 29 Y: 63: In a locked wooden chest in the tower north of the Shadow-Cursed Shambling Mound ambush
  - In a locked wooden chest in the tower north of the Shadow-Cursed Shambling Mound ambush
- Notes:
  - If needed, the key to the chest is nearby on a skeleton, alongside a note.

### Ring of Twilight
- Rarity: Rare | Slot: Ring | Act: Act Two
- Description: The Ring of Twilight is a rare Ring that increases the wearer's Armour Class while obscured.
- Effect: Treader by Twilight: You gain a +1 bonus to Armour Class while obscured.
- How to get:
  - Ruined Battlefield X: -34 Y: -12: In a traveller's chest hidden behind some pots inside a ruined tower
  - In a traveller's chest hidden behind some pots inside a ruined tower

### Shadow-Cloaked Ring
- Rarity: Uncommon | Slot: Ring | Act: Act Two
- Description: The Shadow-Cloaked Ring is an uncommon Ring that causes the wearer's weapon and unarmed attacks to deal an additional 1d4 damage against Obscured or shadow creatures.
- Effect: Shadowthief: The wearer's weapon and unarmed attacks deal an additional 1d4 damage against Lightly or Heavily Obscured creatures, and creatures made of shadow.
- How to get:
  - Ruined Battlefield X: -49 Y: 36: Carried by Shadow Mastiff Alpha in a cursed camp north of the ruined pottery
  - Carried by Shadow Mastiff Alpha in a cursed camp north of the ruined pottery
- Notes:
  - The nearby everburning torches must be destroyed to make the Mastiff appear.
  - Though not mentioned in the description, Shadowthief also increases the damage of Throw attacks.
- Bugs:
  - On a Throw attack with a weapon with the Thrown property, Shadowthief activates for an additional time.

### Thermoarcanic Gloves
- Rarity: Uncommon | Slot: Gloves | Act: Act Two
- Description: Thermoarcanic Gloves are an uncommon pair of Gloves that grant the wearer 2 turns of Heat whenever they deal Fire damage.
- Effect: Arcane Ashes: Whenever you deal Fire damage, you gain 2 turns of Heat.
- How to get:
  - Ruined Battlefield X: 100 Y: -54: Worn by Kansif, either at the cultist camp or after the Harper ambush
  - Worn by Kansif, either at the cultist camp or after the Harper ambush
- Notes:
  - Arcane Ashes only triggers once per attack, but may be triggered multiple times by casting Scorching Ray which counts each ray as a separate attack.


## Shadowfell

### Circle of Bones
- Rarity: Rare | Slot: Helmet | Act: Act Two
- Description: Circle of Bones is a rare Circlet that grants all nearby allied undead Resistance to physical damage, and the wearer can cast Animate Dead once per Long Rest.
- Effect: Animate Dead: Cast as a level 3 spell (Recharge: Long rest.) | Undead Ward: Allied undead within 6 m (20 ft) are Resistant to Bludgeoning, Slashing, and Piercing damage.
- How to get:
  - Gauntlet of Shar X: -845 Y: -793: Carried by Balthazar, at his altar
  - Shadowfell X: -604 Y: -1431: Carried by Balthazar, if he is later confronted near the Nightsong
  - Mind Flayer Colony X: 715 Y: -49: Carried by Balthazar, if he is allowed to abduct the Nightsong
  - Carried by Balthazar, if he is later confronted near the Nightsong
- Notes:
  - The Undead Ward feature does not apply to Astarion but does apply to another vampire if one is in the party, even though they do not have the Undead tag.
- Bugs:
  - Summoning a zombie via this item's version of Animate Dead incorrectly summons a Newborn Zombie, which begins decaying, instead of the normal Zombie.
  - Though it is not stated in the tooltip, Undead Ward applies to summoned fiends, such as Shovel, Cambion (Planar Ally), and Conjured Imp.
  - Though Undead Ward states it has a radius of 6 m (20 ft), it actually has a radius of 9 m (30 ft).

### Dark Justiciar Boots
- Rarity: Rare | Slot: Boots | Act: Act Two
- Description: The Dark Justiciar Boots are a rare pair of Boots that grants the wearer better Dexterity Saving Throws and the ability to cast Shadow Teleportation once per Short Rest.
- Effect: Shadow Teleportation: Teleport to an unoccupied, obscured spot. (Recharge: Short rest.) | Dexterity Saving Throws +1
- How to get:
  - Shadowfell X: -604 Y: -1431: Rewarded to Shadowheart for killing the Nightsong
  - Rewarded to Shadowheart for killing the Nightsong

### Dark Justiciar Gauntlets (Rare)
- Rarity: Rare | Slot: Gloves | Act: Act Two
- Description: The Dark Justiciar Gauntlets are a rare pair of Gloves that cause weapon attacks to deal an additional 1d4 Necrotic damage. They also grant better Strength Saving Throws and allow the wearer to cast Beckoning Darkness once per turn.
- Effect: Beckoning Darkness: Curse a creature to be haunted by darkness. It takes 2d8 Necrotic damage if it enters or starts its turn in a Lightly or Heavily Obscured area. | Umbral Attack: Your weapon attacks deal an additional 1d4 Necrotic damage. | Strength Saving Throws +1
- How to get:
  - Shadowfell X: -604 Y: -1431: Rewarded to Shadowheart for killing the Nightsong
  - Rewarded to Shadowheart for killing the Nightsong
- Notes:
  - Umbral Attack also works on Throw attacks.

### Dark Justiciar Half-Plate (Very Rare)
- Rarity: Very Rare | Slot: Medium Armour (Medium) | Act: Act Two
- Description: Dark Justiciar Half-Plate is a very rare Medium Armour that grants Advantage on Stealth checks while Obscured in shadow. It also grants Advantage on Constitution Saving Throws, allows its wearer to cast Shield of Faith once per Long Rest, and reduces damage while Shield of Faith is active on its wearer.
- Effect: AC 17 | Shar's Aegis: Cast as a level 1 spell (Recharge: Long rest.) | Shar's Umbrae: While obscured, the wearer has Advantage on Stealth Checks. | Shar's Protection: While the wearer has Shield of Faith active, reduce all incoming damage by 2 and reflect damage received back at the attacker, who takes 1d4 Necrotic damage. | File ARM_Shadowheart_Dark_Justiciar_Pants_A | Advantage on Constitution Saving Throws.
- How to get:
  - Shadowfell X: -604 Y: -1431: Awarded to Shadowheart for killing the Nightsong
  - Awarded to Shadowheart for killing the Nightsong
- Bugs:
  - Shar's Umbrae applies its Advantage on Stealth checks without any obscurity level checks, even if in a Clear Area.
  - If a a wearer of this item with Sharran Retribution casts Warding Bond on an ally, when that ally takes damage, it may trigger an infinite Necrotic damage loop. This loop continues until either the ally or the caster dies; however, if both characters have enough hit points to survive the cycle for an extended period, the game usually freezes or crashes.
  - Even though Shar's Protection is not listed as a passive feature on Dark Justiciar Half-Plate (Rare), casting Shar's Aegis with that armour equipped still applies Sharran Retribution to the wearer. However, only the damage reduction effect is functional.

### Dark Justiciar Helm
- Rarity: Uncommon | Slot: Helmet | Act: Act Two
- Description: A Dark Justiciar Helm is an uncommon Helmet worn by Shar's Dark Justiciars that grants a bonus to Saving Throws while obscured by shadow.
- Effect: Swathed in Shadow: While obscured by shadow, the wearer gains +1 to Saving Throws when attacked. | Constitution Saving Throws +1
- How to get:
  - Abandoned Refuge X: -595 Y: 310: On the skeletal remains of Dark Justiciars, north east of the Underdark - Ancient Forge waypoint and south of the heavy splint mold
  - Shadowfell X: -544 Y: -1447: On the ground next to a skeleton in the Nightsong's Prison
  - Shadowfell X: -516 Y: -1397: On the ground next to another skeleton in the Nightsong's Prison
  - On the ground next to another skeleton in the Nightsong's Prison
- Bugs:
  - The Swathed in Shadow passive adds its saving throw bonus at all times, not just when attacked and in shadow.

### Dark Justiciar Helm
- Rarity: Uncommon | Slot: Helmet | Act: Act Two
- Description: A Dark Justiciar Helm is an uncommon Helmet worn by Shar's Dark Justiciars that grants a bonus to Saving Throws while obscured by shadow.
- Effect: Swathed in Shadow: While obscured by shadow, the wearer gains +1 to Saving Throws when attacked. | Constitution Saving Throws +1
- How to get:
  - Abandoned Refuge X: -595 Y: 310: On the skeletal remains of Dark Justiciars, north east of the Underdark - Ancient Forge waypoint and south of the heavy splint mold
  - Shadowfell X: -544 Y: -1447: On the ground next to a skeleton in the Nightsong's Prison
  - Shadowfell X: -516 Y: -1397: On the ground next to another skeleton in the Nightsong's Prison
  - On the ground next to a skeleton in the Nightsong's Prison
- Bugs:
  - The Swathed in Shadow passive adds its saving throw bonus at all times, not just when attacked and in shadow.

### Moonlight Glaive
- Rarity: Rare | Slot: Weapon (Glaives) | Act: Act Two
- Description: Moonlight Glaive is a rare +2 Glaive that deals additional Radiant damage, has a permanent Light effect, and grants its wielder the Moonlight Butterflies weapon action.
- Effect: Damage: 1d10 + 2 (3~12) + Strength modifier Slashing | Extra damage: 1d4 (1~4) Radiant | Moonlight Glaive: Glowing: This object shines with a glowing light in a radius of 6 m (20 ft). | Rush Attack: Charge forward and attack the first enemy in your way, possibly pushing them Off Balance. (Recharge: Short rest.) | Lacerate: Slash at your target's vital points to make it Bleed. (Recharge: Short rest.) | Brace (Melee): Spend 6 m (20 ft) of your movement. For the rest of your turn, roll melee damage twice and use the highest result. (Recharge: Short rest.) | Moonlight Butterflies: Strike a foe, conjuring an illusory swarm of moon-pale butterflies and gaining Advantage on attacks against the target. (Recharge: Short rest.)
- How to get:
  - Shadowfell X: -604 Y: -1431: Rewarded by the Nightsong for freeing her during the Find the Nightsong quest
  - Rewarded by the Nightsong for freeing her during the ⁠Find the Nightsong quest
- Notes:
  - The Moonlight Butterflies area affects every entity inside it, including allies and inanimate objects.
  - The 3 m / 10 ft range of the attack is just enough such that the attacker can remain outside of the Moonlight Butterflies area when attacking at maximum range. At any shorter range, the attacker will also be enveloped in the Moonlight Butterflies and suffer the penalties.

### Shar's Spear of Evening
- Rarity: Legendary | Slot: Weapon (Spears) | Act: Act Two
- Description: Shar's Spear of Evening is a legendary +3 Spear which allows the wielder to gain Shar's Blessing and immunity to blindness.
- Effect: One-handed damage: 1d6 + 3 (4~9) + Strength modifier Piercing | Two-handed damage: 1d8 + 3 (4~11) + Strength modifier Piercing | Shar's Darkness: Cast as a level 2 spell (Recharge: Per turn.) | Shar's Blessing: You gain Advantage on Saving Throws while Lightly or Heavily Obscured. This weapon deals an additional 1d6 damage to creatures that are Lightly or Heavily Obscured. | Blind Immunity: The wearer cannot be Blinded. | Rush Attack: Charge forward and attack the first enemy in your way, possibly pushing them Off Balance. (Recharge: Short rest.) | Maiming Strike: Possibly Maims your target. They can't move. (Recharge: Short rest.) | Edge of Darkness: Create a cloud of Darkness while you attack. [See Notes] (Recharge: Short rest.)
- How to get:
  - Shadowfell X: -604 Y: -1431: Rewarded to Shadowheart for killing the Nightsong
  - Rewarded to Shadowheart for killing the Nightsong
- Notes:
  - Steps for acquisition: Shadowheart must be present in the Shadowfell; she leaves the party upon returning from the Shadowfell if entering without her and becomes hostile if insisting on entering the Shadowfell without the Spear of Night in the inventory of the active party.
  - Aylin must die during The Chosen of Shar.
  - Shar rewards Shadowheart with this spear when leaving the Shadowfell.
  - Helldusk Helmet and Steelwatcher Helmet provide similar immunity to blindness; however, only the latter allows the wearer to see through magical darkness.
  - This action is actually an AoE attack. After striking the main target, an additional attack is made against every creature and object within the 3 m (10 ft) cloud radius around that target, including allies.
  - On-hit reactions such as Divine Smite can be applied to each creature hit by this action (at the cost of multiple spell slots, in the case of Divine Smite).
- Bugs:
  - Shar's Blessing adds its bonus damage to any weapon attacks against obscured creatures, not just attacks with this spear.
  - The advantage on saving throws only applies to Dexterity saving throws.
  - Despite not stating such in the description, Blind Immunity also allows the wearer to see through magical darkness.
  - The in-game tooltip for this action is inaccurate and missing key information about it being an AoE attack.
  - The tooltip claims there is an associated Constitution Saving Throw, but this is not true.


## Sharran Sanctuary

### Ritual Dagger of Shar
- Rarity: Uncommon | Slot: Weapon (Daggers) | Act: Act Two
- Description: Ritual Dagger of Shar is an uncommon +1 Dagger that deals an additional 1d4 Necrotic damage.
- Effect: Damage: 1d4 + 1 (2~5) + Strength or Dexterity modifier Piercing | Extra damage: 1d4 (1~4) Necrotic | Piercing Strike: Stab an enemy and possibly inflict Gaping Wounds. (Recharge: Short rest.)
- How to get:
  - Sharran Sanctuary X: 249 Y: -847: on an altar in a hidden room at the bottom of the sanctuary
  - on an altar in a hidden room at the bottom of the sanctuary
- Notes:
  - Picking up this dagger: Is disapproved of by Shadowheart (-1), unless she does this herself.
  - Grants the inspiration A Dark Edge for party members with the Criminal background and Ruthless Craftsmanship for party members with the Guild Artisan background.
  - Spawns three powerful sentinels that attack the party. The fight with sentinels is still triggered if the dagger is moved from the altar, which also prevents the party from picking up the dagger at all, even after defeating the sentinels – unless it is thrown so Scratch can fetch it.[verify]
  - As with most weapons, the extra elemental damage (in this case, 1d4 Necrotic) is not applied if Thrown.


## Waning Moon

### Punch-Drunk Bastard
- Rarity: Rare | Slot: Weapon (Melee weapon) | Act: Act Two
- Description: Punch-Drunk Bastard is a rare +1 Greatclub. While the wielder is drunk it grants them Advantage on weapon attacks and also creates a Thunder blast on each melee hit.
- Effect: Damage: 1d8 + 1 (2~9) + Strength modifier Bludgeoning | Greatclubs | Tippler's Rage: While you are Drunk, you have Advantage on Attack Rolls. You also create a blast with each melee hit landed, dealing 1d4 Thunder damage to all creatures and objects in a radius of 3 m (10 ft), excluding yourself. | Tenacity: When you miss a melee attack, you deal Strength Modifier Bludgeoning damage (minimum of 1) anyway. | Concussive Smash: Hit an enemy with all your might to deal damage and possibly Daze them. (Recharge: Short rest.) | Backbreaker: Put extra force behind your strike to possibly knock your enemy Prone. (Recharge: Short rest.) | Cleave: Swing your weapon in a large arc to attack up to 3 enemies at once. They each take half the damage your weapon usually deals. (Recharge: Short rest.)
- How to get:
  - The Waning Moon X: -259 Y: -92: in a chest in the back area to the west, next to a trapped cage door
  - in a chest in the back area to the west, next to a trapped cage door
- Notes:
  - When the in-game description of Tippler's Rage mentions being drunk, it is referring to the Drunk, Drunk (Drunken Master), and Alcohol conditions.
  - If a weapon action misses, using Tenacity does not trigger its effects.
  - As Tenacity deals weapon damage even if an attack misses, it can trigger many on-hit effects from equipment. For example, from the Gloves of Power, the Callous Glow Ring, weapon coatings, or any infusion from the Ring of Elemental Infusion.
- Bugs:
  - While 'drunk', Advantage from Tippler's Rage applies to any attack roll made by the wielder including throw, and spell attack rolls.
  - Although not specified with the in-game description, the Thunder damage from Tippler's Rage only triggers on melee weapon attacks.
  - Attacks which deal multiple instances of damage (e.g., the various Smite spells or Booming Blade) will also trigger multiple instances of Tippler's Rage.
  - As Horde Breaker (Melee) rolls invisible, zero-damage weapon attacks against all enemies in the Horde Breaker area of effect, Tenacity can be prompted to trigger against them even if the first attack hits. It is therefore possible to score 2 hits in one attack: the full attack against the original Horde Breaker target and a Tenacity hit against another target.

### Rat Bat
- Rarity: Rare | Slot: Weapon (Melee weapon) | Act: Act Two
- Description: The Rat Bat is a rare Greatclub that grants the wielder Advantage on their Attack Rolls against beasts.
- Effect: Damage: 1d8 + 1 (2~9) + Strength modifier Bludgeoning | Extra damage: 1d6 (1~6) Piercing | Greatclubs | Rat Catcher: Attack Rolls against beasts have Advantage. | Concussive Smash: Hit an enemy with all your might to deal damage and possibly Daze them. (Recharge: Short rest.)
- How to get:
  - The Waning Moon X: -224 Y: -78: Leaning against a wall, near Thisobald Thorm
  - Leaning against a wall, near Thisobald Thorm
- Notes:
  - Unlike other greatclubs, this weapon does not have the Tenacity feature.
  - This weapon is a possible reference to the American sitcom It's Always Sunny in Philadelphia, where in episode 10 of season 6, "Charlie's Surprise Party", one of the characters, Charlie, is gifted a bat covered with chains and nails, dubbed the "Rat Stick".
- Bugs:
  - It is not listed anywhere in-game, but the Rat Bat deals an extra 1d6 PiercingDRS damage (non-magical).


## Additional items in Act Two (not on the wiki's list page)

These items are obtainable in this act but are missing from bg3.wiki's per-act list; acts were assigned from item-page location info.

### Devotee's Mace
- Rarity: Legendary | Slot: Weapon (Maces) | Act: Act Two
- Description: The Devotee's Mace is a legendary +3 Mace that deals extra Radiant damage on hit, and can create a healing aura which heals the wielder and nearby allies.
- Effect: Damage: 1d6 + 3 (4~9) + Strength modifier Bludgeoning | Extra damage: 1d8 (1~8) Radiant | Healing Incense Aura: Emanating a soothing aura, You and nearby allies regain 1d4 Hit Points at the start of your turn (Recharge: Long rest.) | Concussive Smash: Hit an enemy with all your might to deal damage and possibly Daze them. (Recharge: Short rest.) | Backbreaker: Put extra force behind your strike to possibly knock your enemy Prone. (Recharge: Short rest.)
- How to get:
  - Obtained from casting the Arm Thy Servant variant of Divine Intervention. Once the party is level 10+, they can hire a cleric, have them cast Arm Thy Servant, then trade this weapon to another party member.

### Selûne's Spear of Night
- Rarity: Legendary | Slot: Weapon (Spears) | Act: Act Two
- Description: Selûne's Spear of Night is a legendary +3 Spear which allows the wielder to cast Moonbeam and grants Darkvision as well as Advantage on Wisdom Saving Throws and Perception Checks.
- Effect: One-handed damage: 1d6 + 3 (4~9) + Strength modifier Piercing | Two-handed damage: 1d8 + 3 (4~11) + Strength modifier Piercing | Moonbeam: Cast as a level 3 spell (Recharge: Long rest.) | Moonmote: Illuminate the area around you with wisps of moonish light that make movement difficult for enemies and bolster your allies' damage. (Recharge: Long rest.) | Selûne's Blessing: You gain Advantage on Wisdom Saving Throws and Perception Checks. | Darkvision: Can see in the dark up to 12 m (40 ft). | Rush Attack: Charge forward and attack the first enemy in your way, possibly pushing them Off Balance. (Recharge: Short rest.) | Maiming Strike: Possibly Maims your target. They can't move. (Recharge: Short rest.)
- How to get:
  - Given to Shadowheart by Aylin at the campsite
- Notes:
  - Steps for acquisition: Shadowheart must be present in the Shadowfell; she leaves the party upon returning from the Shadowfell if they enter without her and becomes hostile if the party insist on entering the Shadowfell without the Spear of Night in the inventory of the active party.
  - Aylin must survive The Chosen of Shar.
  - The player character must speak with Aylin in camp after Ketheric is defeated.
  - The actual distance of Darkvision often depends on the creature that has this feature. The values above are the default for playable races.
  - When a hiding creature enters the line of sight of a creature with darkvision, and is within the range of darkvision: Being Lightly Obscured counts as being under Clear Area instead.
  - Being Heavily Obscured counts as being Lightly Obscured instead.
  - The same applies to Superior Darkvision, just with a longer range.
  - Also granted by Sarevok's Horned Helmet and Sunwalker's Gift.
  - More information on Darkvision mechanics and its potential combat implications can be found here.
- Bugs:
  - Normally, a creature gains Advantage when making a ranged attack from within magical Darkness, assuming it can do so via a feature such as Devil's Sight that grants vision in magical darkness. However, if the target of the attack has Darkvision, and the attacker is within the target's Darkvision range, then the attacker gains no advantage. This is despite the fact that Darkvision does not grant vision in magical darkness.

### Arcane Absorption Dagger
- Rarity: Very Rare | Slot: Weapon (Daggers) | Act: Act Two
- Description: Arcane Absorption Dagger is a very rare, lightly enchanted (+1) variant of the Daggers family of weapons. It is a simple melee weapon wielded in one hand. As a finesse weapon, it can benefit from the wielder's Dexterity and not just their Strength. It is a light weapon that anyone can dual-wield without special training. Its design lends itself well to be thrown at enemies as a projectile.
- Effect: Damage: 1d4 + 1 (2~5) + Strength or Dexterity modifier Force | Arcane Absorption: When you kill an enemy with a melee attack, regain one of your spent 1st Level spell slots. | Piercing Strike: Stab an enemy and possibly inflict Gaping Wounds. (Recharge: Short rest.)
- Notes:
  - This item appears in an unused treasure table intended for Araj Oblodra in Moonrise Towers: MOO_Infernal Trader_Special Stock .

### Pale Widow Gloves
- Rarity: Very Rare | Slot: Gloves | Act: Act Two
- Description: Pale Widow Gloves are a pair of Gloves that grant the wearer the spells Ensnaring Strands, Pulling Web, and Web.
- Effect: Ensnaring Strands: Cast as a level 1 spell (Recharge: Short rest.) | Pulling Web: Cast as a cantrip (Recharge: Long rest.) | Web (+): Cast as a level 1 spell (Recharge: Long rest.)
- Notes:
  - This item appears in an unused treasure table intended for Araj Oblodra in Moonrise Towers: MOO_Infernal Trader_Special Stock .

### Shield of Returning
- Rarity: Very Rare | Slot: Shield | Act: Act Two
- Description: Shield of Returning is a very rare Shield. This shield Binds itself to the wielder, returning to their hand if thrown.
- Effect: AC +2 | Bound Weapon
- Notes:
  - This item may have been intended to be lootable from a skeleton in the gauntlet of Shar, as it appears in the unused treasure table SHA_Justiciar Skeleton_Combat_Treasure

### Boots of Apparent Death
- Rarity: Rare | Slot: Boots | Act: Act Two
- Description: Boots of Apparent Death are a rare set of Boots that grants the wearer the ability to cast Feign Death once per Short Rest.
- Effect: Feign Death (+): Cast as a level 3 spell (Recharge: Short rest.)
- How to get:
  - Reithwin Graveyard X: -165 Y: 45: In a sarcophagus behind the locked grated iron doors

### Braindrain Cape
- Rarity: Rare | Slot: Cloak | Act: Act Two
- Description: Braindrain Cape is a rare Cloak that exhausts attackers with mental fatigue.
- Effect: Mental Debilitation: When the wearer succeeds a Saving Throw against any foe's spells or actions, that foe gains Mental Fatigue.
- Notes:
  - This item appears in an unused treasure table intended for Araj Oblodra in Moonrise Towers: Infernal Trader_Special Stock .

### Icebite Robe
- Rarity: Rare | Slot: Clothing | Act: Act Two
- Description: Icebite Robe is a rare piece of Clothing. It grants the wearer Resistance to Cold damage and allows them to cast Armour of Agathys as a 3rd level spell once per Long Rest.
- Effect: Armour of Agathys: Cast as a level 3 spell (Recharge: Long rest.) | Resistance to Cold damage.
- How to get:
  - Reithwin Graveyard X: -158 Y: 73: Inside a sarcophagus north of the iron gate
- Notes:
  - If the robe is removed while its version of Armour of Agathys is active, the spell ends.

### Staff of Accretion
- Rarity: Rare | Slot: Weapon (Quarterstaves) | Act: Act Two
- Description: Staff of Accretion is a rare, lightly enchanted (+1) variant of the Quarterstaves family of weapons. It is a simple melee weapon that can be wielded in one hand, or with both hands for extra damage.
- Effect: One-handed damage: 1d6 + 1 (2~7) + Strength modifier Bludgeoning | Two-handed damage: 1d8 + 1 (2~9) + Strength modifier Bludgeoning | Accretion: The wearer gains Arcane Charge when they deal damage with close-quarter-range spells or close-quarter-range cantrips. | Topple: Swipe at a creature to knock it Prone. (Recharge: Short rest.)
- Notes:
  - This item appears in an unused treasure table intended for Araj Oblodra in Moonrise Towers: MOO_Infernal Trader_Special Stock .

### Strange Tendril Amulet
- Rarity: Rare | Slot: Amulet | Act: Act Two
- Description: Strange Tendril Amulet is a rare Amulet that allows the wearer to cast Evard's Black Tentacles once per Long Rest.
- Effect: Evard's Black Tentacles: Cast as a level 4 spell (Recharge: Long rest.)
- How to get:
  - House of Healing Morgue X: 85 Y: -1007: In a wooden chest inside a hidden room near the main entrance

### Bided Time
- Rarity: Uncommon | Slot: Clothing | Act: Act Two
- Description: Bided Time is uncommon Clothing that causes the wearer to gain Arcane Charge whenever they are hit by a melee attack.
- Effect: AC 10 | Time Thoroughly Bided: The wearer gains Arcane Charge whenever they are hit by a melee attack.
- How to get:
  - House of Healing Morgue X: 46 Y: -1005: In a locked heavy chest in the storage room south of the zombie crypt
- Notes:
  - The tooltip for Time Thoroughly Bided does not mention that the wearer receives 2 turns of Arcane Charge, and any following hits merely reset its duration back to 2 turns.
  - Blood Sacrifice or an attack made by a party member does not trigger Arcane Charge.

### Covert Cowl
- Rarity: Uncommon | Slot: Helmet | Act: Act Two
- Description: Covert Cowl is an uncommon Helmet that makes the wearer's critical hits more likely when they are obscured.
- Effect: Covert Critical: While obscured, the number you need to roll a Critical Hit while attacking is reduced by 1. This effect can stack. | Dexterity Saving Throws +1
- How to get:
  - Last Light Inn - Cellar X: 33 Y: -697: Carried by a Meenlock in the cellar of Last Light Inn

### Eversight Ring
- Rarity: Uncommon | Slot: Ring | Act: Act Two
- Description: Eversight Ring is an uncommon Ring that imparts immunity to Blindness upon the wearer.
- Effect: Blind Immunity: The wearer cannot be Blinded.
- How to get:
  - House of Healing Morgue X: 9 Y: -981: In a locked opulent chest in the corner of the morgue lab west of the zombie crypt
- Notes:
  - Helldusk Helmet and Steelwatcher Helmet provide similar immunity to blindness; however, only the latter allows the wearer to see through magical darkness.
- Bugs:
  - If a hireling is dismissed with the Eversight Ring equipped, then they are later resummoned, the ring will have turned into a nonmagical version of itself. This is due to the item template not including the ring's Stats entry.
  - Despite not stating such in the description, Blind Immunity also allows the wearer to see through magical darkness.

### Firzu's Ring of Trading
- Rarity: Uncommon | Slot: Ring | Act: Act Two
- Description: Firzu's Ring of Trading is an uncommon Ring that grants +1 to Deception.
- Effect: Deception +1
- How to get:
  - House of Healing Morgue X: 82 Y: -1006: On a charred corpse in the hidden room immediately south of the entrance hall

### Fleshmelter Cloak
- Rarity: Uncommon | Slot: Cloak | Act: Act Two
- Description: Fleshmelter Cloak is an uncommon Cloak. It deals acid damage to creatures that deal melee damage to the wearer.
- Effect: Caustic Reprisal: Whenever a creature deals melee damage to the wearer, that creature takes 1d4 Acid Damage.
- How to get:
  - House of Healing Morgue X: 29 Y: -930: In a gilded chest above the pit
- Notes:
  - Caustic Reprisal only activates if the wearer takes damage. For example when damage is reduced to 0 by Arcane Ward, Caustic Reprisal does not activate.
  - Acid damage from Caustic Reprisal does not activate the Ichorous Corrosion passive on the Ichorous Gloves.
  - Due to the way Baldur's Gate 3 handles its damage calculations, if the attacker lands a critical hit, "Caustic Reprisal" damage is doubled from 1d4 to 2d4.

### Githyanki Greatsword
- Rarity: Uncommon | Slot: Weapon (Greatswords) | Act: Act Two
- Description: The Githyanki Greatsword is an uncommon, lightly enchanted (+1) greatsword.
- Effect: Damage: 2d6 + 1 (3~13) + Strength modifier Slashing | Cleave: Swing your weapon in a large arc to attack up to 3 enemies at once. They each take half the damage your weapon usually deals. (Recharge: Short rest.) | Lacerate: Slash at your target's vital points to make it Bleed. (Recharge: Short rest.) | Pommel Strike: Make a non-lethal attack against an enemy and possibly Daze them. (Recharge: Short rest.)
- How to get:
  - Carried by multiple githyanki in the Crèche Y'llek
  - Carried by Shadow-Cursed Githyanki Warriors at Last Light Inn

### Ichorous Gloves
- Rarity: Uncommon | Slot: Gloves | Act: Act Two
- Description: Ichorous Gloves are an uncommon pair of Gloves that can inflict Noxious Fumes on targets that are dealt Acid damage.
- Effect: Ichorous Corrosion: When the wearer deals Acid damage, they also inflict Noxious Fumes on the target(s).
- How to get:
  - The Waning Moon X: -253 Y: -71: In a metal chest in the storeroom behind the bar
- Notes:
  - Ichorous Corrosion is not triggered by the Acid damage from Fleshmelter Cloak.
- Bugs:
  - Despite the description stating it affects targets, Ichorous Corrosion only applies once per turn and thus only affects one target. It also does not mention that it only has a chance to apply Noxious Fumes.

### Nightsong's Armour
- Rarity: Uncommon | Slot: Heavy Armour (Heavy) | Act: Act Two
- Description: Nightsong's Armour is an uncommon Heavy Armour that reduces Piercing damage. It is only worn by Aylin.
- Effect: AC 19 | Superior Plate: You take 1 less Piercing damage. | Enchantment: + 1 | Disadvantage on Stealth checks.
- How to get:
  - Worn by Aylin

### Protective Plate
- Rarity: Uncommon | Slot: Heavy Armour (Heavy) | Act: Act Two
- Description: Protective Plate is a set of Heavy Armour that grants Resistance to Necrotic damage.
- Effect: AC 18 | Grants Resistance to Necrotic damage | Does not give disadvantage on stealth checks.
- How to get:
  - House of Healing Morgue X: 44 Y: -942: Worn by the Hollow Armour at the bottom of the pit
- Notes:
  - This item shares a visual model with Plate Armour.
