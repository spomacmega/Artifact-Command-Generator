
main_stat_list = [
    'HP_FLAT_FLOWER',
    'ATK_FLAT_FEATHER',
    'EM_SANDS',
    'ER%_SANDS',
    'DEF%_SANDS',
    'HP%_SANDS',
    'ATK%_SANDS',
    'EM_GOBLET',
    'Physical_DMG_GOBLET',
    'Dendro_DMG_GOBLET',
    'Geo_DMG_GOBLET',
    'Anemo_DMG_GOBLET',
    'Hydro_DMG_GOBLET',
    'Cryo_DMG_GOBLET',
    'Electro_DMG_GOBLET',
    'Pyro_DMG_GOBLET',
    'DEF%_GOBLET',
    'HP%_GOBLET',
    'ATK%_GOBLET',
    'EM_CIRCLET',
    'Healing_CIRCLET',
    'CRIT_DMG_CIRCLET',
    'CRIT_RATE_CIRCLET',
    'DEF%_CIRCLET',
    'HP%_CIRCLET',
    'ATK%_CIRCLET'
]

stat_translation = {
    'HP_FLAT_FLOWER': 14001,
    'ATK_FLAT_FEATHER': 12001,
    'EM_SANDS': 10950,
    'ER%_SANDS': 10960,
    'DEF%_SANDS': 10970,
    'HP%_SANDS': 10980,
    'ATK%_SANDS': 10990,
    'EM_GOBLET': 50880,
    'Physical_DMG_GOBLET': 50890,
    'Dendro_DMG_GOBLET': 50900,
    'Geo_DMG_GOBLET': 50910,
    'Anemo_DMG_GOBLET': 50920,
    'Hydro_DMG_GOBLET': 50930,
    'Cryo_DMG_GOBLET': 50940,
    'Electro_DMG_GOBLET': 50950,
    'Pyro_DMG_GOBLET': 50960,
    'DEF%_GOBLET': 50970,
    'HP%_GOBLET': 50980,
    'ATK%_GOBLET': 50990,
    'EM_CIRCLET': 30930,
    'Healing_CIRCLET': 30940,
    'CRIT_DMG_CIRCLET': 30950,
    'CRIT_RATE_CIRCLET': 30960,
    'DEF%_CIRCLET': 30970,
    'HP%_CIRCLET': 30980,
    'ATK%_CIRCLET': 30990,
    'HP+209': 501021,   # Substat Section
    'HP+239': 501022,
    'HP+269': 501023,
    'HP+299': 501024,
    'DEF+16': 501081,
    'DEF+19': 501082,
    'DEF+21': 501083,
    'DEF+23': 501084,
    'ATK+14': 501051,
    'ATK+16': 501052,
    'ATK+18': 501053,
    'ATK+19': 501054,
    'Elemental Mastery+16': 501241,
    'Elemental Mastery+19': 501242,
    'Elemental Mastery+21': 501243,
    'Elemental Mastery+23': 501244,
    'HP Percentage+4.1%': 501031,
    'HP Percentage+4.7%': 501032,
    'HP Percentage+5.2%': 501033,
    'HP Percentage+5.8%': 501034,
    'DEF Percentage+5.1%': 501091,
    'DEF Percentage+5.8%': 501092,
    'DEF Percentage+6.6%': 501093,
    'DEF Percentage+7.3%': 501094,
    'ATK Percentage+4.1%': 501061,
    'ATK Percentage+4.7%': 501062,
    'ATK Percentage+5.2%': 501063,
    'ATK Percentage+5.8%': 501064,
    'Energy Recharge+4.5%': 501231,
    'Energy Recharge+5.2%': 501232,
    'Energy Recharge+5.8%': 501233,
    'Energy Recharge+6.5%': 501234,
    'CRIT Rate+2.7%': 501201,
    'CRIT Rate+3.1%': 501202,
    'CRIT Rate+3.5%': 501203,
    'CRIT Rate+3.9%': 501204,
    'CRIT DMG+5.4%': 501221,
    'CRIT DMG+6.2%': 501222,
    'CRIT DMG+7.0%': 501223,
    'CRIT DMG+7.8%': 501224
}

