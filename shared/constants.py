from item import ItemType
from part import PartType
from attribute import Attribute

SWORD_ATTRIBUTES = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma", "luck"]
SWORD_PART_LIST = ["blade", "cross-guard", "hilt", "pommel"]
SWORD_PARTS = [PartType(part_name, SWORD_ATTRIBUTES) for part_name in SWORD_PART_LIST]
SWORD = ItemType(SWORD_PARTS, [Attribute("strength", 50)])

SNIPER_RIFLE_ATTRIBUTES = ["damage", "accuracy", "range", "rate_of_fire", "magazine_size"]
SNIPER_RIFLE_PART_LIST = ["barrel", "scope", "stock", "magazine", "trigger", "bolt"]
SNIPER_RIFLE_PARTS = [PartType(part_name, SNIPER_RIFLE_ATTRIBUTES) for part_name in SNIPER_RIFLE_PART_LIST]
SNIPER_RIFLE = ItemType(SNIPER_RIFLE_PARTS, [Attribute("damage", 60), Attribute("accuracy", 75), Attribute("range", 75), Attribute("rate_of_fire", 25), Attribute("magazine_size", 5)])
