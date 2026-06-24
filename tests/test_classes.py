import pytest

from src.classes import Category, CategoryList, GetProduct, LawnGrass, Product, Smartphone, BaseProduct, Order


class TestProduct:
    def test_product_init(self):

        product = Product("Apple", "Simple apple", 50, 100)

        assert product.name == "Apple"
        assert product.description == "Simple apple"
        assert product.price == 50
        assert product.quantity == 100

    def test_product_new_product(self):
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

    def test_product_new_product_existing_product(self):
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
        assert new_prod_1.price == 190000.0
        assert new_prod_1.quantity == 10

        assert new_prod_2.name == "Samsung Galaxy S23 Ultra"
        assert new_prod_2.description == "256GB, Серый цвет, 200MP камера"
        assert new_prod_2.price == 190000.0
        assert new_prod_2.quantity == 10

    def test_product_str(self, capsys):
        product = Product("Apple", "Simple apple", 50, 100)
        print(product)
        captured = capsys.readouterr().out
        assert captured == "Product('Apple', 'Simple apple', 50, 100)\nApple, 50 руб. Остаток: 100 шт.\n"

    def test_product_add(self, capsys):
        product1 = Product("Apple", "Simple apple", 50, 100)
        product2 = Product("Phone", "Simple phone", 500, 10)
        print(product1 + product2)
        captured = capsys.readouterr().out
        assert (
            captured == "Product('Apple', 'Simple apple', 50, 100)\nProduct('Phone', 'Simple phone', 500, 10)\n10000\n"
        )

    def test_product_add_wrong_type(self, capsys):
        product = Product("Apple", "Simple apple", 50, 100)
        with pytest.raises(TypeError):
            print(product + "Phone")  # type: ignore


class TestCategory:
    def test_category_init(self):

        apple = Product("Apple", "Simple apple", 50, 100)
        category = Category("Фрукты", "Свежие фрукты", [apple])

        assert category.name == "Фрукты"
        assert category.description == "Свежие фрукты"
        assert category.category_count == 1
        assert category.product_count == 1

    def test_category_products(self):

        apple = Product("Apple", "Simple apple", 50, 100)
        category = Category("Фрукты", "Свежие фрукты", [apple])

        assert category.products == "Apple, 50 руб. Остаток: 100 шт.\n"

    def test_category_list_append(self):

        apple = Product("Apple", "Simple apple", 50, 100)
        category = Category("Фрукты", "Свежие фрукты", [apple])
        category_list = CategoryList()

        category_list.append(category)

        assert category_list.categories == [category]

    def test_category_find_by_name(self):

        apple = Product("Apple", "Simple apple", 50, 100)
        category = Category("Фрукты", "Свежие фрукты", [apple])
        category_list = CategoryList()

        category_list.append(category)

        assert category_list.find_by_name("Фрукты") == category

    def test_category_find_by_name_not_found(self):

        apple = Product("Apple", "Simple apple", 50, 100)
        category = Category("Фрукты", "Свежие фрукты", [apple])
        category_list = CategoryList()

        category_list.append(category)

        assert not category_list.find_by_name("Яблоки")

    def test_category_add_product(self):

        apple = Product("Apple", "Simple apple", 50, 100)
        category = Category("Фрукты", "Свежие фрукты", [apple])

        category.add_product(Product("Phone", "Simple phone", 500, 10))

        assert category.products == "Apple, 50 руб. Остаток: 100 шт.\nPhone, 500 руб. Остаток: 10 шт.\n"

    def test_category_add_product_not_product(self, capsys):
        apple = Product("Apple", "Simple apple", 50, 100)
        category = Category("Фрукты", "Свежие фрукты", [apple])
        with pytest.raises(TypeError):
            category.add_product("Phone")  # type: ignore

    def test_price_getter(self):
        product = Product("Apple", "Simple apple", 50, 100)
        assert product.price == 50

    def test_price_setter(self):
        product = Product("Apple", "Simple apple", 50, 100)
        product.price = 100
        assert product.price == 100

    def test_price_setter_negative(self, capsys):
        product = Product("Apple", "Simple apple", 50, 100)
        product.price = -100
        assert capsys.readouterr().out == (
            "Product('Apple', 'Simple apple', 50, 100)\n" "Цена не должна быть нулевая или отрицательная\n"
        )
        assert product.price == 50

    def test_price_setter_zero(self, capsys):
        product = Product("Apple", "Simple apple", 50, 100)
        product.price = 0
        assert capsys.readouterr().out == (
            "Product('Apple', 'Simple apple', 50, 100)\n" "Цена не должна быть нулевая или отрицательная\n"
        )
        assert product.price == 50

    def test_price_setter_lower_than_current_yes(self, monkeypatch):
        product = Product("Apple", "Simple apple", 50, 100)

        monkeypatch.setattr("builtins.input", lambda _: "Y")

        product.price = 40

        assert product.price == 40

    def test_price_setter_lower_than_current_no(self, monkeypatch):
        product = Product("Apple", "Simple apple", 50, 100)

        monkeypatch.setattr("builtins.input", lambda _: "N")

        product.price = 40

        assert product.price == 50

    def test_price_setter_higher_than_current(self):
        product = Product("Apple", "Simple apple", 50, 100)
        product.price = 60

        assert product.price == 60

    def test_category_str(self, capsys):

        apple = Product("Apple", "Simple apple", 50, 100)
        category = Category("Фрукты", "Свежие фрукты", [apple])

        print(category)
        captured = capsys.readouterr().out

        assert captured == "Product('Apple', 'Simple apple', 50, 100)\nФрукты, 100 шт.\n"


