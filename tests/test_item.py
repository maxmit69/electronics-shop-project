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


def test_calculate_total_price(item: Item) -> float:
    """
    Тест для функции calculate_total_price.

    :param item: Экземпляр класса item.
    """
    assert item.calculate_total_price() == 100.0
    assert Item
    assert len(Item.all) == 1


def test_apply_discount(item: Item) -> None:
    """
    Тест для функции apply_discount.

    :param item: Экземпляр класса item.
    """
    item.apply_discount()
    assert item.price == 10.0
    assert Item
    assert len(Item.all) == 2
