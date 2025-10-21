from gilded_rose import Item


class MyItem(Item):
    def update_quality(self):
        if self.name != "Aged Brie" and self.name != "Backstage passes to a TAFKAL80ETC concert":
            if self.quality > 0:
                if self.name != "Sulfuras, Hand of Ragnaros":
                    self.quality = self.quality - 1
        else:
            if self.quality < 50:
                self.quality = self.quality + 1
                if self.name == "Backstage passes to a TAFKAL80ETC concert":
                    if self.sell_in < 11:
                        if self.quality < 50:
                            self.quality = self.quality + 1
                    if self.sell_in < 6:
                        if self.quality < 50:
                            self.quality = self.quality + 1
        if self.name != "Sulfuras, Hand of Ragnaros":
            self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            if self.name != "Aged Brie":
                if self.name != "Backstage passes to a TAFKAL80ETC concert":
                    if self.quality > 0:
                        if self.name != "Sulfuras, Hand of Ragnaros":
                            self.quality = self.quality - 1
                else:
                    self.quality = self.quality - self.quality
            else:
                if self.quality < 50:
                    self.quality = self.quality + 1

    @staticmethod
    def make_item(name: str, sell_in: int, quality: int):
        if name.startswith("Conjured"):
            return ConjuredItem(name, sell_in, quality)
        else:
            return MyItem(name, sell_in, quality)

# Conjured items degrade in quality twice as fast
class ConjuredItem(MyItem):
   def update_quality(self):
       self.sell_in = self.sell_in - 1

       if self.sell_in < 0 and self.quality >= 2:
           self.quality = self.quality - 2
       elif self.quality >= 1:
           self.quality = self.quality - 1

