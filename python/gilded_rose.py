# -*- coding: utf-8 -*-
from ctypes import Union


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        self.sell_in -= 1
        self.quality -= 2 if self.sell_in < 0 else 1

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class SulfuraItem(Item):

    def __init__(self, sell_in):
        super().__init__("Sulfuras, Hand of Ragnaros", sell_in, 80)

    def update_quality(self):
        pass


class AgedBrie(Item):

    def __init__(self, sell_in, quality):
        super().__init__("Aged Brie", sell_in, quality)

    def update_quality(self):
        self.sell_in -= 1
        self.quality += 1 if self.quality < 50 else 0


class Backstage(Item):

    def __init__(self, sell_in, quality):
        super().__init__("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)

    def update_quality(self):
        self.sell_in -= 1
        self.quality += 3 if self.sell_in < 6 else 2 if self.sell_in < 11 else 1
        if self.quality > 50:
            self.quality = 50
        if self.sell_in < 0:
            self.quality = 0


class ConjuredItem(Item):

    def __init__(self, sell_in, quality):
        super().__init__("Conjured", sell_in, quality)

    def update_quality(self):
        self.sell_in -= 1
        self.quality -= 2 if self.sell_in > 0 else 4
        if self.quality < 0:
            self.quality = 0


class GildedRose(object):

    def __init__(self, items) -> None:
        super().__init__()
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()
