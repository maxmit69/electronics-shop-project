from src.item import Item


class Phone(Item):
    """ Дочерний класс добавляет атрибут сим-карта и возможность менять их количество
     """

    def __init__(self, name: str, price: float, quantity: int, sim_count: int) -> None:
        """ Инициализация атрибутов экземпляра класса и добавление атрибутов родительского класса
        """
        super().__init__(name, price, quantity)
        self.__sim_count = sim_count

    def __repr__(self) -> str:
        """ Переопределение метода из базового класса
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__sim_count})"

    @property
    def number_of_sim(self) -> int:
        return self.__sim_count

    @number_of_sim.setter
    def number_of_sim(self, num) -> int:
        """ Проверка на валидность сим-карты
        """
        if isinstance(num, int) and num > 0:
            self.__sim_count = num
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
