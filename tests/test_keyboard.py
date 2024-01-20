import pytest
from src.keyboard import Keyboard, KeyboardMixin


@pytest.fixture()
def keyboard() -> Keyboard:
    """
    Функция для создания экземпляра класса Keyboard.

    :return: Экземпляр класса Keyboard.
    """
    return Keyboard('logitech', 500.00, 20, 'EN')


def test_repr(keyboard: Keyboard):
    """ Тест метода __repr__
    """
    assert repr(keyboard) == "Keyboard('logitech', 500.0, 20, EN)"


def test_language_getter(keyboard: Keyboard) -> None:
    """ Тест language_getter
    """
    test_language_getter_1 = keyboard.language
    assert test_language_getter_1 == 'EN'


def test_language_setter(keyboard: Keyboard) -> None:
    """ Тест language_setter
    """
    keyboard.language = 'RU'
    test_language_setter_1 = keyboard.language
    assert test_language_setter_1 == 'RU'
    keyboard.language = 'EN'
    test_language_setter_2 = keyboard.language
    assert test_language_setter_2 == 'EN'


def test_change_lang(keyboard: Keyboard) -> None:
    """ Тест change_lang
    """
    keyboard.change_lang()
    test_change_lang_1 = keyboard.language
    assert test_change_lang_1 == 'RU'
    keyboard.change_lang()
    test_change_lang_2 = keyboard.language
    assert test_change_lang_2 == 'EN'
