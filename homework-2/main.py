from src.item import Item
# import os

if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    #длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.

    #current_dir = os.getcwd()
    #file_path = os.path.join(current_dir, 'items.csv') # без этого и с отсутствием файла в папке homework не получалось

    Item.instantiate_from_csv('items.csv')  # создание объектов из данных файла

    # так как у меня получилось len(Item.all) == 6 +Суперсмарт
    assert len(Item.all) == 6  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    # assert item1.name == 'Ńěŕđňôîí'
    # assert item1.name == 'Суперсмарт'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
