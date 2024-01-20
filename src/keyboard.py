from src.item import Item


class KeyboardMixin:
    """ Миксин для дочернего класса
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """ Инициализация атрибутов экземпляра класса
        """
        super().__init__(name, price, quantity)
        self.language = 'EN'

    def change_lang(self) -> None:
        """ Метод для изменения языка
        """
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'


class Keyboard(KeyboardMixin, Item):
    """ Дочерний класс добавляет атрибут язык и метод для изменения языка (раскладки клавиатуры)
    """

    def __init__(self, name: str, price: float, quantity: int, language: str = 'EN') -> None:
        """ Инициализация атрибутов экземпляра класса и добавление атрибутов родительского класса
        """
        super().__init__(name, price, quantity)
        self.__language = language

    def __repr__(self) -> str:
        """ Переопределение метода из базового класса
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__language})"

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, lang) -> None:
        """ Проверка на валидность языка
        """
        if lang in ['EN', 'RU']:
            self.__language = lang
        else:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
