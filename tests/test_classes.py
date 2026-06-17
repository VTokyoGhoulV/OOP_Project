from src.classes import Category, CategoryList, Product


# тесты для класса Product
def test_product_init():

    product = Product("Apple", "Simple apple", 50, 100)

    assert product.name == "Apple"
    assert product.description == "Simple apple"
    assert product.price == 50
    assert product.quantity == 100


def test_product_new_product():
    new_prod = Product.new_product(
        {
            "name": "Samsung Galaxy S22 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_prod.name == "Samsung Galaxy S22 Ultra"
    assert new_prod.description == "256GB, Серый цвет, 200MP камера"
    assert new_prod.price == 180000.0
    assert new_prod.quantity == 5


def test_product_new_product_existing_product():
    new_prod_1 = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    new_prod_2 = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 190000.0,
            "quantity": 5,
        }
    )
    assert new_prod_1.name == "Samsung Galaxy S23 Ultra"
    assert new_prod_1.description == "256GB, Серый цвет, 200MP камера"
    assert new_prod_1.price == 180000.0
    assert new_prod_1.quantity == 5

    assert new_prod_2.name == "Samsung Galaxy S23 Ultra"
    assert new_prod_2.description == "256GB, Серый цвет, 200MP камера"
    assert new_prod_2.price == 190000.0
    assert new_prod_2.quantity == 10


# тесты для класса Category
def test_category_init():

    apple = Product("Apple", "Simple apple", 50, 100)
    category = Category("Фрукты", "Свежие фрукты", [apple])

    assert category.name == "Фрукты"
    assert category.description == "Свежие фрукты"
    assert category.category_count == 1
    assert category.product_count == 1


def test_category_products():

    apple = Product("Apple", "Simple apple", 50, 100)
    category = Category("Фрукты", "Свежие фрукты", [apple])

    assert category.products == "Apple, 50 руб. Остаток: 100 шт.\n"


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


def test_category_add_product():

    apple = Product("Apple", "Simple apple", 50, 100)
    category = Category("Фрукты", "Свежие фрукты", [apple])

    category.add_product(Product("Phone", "Simple phone", 500, 10))

    assert category.products == "Apple, 50 руб. Остаток: 100 шт.\nPhone, 500 руб. Остаток: 10 шт.\n"


def test_price_getter():
    product = Product("Apple", "Simple apple", 50, 100)
    assert product.price == 50


def test_price_setter():
    product = Product("Apple", "Simple apple", 50, 100)
    product.price = 100
    assert product.price == 100


def test_price_setter_negative(capsys):
    product = Product("Apple", "Simple apple", 50, 100)
    product.price = -100
    assert capsys.readouterr().out == "Цена не должна быть нулевая или отрицательная\n"
    assert product.price == 50


def test_price_setter_zero(capsys):
    product = Product("Apple", "Simple apple", 50, 100)
    product.price = 0
    assert capsys.readouterr().out == "Цена не должна быть нулевая или отрицательная\n"
    assert product.price == 50


def test_price_setter_lower_than_current_yes(monkeypatch):
    product = Product("Apple", "Simple apple", 50, 100)

    monkeypatch.setattr("builtins.input", lambda _: "Y")

    product.price = 40

    assert product.price == 40


def test_price_setter_lower_than_current_no(monkeypatch):
    product = Product("Apple", "Simple apple", 50, 100)

    monkeypatch.setattr("builtins.input", lambda _: "N")

    product.price = 40

    assert product.price == 50


def test_price_setter_higher_than_current():
    product = Product("Apple", "Simple apple", 50, 100)
    product.price = 60

    assert product.price == 60


# тесты для класса CategoryList
def test_category_list_get_all_categories():

    apple = Product("Apple", "Simple apple", 50, 100)
    category = Category("Фрукты", "Свежие фрукты", [apple])
    phone = Product("Phone", "Simple phone", 500, 10)
    category2 = Category("Телефоны", "Свежие телефоны", [phone])
    category_list = CategoryList()

    category_list.append(category)
    category_list.append(category2)
    assert category_list.get_all_categories_names() == ["Фрукты", "Телефоны"]
