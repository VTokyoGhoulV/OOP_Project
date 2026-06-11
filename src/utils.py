from locale import currency

from src.classes import Product, Category, CategoryList

import json

def from_file_to_classes():
    with open ("../data/products.json", "r", encoding="utf-8") as file:
        categories = json.load(file)

    category_list = CategoryList()

    for category in categories:
        product_list = list()

        for product in category["products"]:
            product_list.append(Product(product["name"], product["description"], product["price"], product["quantity"]))

        new_category = Category(category["name"], category["description"], product_list)
        category_list.append(new_category)

    return category_list
