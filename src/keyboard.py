from src.item import Item

class MixinLog:
    LANGUAGE = "EN"

    def __init__(self):
        pass

    def change_lang(self):
        """метод для изменения языка"""
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'

class Keyboard(Item, MixinLog):

    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value="EN"):
        if value != "EN" and value != "RU":
            raise ValueError
        else:
            self.__language = value


    def change_lang(self):
        """Переопределение метода change_lang для класса Keyboard"""
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"






