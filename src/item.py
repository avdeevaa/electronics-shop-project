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

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    @property
    def name(self):
        """возвращает название товара"""
        return self.__name

    @name.setter
    def name(self, name):
        """присваивает название товара
        если название больше 10 символов, то выдает первых 10 символов"""
        if len(str(name)) <= 10:
            self.__name = name

        else:
            self.__name = str(name[0:10])


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
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls, file_name):
        """инициализирует экземпляры класса Item данными из файла"""

        with open(file_name) as file:
            DictReader_obj = csv.DictReader(file)
            for i in DictReader_obj:
                name = i['name']
                price = int(i['price'])
                quantity = int(i['quantity'])

                item = cls(name, price, quantity)


    @staticmethod
    def string_to_number(str_number):
        """возвращает число из строка из числа строки"""
        if "." in str_number:
            fl_num = str_number.split(".")
            part = fl_num[:1]
            fin_num = "".join(part)
            return int(fin_num)
        else:
            number = int(str_number)
            return number

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        return "Складывать можно только объекты Item и дочерние от них."