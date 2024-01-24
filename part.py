from typing import List
from attribute import Attribute
from shared.jsonable import Jsonable

class PartType(Jsonable):
    """
    PartType class for storing part name and allowed attributes.

    Attributes:
        part_name (str): The name of the part.
        allowed_attributes (List[Attribute]): The list of allowed attributes.
    """

    def __init__(self, part_name: str, allowed_attributes: List[Attribute]) -> None:
        """
        Initialize a PartType instance.

        Args:
            part_name (str): The name of the part.
            allowed_attributes (List[Attribute]): The list of allowed attributes.
        """
        self.part_name = part_name
        self.allowed_attributes = allowed_attributes

    def to_dict(self) -> dict:
        """
        Convert the PartType instance to a dictionary.

        Returns:
            dict: A dictionary representation of the PartType instance.
        """
        return {
            "part_name": self.part_name,
            "allowed_attributes": self.allowed_attributes
        }

class Part(Jsonable):
    """
    Part class for storing attributes and part type.

    Attributes:
        attributes (List[Attribute]): The list of attributes.
        part_type (PartType): The type of the part.
    """

    def __init__(self, attributes: List[Attribute], part_type: PartType) -> None:
        """
        Initialize a Part instance.

        Args:
            attributes (List[Attribute]): The list of attributes.
            part_type (PartType): The type of the part.
        """
        self.attributes = attributes
        self.part_type = part_type

    def to_dict(self) -> dict:
        """
        Convert the Part instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Part instance.
        """
        return {
            "part_name": self.part_type.part_name,
            "attributes": [attribute.to_dict() for attribute in self.attributes]
        }
