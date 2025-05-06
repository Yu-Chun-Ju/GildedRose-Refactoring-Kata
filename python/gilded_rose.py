# -*- coding: utf-8 -*-

class Constant:
    EXPIRE_DAY = 0
    QUALITY_MAX = 50
    QUALITY_MIN = 0

class NormalItem:
    sellin_rate_per_day = -1
    quality_rate_per_day = -1

    def __init__(self, item):
        self.item = item

    def update_sellin(self):
        self.item.sell_in += self.sellin_rate_per_day

    def check_expire(self):
        if (self.item.sell_in <= Constant.EXPIRE_DAY):
            self.quality_rate_per_day *= 2

    def check_quality(self):
        if (self.quality_rate_per_day > 0 and self.item.quality >= Constant.QUALITY_MAX) \
            or (self.quality_rate_per_day < 0 and self.item.quality <= Constant.QUALITY_MIN):
            self.quality_rate_per_day = 0

    def update_quality(self):
        if self.quality_rate_per_day != 0:
            self.item.quality += self.quality_rate_per_day
            if (self.quality_rate_per_day < 0):
                self.item.quality = max(self.item.quality, Constant.QUALITY_MIN)
            else:
                self.item.quality = min(self.item.quality, Constant.QUALITY_MAX)

class ConjuredItem(NormalItem):
    def __init__(self, item):
        super().__init__(item)
        self.quality_rate_per_day *= 2

class AgedBrieItem(NormalItem):
    def __init__(self, item):
        super().__init__(item)
        self.quality_rate_per_day = 1

class BackStageItem(AgedBrieItem):
    def value_added_check(self):
        if (self.item.sell_in <= 5):
            self.quality_rate_per_day = 3
        else:
            self.quality_rate_per_day = 2

    def check_expire(self):
        if (self.item.sell_in <= Constant.EXPIRE_DAY):
            self.item.quality = Constant.QUALITY_MIN
            self.quality_rate_per_day = 0
        elif (self.item.sell_in <= 10):
            self.value_added_check()

class SulfurasItem(NormalItem):
     def __init__(self, item):
        super().__init__(item)
        self.quality_rate_per_day = 0
        self.sellin_rate_per_day = 0

ItemTypeDict = {
    "Aged Brie": AgedBrieItem,
    "Backstage passes to a TAFKAL80ETC concert": BackStageItem,
    "Sulfuras, Hand of Ragnaros": SulfurasItem
}

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            instance_type = ConjuredItem if (item.name.startswith("Conjured ")) \
                else ItemTypeDict.get(item.name, NormalItem)
            instance = instance_type(item)
            instance.check_expire()
            if instance.quality_rate_per_day != 0:
                instance.check_quality()
            instance.update_quality()
            instance.update_sellin()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
