class Item:
    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name: str = name
        self.sell_in: int = sell_in
        self.quality: int = quality

    def __repr__(self) -> str:
        return f"{self.name}, {self.sell_in}, {self.quality}"
