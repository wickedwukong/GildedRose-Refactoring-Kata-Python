# -*- coding: utf-8 -*-
import unittest

from GildedRoseItem import GildedRoseItem
from gilded_rose import GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [GildedRoseItem.make_item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

        
if __name__ == '__main__':
    unittest.main()
