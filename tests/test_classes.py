from src.classes import Product, Category


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
    assert category.total_categories == 1
    assert category.total_products == 1