sub_stat_list = [
    'CRIT DMG+7.8%',
    'CRIT Rate+3.9%',
    'ATK Percentage+5.8%',
    'Energy Recharge+6.5%',
    'Elemental Mastery+23',
    'HP Percentage+5.8%',
    'DEF Percentage+7.3%',
    'HP+299',
    'DEF+23',
    'ATK+19',
]

sub_stat_list2 = [
    'CRIT DMG+7.8%',
    'CRIT DMG+7.0%',
    'CRIT DMG+6.2%',
    'CRIT DMG+5.4%',
    'CRIT Rate+3.9%',
    'CRIT Rate+3.5%',
    'CRIT Rate+3.1%',
    'CRIT Rate+2.7%',
    'ATK Percentage+5.8%',
    'ATK Percentage+5.2%',
    'ATK Percentage+4.7%',
    'ATK Percentage+4.1%',
    'Elemental Mastery+23',
    'Elemental Mastery+21',
    'Elemental Mastery+19',
    'Elemental Mastery+16',
    'Energy Recharge+6.5%',
    'Energy Recharge+5.8%',
    'Energy Recharge+5.2%',
    'Energy Recharge+4.5%',
    'HP Percentage+5.8%',
    'HP Percentage+5.2%',
    'HP Percentage+4.7%',
    'HP Percentage+4.1%',
    'DEF Percentage+7.3%',
    'DEF Percentage+6.6%',
    'DEF Percentage+5.8%',
    'DEF Percentage+5.1%',
    'ATK+19',
    'ATK+18',
    'ATK+16',
    'ATK+14',
    'HP+299',
    'HP+269',
    'HP+239',
    'HP+209',
    'DEF+23',
    'DEF+21',
    'DEF+19',
    'DEF+16'
]

# SPAWN ENTITY DATA SECTION

elite_enemies_list = [
    "Geovishap Hatchling",
    "Geovishap Type1",
    "Geovishap Type2",
    "Geovishap Type3",
    "Geovishap Type4",
    "Primordial Bathysmal Vishap Large",
    "Primordial Bathysmal Vishap Small",
    "Rimebiter Bathysmal Vishap Large",
    "Rimebiter Bathysmal Vishap Small",
    "Rimebiter Bathysmal Vishap Large Boss Type",
    "Bolteater Bathysmal Vishap Large",
    "Bolteater Bathysmal Vishap Small",
    "Bolteater Bathysmal Vishap Large Boss Type",
    "Fatui Electro Cicin Mage Type1",
    "Fatui Electro Cicin Mage Type2",
    "Fatui Cryo Cicin Mage Type1",
    "Fatui Cryo Cicin Mage Type2",
    "Fatui Pyro Agent Type1",
    "Fatui Pyro Agent Type2",
    "Mirror Maiden",
    "Wooden Shieldwall Mitachurl",
    "Blazing Axe Mitachurl Type1",
    "Blazing Axe Mitachurl Type2",
    "Rock Shieldwall Mitachurl",
    "Ice Shieldwall Mitachurl",
    "Crackling Axe Mitachurl Type1",
    "Crackling Axe Mitachurl Type2",
    "Frostarm Lawachurl",
    "Stonehide Lawachurl",
    "Thunderhelm Lawachurl",
    "Pyro Abyss Mage",
    "Cryo Abyss Mage",
    "Hydro Abyss Mage",
    "Electro Abyss Mage",
    "Abyss Herald: Wicked Torrents Type1",
    "Abyss Herald: Wicked Torrents Type2",
    "Abyss Lector: Violet Lightning Type1",
    "Abyss Lector: Violet Lightning Type2",
    "Abyss Lector: Fathomless Flames Type1",
    "Abyss Lector: Fathomless Flames Type2",
    "Shadowy Husk: Standard Bearer Type1",
    "Shadowy Husk: Standard Bearer Type2",
    "Shadowy Husk: Line Breaker Type1",
    "Shadowy Husk: Line Breaker Type2",
    "Shadowy Husk: Defender Type1",
    "Shadowy Husk: Defender Type2",
    "Black Serpent Knight Windcutter",
    "Rockfond Rifthound",
    "Thundercraven Rifthound",
    "Rockfond Rifthound Whelp",
    "Thundercraven Rifthound Whelp",
    "Ruin Guard",
    "Ruin Guard Very High HP",
    "Ruin Guard Very High HP2",
    "Ruin Hunter",
    "Ruin Grader Type1",
    "Ruin Grader Type2",
    "Ruin Serpent",
    "Ruin Cruiser Type1",
    "Ruin Cruiser Type2",
    "Ruin Cruiser Type3",
    "Ruin Destroyer Type1",
    "Ruin Destroyer Type2",
    "Ruin Destroyer Type3",
    "Ruin Defender Type1",
    "Ruin Defender Type2",
    "Ruin Defender Type3",
    "Ruin Scout Type1",
    "Ruin Scout Type2",
    "Ruin Scout Type3",
    "Eye of the Storm"
]

