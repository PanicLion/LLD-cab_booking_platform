import uuid


class Rider:
    def __init__(self, name: str) -> None:
        self.id = uuid.uuid4()
        self.name = name


    def __str__(self) -> str:
        return f"Rider(id={str(self.id)}, name={self.name})"
    

    def get_id(self) -> str:
        return str(self.id)
    