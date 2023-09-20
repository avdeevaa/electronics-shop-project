from src.phone import Phone

def test_repr():
    phone = Phone("iPhone 14", 120000, 20, 2)
    assert Phone.__repr__(phone) == "Phone('iPhone 14', 120000, 20, 2)"


class NotItem():
    """класс для провеки сложения"""
    def __init__(self, name, price, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


def test_add():
    phone = Phone("Смартфон", 10000, 20, 2)
    phone1 = Phone("Айфон", 70000, 10, 1)
    assert Phone.__add__(phone, phone1) == 30
    notitem = NotItem("Тетрадь", 10, 150)
    assert Phone.__add__(phone, notitem) == "Складывать можно только объекты Phone и дочерние от них."