all_enemies_list_translation = {
    "Geovishap Hatchling": 26030101,
    "Geovishap Type1": 26040101,
    "Geovishap Type2": 26040102,
    "Geovishap Type3": 26040103,
    "Geovishap Type4": 26040104,
    "Primordial Bathysmal Vishap Large": 26050601,
    "Primordial Bathysmal Vishap Small": 26050901,
    "Rimebiter Bathysmal Vishap Large": 26050701,
    "Rimebiter Bathysmal Vishap Small": 26051001,
    "Rimebiter Bathysmal Vishap Large Boss Type": 26050702,
    "Bolteater Bathysmal Vishap Large": 26050801,
    "Bolteater Bathysmal Vishap Small": 26051101,
    "Bolteater Bathysmal Vishap Large Boss Type": 26050802,
    "Fatui Electro Cicin Mage Type1": 23030101,
    "Fatui Electro Cicin Mage Type2": 23030102,
    "Fatui Cryo Cicin Mage Type1": 23040101,
    "Fatui Cryo Cicin Mage Type2": 23040102,
    "Fatui Pyro Agent Type1": 23020101,
    "Fatui Pyro Agent Type2": 23020102,
    "Mirror Maiden": 23050101,
    "Wooden Shieldwall Mitachurl": 21020101,
    "Blazing Axe Mitachurl Type1": 21020201,
    "Blazing Axe Mitachurl Type2": 21020202,
    "Rock Shieldwall Mitachurl": 21020301,
    "Ice Shieldwall Mitachurl": 21020601,
    "Crackling Axe Mitachurl Type1": 21020701,
    "Crackling Axe Mitachurl Type2": 21020703,
    "Frostarm Lawachurl": 21020401,
    "Stonehide Lawachurl": 21020501,
    "Thunderhelm Lawachurl": 21020801,
    "Pyro Abyss Mage": 22010105,
    "Cryo Abyss Mage": 22010205,
    "Hydro Abyss Mage": 22010305,
    "Electro Abyss Mage": 22010402,
    "Abyss Herald: Wicked Torrents Type1": 22020101,
    "Abyss Herald: Wicked Torrents Type2": 22020102,
    "Abyss Lector: Violet Lightning Type1": 22030101,
    "Abyss Lector: Violet Lightning Type2": 22030102,
    "Abyss Lector: Fathomless Flames Type1": 22030201,
    "Abyss Lector: Fathomless Flames Type2": 22030202,
    "Shadowy Husk: Standard Bearer Type1": 22070101,
    "Shadowy Husk: Standard Bearer Type2": 22070102,
    "Shadowy Husk: Line Breaker Type1": 22070201,
    "Shadowy Husk: Line Breaker Type2": 22070202,
    "Shadowy Husk: Defender Type1": 22070301,
    "Shadowy Husk: Defender Type2": 22070302,
    "Black Serpent Knight Windcutter": 22080101,
    "Rockfond Rifthound": 22050101,
    "Thundercraven Rifthound": 22050201,
    "Rockfond Rifthound Whelp": 22040101,
    "Thundercraven Rifthound Whelp": 22040201,
    "Ruin Guard": 24010101,
    "Ruin Guard Very High HP": 24010108,
    "Ruin Guard Very High HP2": 24010109,
    "Ruin Hunter": 24010201,
    "Ruin Grader Type1": 24010301,
    "Ruin Grader Type2": 24010303,
    "Ruin Serpent": 24010401,
    "Ruin Cruiser Type1": 24020101,
    "Ruin Cruiser Type2": 24020102,
    "Ruin Cruiser Type3": 24020103,
    "Ruin Destroyer Type1": 24020201,
    "Ruin Destroyer Type2": 24020202,
    "Ruin Destroyer Type3": 24020203,
    "Ruin Defender Type1": 24020301,
    "Ruin Defender Type2": 24020302,
    "Ruin Defender Type3": 24020303,
    "Ruin Scout Type1": 24020401,
    "Ruin Scout Type2": 24020402,
    "Ruin Scout Type3": 24020403,
    "Eye of the Storm": 20020101
}


