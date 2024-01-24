from shared.jsonable import Jsonable

class Attribute(Jsonable):
    """
    Attribute class for storing attribute name and value.

    Attributes:
        name (str): The name of the attribute.
        value (int): The value of the attribute.
    """
    
    def __init__(self, name: str, value: int) -> None:
        """
        Initialize an Attribute instance.

        Args:
            name (str): The name of the attribute.
            value (int): The value of the attribute.
        """
        self.name = name
        self.value = value

    def to_dict(self) -> dict:
        """
        Convert the Attribute instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Attribute instance.
        """
        return {
            "name": self.name, 
            "value": self.value
        }
