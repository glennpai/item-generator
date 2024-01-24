import json
from typing import List
from part import Part, PartType
from attribute import Attribute

class ItemType:
    def __init__(self, allowed_parts: List[PartType], base_attributes: List[Attribute] = []) -> None:
        self.allowed_parts = allowed_parts
        self.base_attributes = base_attributes

    def to_dict(self) -> dict:
        return {
            "allowed_parts": [part.to_dict() for part in self.allowed_parts]
        }

class Item:
    def __init__(self, parts: Part, item_type: ItemType) -> None:
        self.parts = parts
        self.item_type = item_type

    @property
    def total_attributes(self) -> dict:
        total = {}
        for attribute in self.item_type.base_attributes:
            if attribute.name in total:
                total[attribute.name] += attribute.value
            else:
                total[attribute.name] = attribute.value
        for part in self.parts:
            for attribute in part.attributes:
                if attribute.name in total:
                    total[attribute.name] += attribute.value
                else:
                    total[attribute.name] = attribute.value
        return total

    def to_dict(self) -> dict:
        return {
            "total_attributes": self.total_attributes,
            "parts": [part.to_dict() for part in self.parts]
        }

    def __repr__(self) -> str:
        return json.dumps(self.to_dict(), indent=2)
