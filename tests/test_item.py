"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item() -> Item:
    """
    Функция для создания экземпляра класса item.

    :return: Экземпляр класса item.
    """
    return Item("test", 10, 10)


def test_calculate_total_price(item: Item) -> None:
    """
    Тест для функции calculate_total_price.

    :param item: Экземпляр класса item.
    """
    assert item.calculate_total_price() == 100
    assert Item.all == []
    assert len(Item.all) == 0


def test_apply_discount(item: Item) -> None:
    """
    Тест для функции apply_discount.

    :param item: Экземпляр класса item.
    """
    item.apply_discount()
    assert item.price == 10
    assert Item.all == ["test", 10]
    assert len(Item.all) == 2
