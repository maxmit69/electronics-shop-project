from src.item import Item


class KeyboardMixin:
    """ Миксин для дочернего класса
    """
    __language = 'EN'

    def change_lang(self) -> None:
        """ Метод для изменения языка
        """
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'

    @property
    def language(self) -> str:
        """ Метод для получения языка
        """
        return self.__language

    @language.setter
    def language(self, value: str) -> None:
        """ Метод для проверки языка
        """
        if value in ('EN', 'RU'):
            self.__language = value
        else:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")


class Keyboard(KeyboardMixin, Item):
    """ Класс для товара “клавиатура”
    """
    pass
