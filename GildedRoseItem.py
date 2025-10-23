from abc import ABC, abstractmethod

from gilded_rose import Item

MAX_QUALITY = 50


class GildedRoseItem(ABC):
    def __init__(self, name: str, sell_in: int, quality: int):
        self.item = Item(name, sell_in, quality)

    @property
    def name(self) -> str:
        return self.item.name

    @property
    def sell_in(self) -> int:
        return self.item.sell_in

    @sell_in.setter
    def sell_in(self, value: int) -> None:
        self.item.sell_in = value

    @property
    def quality(self) -> int:
        return self.item.quality

    @quality.setter
    def quality(self, value: int) -> None:
        self.item.quality = value

    @abstractmethod
    def update_quality(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"{self.name}, {self.sell_in}, {self.quality}"

    @staticmethod
    def make_item(name: str, sell_in: int, quality: int) -> "GildedRoseItem":
        if name.startswith("Conjured"):
            return ConjuredItem(name, sell_in, quality)
        elif name == "Aged Brie":
            return AgedBrieItem(name, sell_in, quality)
        elif name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassItem(name, sell_in, quality)
        elif name == "Sulfuras, Hand of Ragnaros":
            return SulfurasItem(name, sell_in, quality)
        else:
            return RegularItem(name, sell_in, quality)


class SulfurasItem(GildedRoseItem):
    def update_quality(self) -> None:
        pass  # Sulfuras does not change in quality or sell_in


class RegularItem(GildedRoseItem):
    def update_quality(self) -> None:
        if self.quality > 0:
            self.quality = self.quality - 1

        self.sell_in = self.sell_in - 1

        if self.sell_in < 0 < self.quality:
            self.quality = self.quality - 1


# Conjured items degrade in quality twice as fast
class ConjuredItem(GildedRoseItem):
    def update_quality(self) -> None:
        self.sell_in = self.sell_in - 1

        if self.sell_in < 0 and self.quality >= 2:
            self.quality = self.quality - 2
        elif self.quality >= 1:
            self.quality = self.quality - 1


class AgedBrieItem(GildedRoseItem):
    def update_quality(self) -> None:
        self.sell_in = self.sell_in - 1

        if self.sell_in >= 0:
            self.quality = min(self.quality + 1, MAX_QUALITY)
        elif self.sell_in < 0:
            self.quality = min(self.quality + 2, MAX_QUALITY)


class BackstagePassItem(GildedRoseItem):
    def update_quality(self) -> None:
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in < 5:
            self.quality = min(self.quality + 3, MAX_QUALITY)
        elif self.sell_in < 10:
            self.quality = min(self.quality + 2, MAX_QUALITY)
        else:
            self.quality = min(self.quality + 1, MAX_QUALITY)
