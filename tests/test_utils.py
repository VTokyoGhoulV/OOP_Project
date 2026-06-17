import pytest

from src.utils import find_project_root, from_file_to_classes


def test_from_file_to_classes():

    category_list = from_file_to_classes()
    category = category_list.categories[0]

    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    product = category.products
    assert (
        product == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_find_project_root_not_found():

    with pytest.raises(RuntimeError):
        find_project_root("")
