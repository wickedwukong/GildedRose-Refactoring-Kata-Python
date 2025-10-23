from GildedRoseItem import GildedRoseItem


class GildedRose:
    def __init__(self, items: list[GildedRoseItem]) -> None:
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            item.update_quality()
