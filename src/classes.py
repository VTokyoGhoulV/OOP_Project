class Product:
    """
    Класс, описывающий товар
    """

    def __init__(self, name: str, description: str, price: int, quantity: int):
        self.name: str = name
        self.description: str = description
        self.price: int = price
        self.quantity: int = quantity


class Category:
    """
    Класс, описывающий категорию
    """

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        self.name: str = name
        self.description: str = description
        self.products: list = products

        Category.category_count += 1
        Category.product_count += len(products)

    def show_products(self) -> str:
        """
        Возвращает информацию по всем продуктам в категории
        """

        return "\n".join(
            f"{product.name} - {product.description} - {product.price} - {product.quantity}"
            for product in self.products
        )


class CategoryList:
    """
    Класс, описывающий список категорий
    """

    def __init__(self) -> None:
        self.categories: list = list()

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

                return category  # type: ignore

        return None

    def get_all_categories_names(self) -> list:
        """
        Возвращает список имен всех категорий в списке
        """

        names = list()

        for category in self.categories:
            names.append(category.name)

        return names
