# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def runInstance(self, items):
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        return items

    def verify(self, items, expected_items):
        for index, expected_item in enumerate(expected_items):
            self.assertEqual(expected_item.__dict__, items[index].__dict__)

    def test_NormalItem(self):
        items = [
            Item("Elixir of the Mongoose", 0, -5),
            Item("Elixir of the Mongoose", 0, 1),
            Item("Elixir of the Mongoose", 0, 3),
            Item("Elixir of the Mongoose", 1, -1),
            Item("Elixir of the Mongoose", 1, 0),
            Item("Elixir of the Mongoose", 1, 1),
            Item("+5 Dexterity Vest", 0, -5),
            Item("+5 Dexterity Vest", 0, 1),
            Item("+5 Dexterity Vest", 0, 3),
            Item("+5 Dexterity Vest", 1, -1),
            Item("+5 Dexterity Vest", 1, 0),
            Item("+5 Dexterity Vest", 1, 1),
        ]

        expected_items = [
            Item("Elixir of the Mongoose", -1, -5),
            Item("Elixir of the Mongoose", -1, 0),
            Item("Elixir of the Mongoose", -1, 1),
            Item("Elixir of the Mongoose", 0, -1),
            Item("Elixir of the Mongoose", 0, 0),
            Item("Elixir of the Mongoose", 0, 0),
            Item("+5 Dexterity Vest", -1, -5),
            Item("+5 Dexterity Vest", -1, 0),
            Item("+5 Dexterity Vest", -1, 1),
            Item("+5 Dexterity Vest", 0, -1),
            Item("+5 Dexterity Vest", 0, 0),
            Item("+5 Dexterity Vest", 0, 0),
        ]

        self.verify(self.runInstance(items), expected_items)

    def test_AgedBrie(self):
        items = [
            Item("Aged Brie", -1, 20),
            Item("Aged Brie", 0, 20),
            Item("Aged Brie", 0, 49),
            Item("Aged Brie", 1, 20),
            Item("Aged Brie", 1, -49),
            Item("Aged Brie", 10, 50)
        ]

        expected_items = [
            Item("Aged Brie", -2, 22),
            Item("Aged Brie", -1, 22),
            Item("Aged Brie", -1, 50),
            Item("Aged Brie", 0, 21),
            Item("Aged Brie", 0, -48),
            Item("Aged Brie", 9, 50)
        ]

        self.verify(self.runInstance(items), expected_items)

    def test_BackstagePass(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 0, -20),
            Item("Backstage passes to a TAFKAL80ETC concert", 0, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", 1, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)
        ]

        expected_items = [
            Item("Backstage passes to a TAFKAL80ETC concert", -1, 0),
            Item("Backstage passes to a TAFKAL80ETC concert", -1, 0),
            Item("Backstage passes to a TAFKAL80ETC concert", 0, 23),
            Item("Backstage passes to a TAFKAL80ETC concert", 4, 23),
            Item("Backstage passes to a TAFKAL80ETC concert", 9, 22),
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 21)
        ]

        self.verify(self.runInstance(items), expected_items)

    def test_Sulfuras(self):
        # Sulfuras's expected items and items always is the same
        items = [
            Item("Sulfuras, Hand of Ragnaros", -1, 20),
            Item("Sulfuras, Hand of Ragnaros", 0, 20),
            Item("Sulfuras, Hand of Ragnaros", 5, -20),
            Item("Sulfuras, Hand of Ragnaros", 10, 0),
            Item("Sulfuras, Hand of Ragnaros", 11, 80)
        ]

        self.verify(self.runInstance(items), items)

if __name__ == '__main__':
    unittest.main()