# Item Section

optionmenu1_list = [
    "5 Star Swords",
    "4 Star Swords",
    "3 Star Swords",
    "5 Star Claymores",
    "4 Star Claymores",
    "3 Star Claymores",
    "5 Star Polearms",
    "4 Star Polearms",
    "3 Star Polearms",
    "5 Star Catalysts",
    "4 Star Catalysts",
    "3 Star Catalysts",
    "5 Star Bows",
    "4 Star Bows",
    "3 Star Bows"
]


# ========== itemTranslation ==========

item_translation = {
    "Aquila Favonia": 11501,            # 5 STAR SWORDS
    "Freedom-Sworn": 11503,
    "Haran Geppaku Futsu": 11510,
    "Mistsplitter Reforged": 11509,
    "Primordial Jade Cutter": 11505,
    "Skyward Blade": 11502,
    "Summit Shaper": 11504,
    "Amenoma Kageuchi": 11414,            # 4 STAR SWORDS
    "Blackcliff Longsword": 11408,
    "Cinnabar Spindle": 11415,
    "Favonius Sword": 11401,
    "Festering Desire": 11413,
    "Iron Sting": 11407,
    "Lion's Roar": 11405,
    "Prototype Rancour": 11406,
    "Royal Longsword": 11404,
    "Sacrificial Sword": 11403,
    "Sword of Descension": 11412,
    "The Alley Flash": 11410,
    "The Black Sword": 11409,
    "The Flute": 11402,
    "Cool Steel": 11301,                  # 3 STAR SWORDS
    "Dark Iron Sword": 11304,
    "Fillet Blade": 11305,
    "Harbinger of Dawn": 11302,
    "Skyrider Sword": 11306,
    "Traveler's Handy Sword": 11303,
    "Redhorn Stonethresher": 12510,       # 5 STAR CLAYMORES
    "Skyward Pride": 12501,
    "Song of Broken Pines": 12503,
    "The Unforged": 12504,
    "Wolf's Gravestone": 12502,
    "Akuoumaru": 12416, # 4 STAR CLAYMORES
    "Blackcliff Slasher": 12408,
    "Favonius Greatsword": 12401,
    "Katsuragikiri Nagamasa": 12414,
    "Lithic Blade": 12410,
    "Luxurious Sea-Lord": 12412,
    "Prototype Archaic": 12406,
    "Rainslasher": 12405,
    "Royal Greatsword": 12404,
    "Sacrificial Greatsword": 12403,
    "Serpent Spine": 12409,
    "Snow-Tombed Starsilver": 12411,
    "The Bell": 12402,
    "Whiteblind": 12407,
    "Bloodtainted Greatsword": 12302,        # 3 STAR CLAYMORES
    "Debate Club": 12305,
    "Ferrous Shadow": 12301,
    "Skyrider Greatsword": 12306,
    "White Iron Greatsword": 12303,
    "Calamity Queller": 13507,           # 5 STAR POLEARMS
    "Engulfing Lightning": 13509,
    "Primordial Jade Winged-Spear": 13505,
    "Skyward Spine": 13502,
    "Staff of Homa": 13501,
    "Vortex Vanquisher": 13504,
    '"The Catch"': 13415,     # 4 STAR POLEARMS
    "Blackcliff Pole": 13404,
    "Crescent Pike": 13403,
    "Deathmatch": 13405,
    "Dragon's Bane": 13401,
    "Dragonspine Spear": 13409,
    "Favonius Lance": 13407,
    "Kitain Cross Spear": 13414,
    "Lithic Spear": 13406,
    "Prototype Starglitter": 13402,
    "Royal Spear": 13408,
    "Wavebreaker's Fin": 13416,
    "Black Tassel": 13303,      # 3 STAR POLEARMS
    "Halberd": 13302,
    "White Tassel": 13301,
    "Everlasting Moonglow": 14506,     # 5 STAR CATALYSTS
    "Kagura's Verity": 14509,
    "Lost Prayer to the Sacred Winds": 14502,
    "Memory of Dust": 14504,
    "Skyward Atlas": 14501,
    "Blackcliff Agate": 14408,   # 4 STAR CATALYSTS
    "Dodoco Tales": 14413,
    "Eye of Perception": 14409,
    "Favonius Codex": 14401,
    "Frostbearer": 14412,
    "Hakushin Ring": 14414,
    "Mappa Mare": 14407,
    "Oathsworn Eye": 14415,
    "Prototype Amber": 14406,
    "Royal Grimoire": 14404,
    "Sacrificial Fragments": 14403,
    "Solar Pearl": 14405,
    "The Widsith": 14402,
    "Wine and Song": 14410,
    "Emerald Orb": 14304,     # 3 STAR CATALYSTS
    "Magic Guide": 14301,
    "Otherworldly Story": 14303,
    "Thrilling Tales of Dragon Slayers": 14302,
    "Twin Nephrite": 14305,
    "Amos' Bow": 15502,         # 5 STAR BOWS
    "Elegy for the End": 15503,
    "Polar Star": 15507,
    "Skyward Harp": 15501,
    "Thundering Pulse": 15509,
    "Alley Hunter": 15410,          # 4 STAR BOWS
    "Blackcliff Warbow": 15408,
    "Compound Bow": 15407,
    "Favonius Warbow": 15401,
    "Hamayumi": 15414,
    "Mitternachts Waltz": 15412,
    "Mouun's Moon": 15416,
    "Predator": 15415,
    "Prototype Crescent": 15406,
    "Royal Bow": 15404,
    "Rust": 15405,
    "Sacrificial Bow": 15403,
    "The Stringless": 15402,
    "The Viridescent Hunt": 15409,
    "Windblume Ode": 15413,
    "Messenger": 15305,         # 3 STAR BOWS
    "Raven Bow": 15301,
    "Recurve Bow": 15303,
    "Sharpshooter's Oath": 15302,
    "Slingshot": 15304
}















