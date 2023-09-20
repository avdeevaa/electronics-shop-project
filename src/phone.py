from src.item import Item

class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim


    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})")


    def __add__(self, other):
        if isinstance(other, Phone):
            return int(self.quantity) + int(other.quantity)
        return "Складывать можно только объекты Phone и дочерние от них."







