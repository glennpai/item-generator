import json
from typing import List
from attribute import Attribute

class PartType:
    def __init__(self, part_name: str, allowed_attributes: List[Attribute]) -> None:
        self.part_name = part_name
        self.allowed_attributes = allowed_attributes

    def to_dict(self) -> dict:
        return {
            "part_name": self.part_name,
            "allowed_attributes": self.allowed_attributes
        }

class Part:
    def __init__(self, attributes: List[Attribute], part_type: PartType) -> None:
        self.attributes = attributes
        self.part_type = part_type

    def to_dict(self) -> dict:
        return {
            "part_name": self.part_type.part_name,
            "attributes": [attribute.to_dict() for attribute in self.attributes]
        }

    def __repr__(self) -> str:
        return json.dumps(self.to_dict(), indent=2)
