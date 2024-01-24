import json

class Attribute:
    def __init__(self, name: str, value: int) -> None:
        self.name = name
        self.value = value

    def to_dict(self) -> dict:
        return {
            "name": self.name, 
            "value": self.value
        }
    
    def __repr__(self) -> str:
        return json.dumps(self.to_dict(), indent=2)
