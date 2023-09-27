from src.item import Item

def test_calculate_total_price():
    item = Item("Смартфон", 10000, 20)
    assert item.calculate_total_price() == 200000

def test_apply_discount():
    item = Item("Смартфон", 10000, 20)
    item.pay_rate = 0.8
    assert item.apply_discount() == 8000.0

def test_name():
    item = Item("Смартфон", 10000, 20)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'

from src.item import InstantiateCSVError
def test_instantiate_from_csv():
    file_name = 'src/items.csv'
    Item.instantiate_from_csv(file_name)
    assert len(Item.all) == 8 # потому что он собирает и те предыдущие экземпляры(3 + 5 из файла)

def test_instantiate_from_csv():
    # тесты для исключений
    file_name1 = 'homework-6/item3.csv'

    try:
        Item.instantiate_from_csv(file_name1)
    except FileNotFoundError as e:
        assert str(e) == f"Отсутствует файл {file_name1}"

    file_name2 = 'homework-6/items.csv'
    try:
        Item.instantiate_from_csv(file_name2)
    except InstantiateCSVError as e:
        assert str(e) == 'Файл item.csv поврежден.'

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('60') == 60
    assert Item.string_to_number('8.1') == 8

def test_repr():
    item = Item("Смартфон", 10000, 20)
    assert Item.__repr__(item) == "Item('Смартфон', 10000, 20)"

def test_str():
    item = Item("Смартфон", 10000, 20)
    assert Item.__str__(item) == 'Смартфон'


class NotItem:
    """класс для провеки сложения"""
    def __init__(self, name, price, quantity : int):
        self.name = name
        self.price = price
        self.quantity = quantity

def test_add():
    item = Item("Смартфон", 10000, 20)
    item1 = Item("Айфон", 70000, 10)
    assert Item.__add__(item, item1) == 30
    notitem = NotItem("Тетрадь", 10, 150)
    assert Item.__add__(item, notitem) == "Складывать можно только объекты Item и дочерние от них."

