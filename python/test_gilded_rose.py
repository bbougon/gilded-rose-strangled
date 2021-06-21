from python.gilded_rose import ConjuredItem, GildedRose, Item, SulfuraItem, AgedBrie, Backstage


def test_conjured_item_is_decaying_twice_as_fast():
    item = ConjuredItem(10, 50)

    GildedRose(items=[item]).update_quality()

    assert item.name == "Conjured"
    assert_item(item, 9, 48)


def assert_item(item, sell_in, quality):
    assert item.sell_in == sell_in
    assert item.quality == quality


def test_conjured_item_is_decaying_twice_as_fast_when_sell_in_has_passed():
    item = ConjuredItem(0, 40)

    GildedRose(items=[item]).update_quality()

    assert_item(item, -1, 36)


def test_conjured_item_quality_cannot_be_negative():
    item = ConjuredItem(0, 1)

    GildedRose(items=[item]).update_quality()

    assert_item(item, -1, 0)


def test_normal_item():
    item = Item("Normal", 10, 50)

    GildedRose(items=[item]).update_quality()

    assert_item(item, 9, 49)


def test_conjured_and_normal_items():
    conjured_item = ConjuredItem(10, 50)
    normal_item = Item("Normal", 10, 50)

    GildedRose(items=[conjured_item, normal_item]).update_quality()

    assert_item(conjured_item, 9, 48)
    assert_item(normal_item, 9, 49)


def test_multiple_conjured_and_normal_items():
    first_conjured_item = ConjuredItem(10, 50)
    second_conjured_item = ConjuredItem(8, 46)
    first_normal_item = Item("Normal", 10, 50)
    second_normal_item = Item("Normal", 9, 40)

    GildedRose(items=[first_conjured_item, second_conjured_item, first_normal_item, second_normal_item]).update_quality()

    assert_item(first_conjured_item, 9, 48)
    assert_item(second_conjured_item, 7, 44)
    assert_item(first_normal_item, 9, 49)
    assert_item(second_normal_item, 8, 39)


def test_sulfuras():
    sulfura = SulfuraItem(0)

    GildedRose(items=[sulfura]).update_quality()

    assert sulfura.name == "Sulfuras, Hand of Ragnaros"
    assert_item(sulfura, 0, 80)


def test_sulfuras_does_not_decay_in_the_past():
    sulfura = SulfuraItem(-1)

    GildedRose(items=[sulfura]).update_quality()

    assert_item(sulfura, -1, 80)


def test_aged_brie_is_improved():
    aged_brie = AgedBrie(11, 29)

    GildedRose(items=[aged_brie]).update_quality()

    assert_item(aged_brie, 10, 30)


def test_aged_brie_has_maximum_50_quality():
    aged_brie = AgedBrie(0, 50)

    GildedRose(items=[aged_brie]).update_quality()

    assert_item(aged_brie, -1, 50)


def test_backstage():
    backstage = Backstage(15, 20)

    GildedRose(items=[backstage]).update_quality()

    assert backstage.name == "Backstage passes to a TAFKAL80ETC concert"
    assert_item(backstage, 14, 21)


def test_backstage_has_quality_improved_twice_at_10_days_from_concert():
    backstage = Backstage(10, 45)

    GildedRose(items=[backstage]).update_quality()

    assert_item(backstage, 9, 47)


def test_backstage_has_quality_improved_by_three_at_5_days_from_concert():
    backstage = Backstage(5, 45)

    GildedRose(items=[backstage]).update_quality()

    assert_item(backstage, 4, 48)


def test_backstage_has_maximum_quality():
    backstage = Backstage(5, 48)

    GildedRose(items=[backstage]).update_quality()

    assert_item(backstage, 4, 50)


def test_backstage_has_zero_quality_after_concert():
    backstage = Backstage(0, 48)

    GildedRose(items=[backstage]).update_quality()

    assert_item(backstage, -1, 0)


def test_normal_item_is_decaying_by_one():
    item = Item("+5 Dexterity Vest", 11, 50)

    GildedRose(items=[item]).update_quality()

    assert item.name == "+5 Dexterity Vest"
    assert_item(item, 10, 49)


def test_normal_item_is_decaying_twice_as_fast_when_sell_in_is_negative():
    item = Item("+5 Dexterity Vest", 0, 50)

    GildedRose(items=[item]).update_quality()

    assert item.name == "+5 Dexterity Vest"
    assert_item(item, -1, 48)