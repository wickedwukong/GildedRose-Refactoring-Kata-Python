from gilded_rose import Item


class MyItem(Item):
    def update_quality(self):
        pass

    @staticmethod
    def make_item(name: str, sell_in: int, quality: int):
        if name.startswith("Conjured"):
            return ConjuredItem(name, sell_in, quality)
        elif name == "Aged Brie":
            return AgedBrieItem(name, sell_in, quality)
        elif name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassItem(name, sell_in, quality)
        else:
            return RegularItem(name, sell_in, quality)


class RegularItem(MyItem):
    def update_quality(self):
        if self.quality > 0:
            if self.name != "Sulfuras, Hand of Ragnaros":
                self.quality = self.quality - 1

        if self.name != "Sulfuras, Hand of Ragnaros":
            self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            if self.quality > 0:
                if self.name != "Sulfuras, Hand of Ragnaros":
                    self.quality = self.quality - 1

# Conjured items degrade in quality twice as fast
class ConjuredItem(MyItem):
    def update_quality(self):
        self.sell_in = self.sell_in - 1

        if self.sell_in < 0 and self.quality >= 2:
            self.quality = self.quality - 2
        elif self.quality >= 1:
            self.quality = self.quality - 1


class AgedBrieItem(MyItem):
    def update_quality(self):
        self.sell_in = self.sell_in - 1

        if self.sell_in >= 0 and self.quality < 50:
            self.quality = self.quality + 1
        elif self.sell_in < 0 and self.quality <= 48:
            self.quality = self.quality + 2


class BackstagePassItem(MyItem):
    def update_quality(self):
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in < 5:
            self.quality = min(self.quality + 3, 50)
        elif self.sell_in < 10:
            self.quality = min(self.quality + 2, 50)
        else:
            self.quality = min(self.quality + 1, 50)
