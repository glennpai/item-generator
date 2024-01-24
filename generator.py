import random
from attribute import Attribute
from item import Item, ItemType
from part import Part, PartType

def generate_random_attribute(part_type: PartType) -> Attribute:
    name = random.choice(part_type.allowed_attributes)
    value = random.randint(1, 10)
    return Attribute(name, value)

def generate_random_part(part_type: PartType) -> Part:
    attributes = []
    for _ in range(random.randint(1, 3)):
        attributes.append(generate_random_attribute(part_type))
    return Part(attributes, part_type)

def generate_random_item(item_type: ItemType) -> Item:
    parts = []
    for part_type in item_type.allowed_parts:
        if random.choice([True, False]):
            parts.append(generate_random_part(part_type))

    if len(parts) == 0:
        return [generate_random_part(random.choice(item_type.allowed_parts))]

    return Item(parts, item_type)