# ========== SWORD ITEM LIST ==========

five_star_swords_list = [
    "Aquila Favonia",
    "Freedom-Sworn",
    "Haran Geppaku Futsu",
    "Mistsplitter Reforged",
    "Primordial Jade Cutter",
    "Skyward Blade",
    "Summit Shaper"
]

four_star_swords_list = [
    "Amenoma Kageuchi",
    "Blackcliff Longsword",
    "Cinnabar Spindle",
    "Favonius Sword",
    "Festering Desire",
    "Iron Sting",
    "Lion's Roar",
    "Prototype Rancour",
    "Royal Longsword",
    "Sacrificial Sword",
    "Sword of Descension",
    "The Alley Flash",
    "The Black Sword",
    "The Flute"
]

three_star_swords_list = [
    "Cool Steel",
    "Dark Iron Sword",
    "Fillet Blade",
    "Harbinger of Dawn",
    "Skyrider Sword",
    "Traveler's Handy Sword"
]

# ========== CLAYMORE ITEM LIST ==========

five_star_claymore_list = [
    "Redhorn Stonethresher",
    "Skyward Pride",
    "Song of Broken Pines",
    "The Unforged",
    "Wolf's Gravestone"
]

four_star_claymore_list = [
    "Akuoumaru",
    "Blackcliff Slasher",
    "Favonius Greatsword",
    "Katsuragikiri Nagamasa",
    "Lithic Blade",
    "Luxurious Sea-Lord",
    "Prototype Archaic",
    "Rainslasher",
    "Royal Greatsword",
    "Sacrificial Greatsword",
    "Serpent Spine",
    "Snow-Tombed Starsilver",
    "The Bell",
    "Whiteblind"
]

