import json
from abc import ABC, abstractmethod

class Jsonable(ABC):
    """
    Jsonable abstract base class for providing a common __repr__ method and an abstract to_dict method.
    """

    @abstractmethod
    def to_dict(self) -> dict:
        """
        Convert the AbstractAttribute instance to a dictionary.

        Returns:
            dict: A dictionary representation of the AbstractAttribute instance.
        """
        pass

    def __repr__(self) -> str:
        """
        Generate a string representation of the AbstractAttribute instance in JSON format.

        Returns:
            str: A JSON string representation of the AbstractAttribute instance.
        """
        return json.dumps(self.to_dict(), indent=2)
