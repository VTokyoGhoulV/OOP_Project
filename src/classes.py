from typing import Any, Dict, Optional


class Product:
    """
    Класс, описывающий товар
    """

    __all_products: list = list()

    def __init__(self, name: str, description: str, price: int, quantity: int):
        self.name: str = name
        self.description: str = description
        self.__price: int = price
        self.quantity: int = quantity

        Product.__all_products.append(self)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Product) -> int:
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def new_product(cls, product_params: Dict[str, Any]) -> Product:
        """
        Создает новый продукт или изменяет уже существующий (складывает количество и ставит высшую цену)
        """

        existing_product: Optional[Product] = None

        for product in Product.__all_products:

            if product.name == product_params["name"]:

                existing_product = product
                break

        if existing_product:

            existing_product.quantity += product_params["quantity"]

            if product_params["price"] > existing_product.price:
                existing_product.price = product_params["price"]

            return existing_product

        else:

            return cls(
                product_params["name"],
                product_params["description"],
                product_params["price"],
                product_params["quantity"],
            )

    @property
    def price(self) -> int:
        """
        Возвращает цену продукта
        """
        return self.__price

    @price.setter
    def price(self, new_price: int) -> None:
        """
        Устанавливает новую цену на товар
        """

        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")

        elif new_price < self.__price:
            user_input = input("Цена ниже существующей, вы уверены что хотите продолжить? Y - Да N - Нет\n>>>").upper()

            if user_input == "Y":
                self.__price = new_price

            else:
                print("Операция отменена")

        else:
            self.__price = new_price


class Category:
    """
    Класс, описывающий категорию
    """

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        self.name: str = name
        self.description: str = description
        self.__products: list = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        total_products = sum(product.quantity for product in self.__products)
        return f"{self.name}, {total_products} шт."

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию
        """

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Возвращает все продукты в категории
        """

        return "".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n" for product in self.__products
        )

    @property
    def products_list(self) -> list[Product]:
        return self.__products


class CategoryList:
    """
    Класс, описывающий список категорий
    """

    def __init__(self) -> None:
        self.categories: list[Category] = list()

    def append(self, category: Category) -> None:
        """
        Добавляет в список категорий новую категорию
        """
        self.categories.append(category)

    def find_by_name(self, name: str) -> Category | None:
        """
        Возвращает категорию соответствующую получаемому имени категории
        """

        for category in self.categories:
            if category.name == name:

                return category

        return None

    def get_all_categories_names(self) -> list:
        """
        Возвращает список имен всех категорий в списке
        """

        names = list()

        for category in self.categories:
            names.append(category.name)

        return names


class GetProduct:
    """
    Класс, позволяющий перебрать все товары в категории
    """

    def __init__(self, category: Category) -> None:
        self.category = category
        self.index: int = 0

    def __iter__(self) -> GetProduct:
        self.index = 0
        return self

    def __next__(self) -> str:
        if self.index < len(self.category.products_list):
            product = self.category.products_list[self.index]
            self.index += 1
            return f"{str(product)}\n"
        else:
            raise StopIteration
