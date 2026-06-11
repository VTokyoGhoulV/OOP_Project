class Product:
    """
    Класс, описывающий товар
    """

    def __init__(self, name, description, price, quantity):
        self.name: str = name
        self.description: str = description
        self.price: int = price
        self.quantity: int = quantity


class Category:
    """
    Класс, описывающий категорию
    """

    total_categories: int = 0
    total_products: int = 0

    def __init__(self, name, description, products):
        self.name: int = name
        self.description: str = description
        self.products: list = products

        Category.total_categories += 1
        Category.total_products += len(products)


    def show_products(self):

        info = ""
        for product in self.products:
            info += f"{product.name} - {product.description} - {product.price} - {product.quantity}\n"

        return info


class CategoryList:
    """
    Класс, описывающий список категорий
    """
    def __init__(self):
        self.categories = list()

    def append(self, category):
        self.categories.append(category)

    def remove(self, name):
        self.categories.remove(self.find_by_name(name))

    def find_by_name(self, name):

        for category in self.categories:
            if category.name == name:

                return category

        return None

    def show_all(self):
        for category in self.categories:
            print(category.name)