three_star_claymore_list = [
    "Bloodtainted Greatsword",
    "Debate Club",
    "Ferrous Shadow",
    "Skyrider Greatsword",
    "White Iron Greatsword"
]

# ========== POLEARM ITEM LIST ==========

five_star_polearm_list = [
    "Calamity Queller",
    "Engulfing Lightning",
    "Primordial Jade Winged-Spear",
    "Skyward Spine",
    "Staff of Homa",
    "Vortex Vanquisher",
]

four_star_polearm_list = [
    '"The Catch"',
    "Blackcliff Pole",
    "Crescent Pike",
    "Deathmatch",
    "Dragon's Bane",
    "Dragonspine Spear",
    "Favonius Lance",
    "Kitain Cross Spear",
    "Lithic Spear",
    "Prototype Starglitter",
    "Royal Spear",
    "Wavebreaker's Fin"
]

three_star_polearm_list = [
    "Black Tassel",
    "Halberd",
    "White Tassel"
]

# ========== CATALYST ITEM LIST ==========

five_star_catalyst_list = [
    "Everlasting Moonglow",
    "Kagura's Verity",
    "Lost Prayer to the Sacred Winds",
    "Memory of Dust",
    "Skyward Atlas"
]

four_star_catalyst_list = [
    "Blackcliff Agate",
    "Dodoco Tales",
    "Eye of Perception",
    "Favonius Codex",
    "Frostbearer",
    "Hakushin Ring",
    "Mappa Mare",
    "Oathsworn Eye",
    "Prototype Amber",
    "Royal Grimoire",
    "Sacrificial Fragments",
    "Solar Pearl",
    "The Widsith",
    "Wine and Song"
]

three_star_catalyst_list = [
    "Emerald Orb",
    "Magic Guide",
    "Otherworldly Story",
    "Thrilling Tales of Dragon Slayers",
    "Twin Nephrite",
]

# ========== BOW ITEM LIST ==========

five_star_bow_list = [
    "Amos' Bow",
    "Elegy for the End",
    "Polar Star",
    "Skyward Harp",
    "Thundering Pulse"
]

four_star_bow_list = [
    "Alley Hunter",
    "Blackcliff Warbow",
    "Compound Bow",
    "Favonius Warbow",
    "Hamayumi",
    "Mitternachts Waltz",
    "Mouun's Moon",
    "Predator",
    "Prototype Crescent",
    "Royal Bow",
    "Rust",
    "Sacrificial Bow",
    "The Stringless",
    "The Viridescent Hunt",
    "Windblume Ode"
]

three_star_bow_list = [
    "Messenger",
    "Raven Bow",
    "Recurve Bow",
    "Sharpshooter's Oath",
    "Slingshot"
]
