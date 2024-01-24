from typing import List
from part import Part, PartType
from attribute import Attribute
from shared.jsonable import Jsonable

class ItemType(Jsonable):
    """
    ItemType class for storing allowed parts and base attributes.

    Attributes:
        allowed_parts (List[PartType]): The list of allowed parts.
        base_attributes (List[Attribute]): The list of base attributes.
    """

    def __init__(self, allowed_parts: List[PartType], base_attributes: List[Attribute] = []) -> None:
        """
        Initialize an ItemType instance.

        Args:
            allowed_parts (List[PartType]): The list of allowed parts.
            base_attributes (List[Attribute]): The list of base attributes.
        """
        self.allowed_parts = allowed_parts
        self.base_attributes = base_attributes

    def to_dict(self) -> dict:
        """
        Convert the ItemType instance to a dictionary.

        Returns:
            dict: A dictionary representation of the ItemType instance.
        """
        return {
            "allowed_parts": [part.to_dict() for part in self.allowed_parts]
        }

class Item(Jsonable):
    """
    Item class for storing parts and item type.

    Attributes:
        parts (Part): The parts of the item.
        item_type (ItemType): The type of the item.
    """

    def __init__(self, parts: Part, item_type: ItemType) -> None:
        """
        Initialize an Item instance.

        Args:
            parts (Part): The parts of the item.
            item_type (ItemType): The type of the item.
        """
        self.parts = parts
        self.item_type = item_type

    @property
    def total_attributes(self) -> dict:
        """
        Calculate the total attributes of the item.

        Returns:
            dict: A dictionary of attribute names and their total values.
        """
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
        """
        Convert the Item instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Item instance.
        """
        return {
            "total_attributes": self.total_attributes,
            "parts": [part.to_dict() for part in self.parts]
        }
