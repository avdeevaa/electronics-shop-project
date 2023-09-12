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

def test_instantiate_from_csv():
    file_name = 'src/items.csv'
    Item.instantiate_from_csv(file_name)
    assert len(Item.all) == 8 # потому что он собирает и те предыдущие экземпляры(3 + 5 из файла)

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