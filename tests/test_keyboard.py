import pytest
from src.keyboard import Keyboard, KeyboardMixin


@pytest.fixture()
def keyboard() -> Keyboard:
    """
    Функция для создания экземпляра класса Keyboard.

    :return: Экземпляр класса Keyboard.
    """
    return Keyboard('logitech', 500.00, 20)


def test_change_lang(keyboard: Keyboard) -> None:
    """ Метод для изменения языка
    """
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'


def test_language(keyboard: Keyboard) -> None:
    """ Метод для проверки языка
    """
    assert keyboard.language == 'EN'
    keyboard.language = 'RU'
    assert keyboard.language == 'RU'
    with pytest.raises(AttributeError):
        keyboard.language = 'XX'

