from python.gilded_rose import ConjuredItem, GildedRose, Item


def test_conjured_item_is_decaying_twice_as_fast():
    item = ConjuredItem(10, 50)

    GildedRose(items=[item]).update_quality()

    assert item.sell_in == 9
    assert item.quality == 48


def test_conjured_item_is_decaying_twice_as_fast_when_sell_in_has_passed():
    item = ConjuredItem(0, 40)

    GildedRose(items=[item]).update_quality()

    assert item.sell_in == -1
    assert item.quality == 36


def test_conjured_item_quality_cannot_be_negative():
    item = ConjuredItem(0, 1)

    GildedRose(items=[item]).update_quality()

    assert item.sell_in == -1
    assert item.quality == 0


def test_normal_item():
    item = Item("Normal", 10, 50)

    GildedRose(items=[item]).update_quality()

    assert item.sell_in == 9
    assert item.quality == 49


def test_conjured_and_normal_items():
    conjured_item = ConjuredItem(10, 50)
    normal_item = Item("Normal", 10, 50)

    GildedRose(items=[conjured_item, normal_item]).update_quality()

    assert conjured_item.sell_in == 9
    assert conjured_item.quality == 48
    assert normal_item.sell_in == 9
    assert normal_item.quality == 49


def test_multiple_conjured_and_normal_items():
    first_conjured_item = ConjuredItem(10, 50)
    second_conjured_item = ConjuredItem(8, 46)
    first_normal_item = Item("Normal", 10, 50)
    second_normal_item = Item("Normal", 9, 40)

    GildedRose(items=[first_conjured_item, second_conjured_item, first_normal_item, second_normal_item]).update_quality()

    assert first_conjured_item.sell_in == 9
    assert first_conjured_item.quality == 48
    assert second_conjured_item.sell_in == 7
    assert second_conjured_item.quality == 44
    assert first_normal_item.sell_in == 9
    assert first_normal_item.quality == 49
    assert second_normal_item.sell_in == 8
    assert second_normal_item.quality == 39
