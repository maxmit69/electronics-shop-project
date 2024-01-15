"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def item() -> Item:
    """
    Функция для создания экземпляра класса item.

    :return: Экземпляр класса item.
    """
    return Item("test", 10, 10)


@pytest.fixture()
def phone() -> Phone:
    """
    Функция для создания экземпляра класса Phone.

    :return: Экземпляр класса Phone.
    """

    return Phone('fly', 15000.0, 15, 1)


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


def test_instantiate_from_csv(item: Item) -> None:
    """
    Тест для функции instantiate_from_csv.

    :param item: Экземпляр класса item.
    """
    Item.instantiate_from_csv('/home/sergei/PycharmProjects/electronics-shop-project/src/items.csv')
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[0].price == 100
    assert Item.all[0].quantity == 1
    assert Item.all[1].name == 'Ноутбук'
    assert Item.all[1].price == 1000
    assert Item.all[1].quantity == 3
    assert Item.all[2].name == 'Кабель'


def test_string_to_number(item: Item) -> int:
    """
    Тест для функции string_to_number.

    :param item: Экземпляр класса item.
    """
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name_getter(item: Item) -> str:
    """
    Тест для функции name.getter.

    :param item: Экземпляр класса item.
    """
    assert item.name == 'test'


def test_name_setter(item: Item) -> None:
    """
    Тест для функции name.setter.

    :param item: Экземпляр класса item.
    """
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'


def test_repr(item: Item) -> str:
    """ Тест метода __repr__
    """
    assert repr(item) == "Item('test', 10, 10)"


def test_str(item: Item) -> str:
    """ Тест метода __str__
    """
    assert str(item) == 'test'


def test_add(item, phone) -> None:
    """ Тест метода __add__
    :param item Экземпляр класса item и дочерний экземпляр класс phone
    """
    item1 = Item("test", 10, 10)
    phone1 = Phone('fly', 15000.0, 15, 1)
    assert isinstance(phone1, item1.__class__) == True
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 30
