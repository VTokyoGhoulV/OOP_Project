import json
from pathlib import Path

from src.classes import Category, CategoryList, Product


def from_file_to_classes() -> CategoryList:
    """
    Преобразует данные из JSON файла в классы
    """

    with open(f"{find_project_root()}/data/products.json", "r", encoding="utf-8") as file:
        categories = json.load(file)

    category_list = CategoryList()

    for category in categories:
        product_list = list()

        for product in category["products"]:
            product_list.append(
                Product(product["name"], product["description"], product["price"], product["quantity"])
            )

        new_category = Category(category["name"], category["description"], product_list)
        category_list.append(new_category)

    return category_list


def find_project_root(marker_files: str | tuple = ("pyproject.toml", ".git", "requirements.txt")) -> Path:
    """
    Ищет корневую директорию проекта, поднимаясь по дереву папок,
    пока не найдет один из маркерных файлов/папок.
    """
    current_path = Path.cwd()  # Начинаем с текущей рабочей директории

    for parent in [current_path] + list(current_path.parents):
        for marker in marker_files:
            if (parent / marker).exists():
                return parent

    raise RuntimeError("Не удалось найти корень проекта. Убедитесь, что один из маркерных файлов присутствует.")
