import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self) -> str:
        """ Преобразование экземпляра класса item в строку
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        """ Преобразование экземпляра класса item в строку
        """
        return self.__name

    def __add__(self, other):
        """ Сложение экземпляров одного класса
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        else:
            raise TypeError("Экземпляры классов должны принадлежать одному классу")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if len(value) > 10:
            self.__name = value[0:10]
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls, file_name: str) -> None:
        """
        Создание экземпляра класса item из файла.

        :param file_name: Путь к файлу с данными по товарам.
        """
        cls.all.clear()
        with open(file_name, encoding="UTF=8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = cls.string_to_number(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string: str) -> int:
        """
        Преобразование строки в число.

        :param string: Преобразованная строка.
        :return: Преобразованное число.
        """
        return int(float(string))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