class TestCategoryList:
    def test_category_list_get_all_categories(self):

        apple = Product("Apple", "Simple apple", 50, 100)
        category = Category("Фрукты", "Свежие фрукты", [apple])
        phone = Product("Phone", "Simple phone", 500, 10)
        category2 = Category("Телефоны", "Свежие телефоны", [phone])
        category_list = CategoryList()

        category_list.append(category)
        category_list.append(category2)
        assert category_list.get_all_categories_names() == ["Фрукты", "Телефоны"]


class TestGetProduct:
    def test_get_product_iter(self):
        apple = Product("Apple", "Simple apple", 50, 100)
        category = Category("Фрукты", "Свежие фрукты", [apple])
        get_product = GetProduct(category)
        assert iter(get_product) == get_product

    def test_get_product_next(self):
        apple = Product("Apple", "Simple apple", 50, 100)
        category = Category("Фрукты", "Свежие фрукты", [apple])
        get_product = GetProduct(category)
        assert next(get_product) == "Apple, 50 руб. Остаток: 100 шт.\n"
        with pytest.raises(StopIteration):
            next(get_product)


class TestSmartphone:
    def test_smartphone_init(self):
        apple = Smartphone("Apple", "Simple apple", 50, 100, 10, "iPhone", 128, "Black")
        assert apple.efficiency == 10
        assert apple.model == "iPhone"
        assert apple.memory == 128
        assert apple.color == "Black"


class TestLawnGrass:
    def test_lawn_grass_init(self):
        grass = LawnGrass("Grass", "Simple grass", 50, 100, "Russia", 10, "Green")
        assert grass.country == "Russia"
        assert grass.germination_period == 10
        assert grass.color == "Green"


class TestBaseProduct:
    """Тесты для абстрактного класса BaseProduct"""

    def test_base_product_abstract_methods(self):
        """Проверка, что BaseProduct требует реализации __init__"""
        # Попытка создать экземпляр абстрактного класса должна вызвать ошибку
        with pytest.raises(TypeError):
            BaseProduct("Test", "Description", 100, 10)

    def test_product_inherits_base_product(self):
        """Проверка, что Product наследует BaseProduct"""
        assert issubclass(Product, BaseProduct)

    def test_product_implements_abstract_methods(self):
        """Проверка, что Product реализует все абстрактные методы"""
        product = Product("Test", "Description", 100, 10)

        # Проверяем, что у продукта есть все необходимые атрибуты
        assert hasattr(product, 'name')
        assert hasattr(product, 'description')
        assert hasattr(product, 'price')
        assert hasattr(product, 'quantity')

        assert isinstance(product.name, str)
        assert isinstance(product.description, str)
        assert isinstance(product.price, (float, int))
        assert isinstance(product.quantity, int)


class TestOrder:
    """Тесты для класса Order"""

    def test_order_init(self):
        """Тест инициализации класса Order"""
        product1 = Product("Test", "Description", 100, 10)
        order = Order(product1, 5)
        assert order.product == product1
        assert order.quantity == 5
        assert order.total_price == 500

    def test_order_init_with_invalid_quantity(self):
        """Тест инициализации класса Order с некорректным количеством товара"""
        product1 = Product("Test", "Description", 100, 10)
        with pytest.raises(ValueError):
            Order(product1, -5)
        with pytest.raises(ValueError):
            Order(product1, 0)
        with pytest.raises(ValueError):
            Order(product1, 15)


    def test_order_str(self, capsys):
        product1 = Product("Test", "Description", 100, 10)
        order = Order(product1, 5)
        print(order)
        captured = capsys.readouterr().out
        assert captured == (f"Product('Test', 'Description', 100, 10)\n"
                            f"Заказ: {product1.name}, {order.quantity} шт., Итого: {order.total_price} руб.\n")