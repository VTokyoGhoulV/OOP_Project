from src.classes import Category, CategoryList, Product


def test_product_init():

    product = Product("Apple", "Simple apple", 50, 100)

    assert product.name == "Apple"
    assert product.description == "Simple apple"
    assert product.price == 50
    assert product.quantity == 100


def test_category_init():

    apple = Product("Apple", "Simple apple", 50, 100)
    category = Category("Фрукты", "Свежие фрукты", [apple])

    assert category.name == "Фрукты"
    assert category.description == "Свежие фрукты"
    assert category.products == [apple]
    assert category.category_count == 1
    assert category.product_count == 1


def test_category_show_products():

    apple = Product("Apple", "Simple apple", 50, 100)
    category = Category("Фрукты", "Свежие фрукты", [apple])

    assert category.show_products() == "Apple - Simple apple - 50 - 100"


def test_category_list_append():

    apple = Product("Apple", "Simple apple", 50, 100)
    category = Category("Фрукты", "Свежие фрукты", [apple])
    category_list = CategoryList()

    category_list.append(category)

    assert category_list.categories == [category]


def test_category_find_by_name():

    apple = Product("Apple", "Simple apple", 50, 100)
    category = Category("Фрукты", "Свежие фрукты", [apple])
    category_list = CategoryList()

    category_list.append(category)

    assert category_list.find_by_name("Фрукты") == category


def test_category_find_by_name_not_found():

    apple = Product("Apple", "Simple apple", 50, 100)
    category = Category("Фрукты", "Свежие фрукты", [apple])
    category_list = CategoryList()

    category_list.append(category)

    assert not category_list.find_by_name("Яблоки")


def test_category_list_get_all_categories():

    apple = Product("Apple", "Simple apple", 50, 100)
    category = Category("Фрукты", "Свежие фрукты", [apple])
    phone = Product("Phone", "Simple phone", 500, 10)
    category2 = Category("Телефоны", "Свежие телефоны", [phone])
    category_list = CategoryList()

    category_list.append(category)
    category_list.append(category2)
    assert category_list.get_all_categories_names() == ["Фрукты", "Телефоны"]
