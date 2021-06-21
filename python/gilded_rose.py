# -*- coding: utf-8 -*-
from ctypes import Union


class GildedRoseLegacy(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


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
        self.items = [item for item in items if isinstance(item, (ConjuredItem, SulfuraItem, AgedBrie, Backstage, Item))]
        self.legacy_items = [item for item in items if not isinstance(item, (ConjuredItem, SulfuraItem, AgedBrie, Backstage, Item))]

    def update_quality(self):
        for item in self.items:
            item.update_quality()
        GildedRoseLegacy(self.legacy_items).update_quality()
