# -*- coding: utf-8 -*-

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
        pass

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


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
        self.conjured_items = [item for item in items if isinstance(item, ConjuredItem)]
        self.normal_items = [item for item in items if item.name != "Conjured"]

    def update_quality(self):
        for item in self.conjured_items:
            item.update_quality()
        GildedRoseLegacy(self.normal_items).update_quality()
