from abc import ABC, abstractmethod

from gilded_rose import Item


class GildedRoseItem(ABC):
    def __init__(self, name: str, sell_in: int, quality: int):
        self.item = Item(name, sell_in, quality)

    @abstractmethod
    def update_quality(self):
        pass

    def __repr__(self):
        return "%s, %s, %s" % (self.item.name, self.item.sell_in, self.item.quality)

    @staticmethod
    def make_item(name: str, sell_in: int, quality: int):
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
    def update_quality(self):
        pass  # Sulfuras does not change in quality or sell_in

class RegularItem(GildedRoseItem):
    def update_quality(self):
        if self.item.quality > 0:
            self.item.quality = self.item.quality - 1

        self.item.sell_in = self.item.sell_in - 1

        if self.item.sell_in < 0 < self.item.quality:
            self.item.quality = self.item.quality - 1

# Conjured items degrade in quality twice as fast
class ConjuredItem(GildedRoseItem):
    def update_quality(self):
        self.item.sell_in = self.item.sell_in - 1

        if self.item.sell_in < 0 and self.item.quality >= 2:
            self.item.quality = self.item.quality - 2
        elif self.item.quality >= 1:
            self.item.quality = self.item.quality - 1


class AgedBrieItem(GildedRoseItem):
    def update_quality(self):
        self.item.sell_in = self.item.sell_in - 1

        if self.item.sell_in >= 0 and self.item.quality < 50:
            self.item.quality = self.item.quality + 1
        elif self.item.sell_in < 0 and self.item.quality <= 48:
            self.item.quality = self.item.quality + 2


class BackstagePassItem(GildedRoseItem):
    def update_quality(self):
        self.item.sell_in = self.item.sell_in - 1
        if self.item.sell_in < 0:
            self.item.quality = 0
        elif self.item.sell_in < 5:
            self.item.quality = min(self.item.quality + 3, 50)
        elif self.item.sell_in < 10:
            self.item.quality = min(self.item.quality + 2, 50)
        else:
            self.item.quality = min(self.item.quality + 1, 50)
