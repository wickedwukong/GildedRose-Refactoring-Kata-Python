import unittest

from gilded_rose import GildedRose
from gilded_rose_item import GildedRoseItem


class GildedRoseTest(unittest.TestCase):
    def test_foo(self) -> None:
        items = [GildedRoseItem.make_item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)


if __name__ == "__main__":
    unittest.main()
