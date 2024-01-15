import pytest
from src.phone import Phone


@pytest.fixture()
def phone() -> Phone:
    """
    Функция для создания экземпляра класса Phone.

    :return: Экземпляр класса Phone.
    """

    return Phone('fly', 15000.0, 15, 1)


def test_repr(phone: Phone) -> str:
    assert repr(phone) == "Phone('fly', 15000.0, 15, 1)"


def test_number_of_sim_setter(phone: Phone) -> int:
    phone.number_of_sim = 4
    assert phone.number_of_sim == 4
    phone.number_of_sim = 5
    assert phone.number_of_sim == 5


def test_number_of_sim_getter(phone: Phone) -> int:
    assert phone.number_of_sim == 1
