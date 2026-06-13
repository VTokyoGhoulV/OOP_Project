import pytest

from src.utils import from_file_to_classes, find_project_root


def test_from_file_to_classes():

    category_list = from_file_to_classes()
    category = category_list.categories[0]

    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert category.products[0].name == "Samsung Galaxy C23 Ultra"

def test_find_project_root_not_found():

    with pytest.raises(RuntimeError):
        find_project_root("")