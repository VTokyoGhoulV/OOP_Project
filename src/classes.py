from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class BaseProduct(ABC):
    """
    Абстрактный класс, описывающий общие методы для всех продуктов
    """

    @abstractmethod
    def __init__(self, name: str, description: str, price: float | int, quantity: int):
        self.name: str = name
        self.description: str = description
        self._price: float | int = price
        self.quantity: int = quantity


class BaseOrderCategory(ABC):
    """Абстрактный класс для Order и Category"""

    @abstractmethod
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


class InitMixin:
    """
    Миксин, выводящий информацию о том, от какого класса
    наследован и с какими параметрами был создан объект
    """

    def __init__(self, *args):
        print(f"{self.__class__.__name__}{args}")


class Product(BaseProduct, InitMixin):
    """
    Класс, описывающий товар
    """

    _all_products: list = list()

    def __init__(self, name: str, description: str, price: float | int, quantity: int):
        super().__init__(name, description, price, quantity)  # <--- ВЫЗОВ конструктора BaseProduct
        
        InitMixin.__init__(self, name, description, price, quantity)

        Product._all_products.append(self)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Product) -> float | int:
        if isinstance(other, type(self)):
            return (self._price * self.quantity) + (other._price * other.quantity)
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product_params: Dict[str, Any]) -> Product:
        """
        Создает новый продукт или изменяет уже существующий (складывает количество и ставит высшую цену)
        """

        existing_product: Optional[Product] = None

        for product in Product._all_products:

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
    def price(self) -> float | int:
        """
        Возвращает цену продукта
        """
        return self._price

    @price.setter
    def price(self, new_price: float | int) -> None:
        """
        Устанавливает новую цену на товар
        """

        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")

        elif new_price < self._price:
            user_input = input("Цена ниже существующей, вы уверены что хотите продолжить? Y - Да N - Нет\n>>>").upper()

            if user_input == "Y":
                self._price = new_price

            else:
                print("Операция отменена")

        else:
            self._price = new_price


class Category(BaseOrderCategory):
    """Класс, описывающий категорию"""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        super().__init__(name, description)
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        total_products = sum(product.quantity for product in self.__products)
        return f"{self.name}, {total_products} шт."

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию
        """
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

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


class Order(BaseOrderCategory):
    """Класс, описывающий заказ"""

    def __init__(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Количество товара в заказе должно быть положительным")
        if quantity > product.quantity:
            raise ValueError(f"Недостаточно товара на складе. Доступно: {product.quantity}")

        super().__init__(product.name, product.description)
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self) -> str:
        return f"Заказ: {self.name}, {self.quantity} шт., Итого: {self.total_price} руб."


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


class Smartphone(Product):
    """
    Класс, описывающий смартфон
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float | int,
        quantity: int,
        efficiency: int,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """
    Класс, описывающий газон
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float | int,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
