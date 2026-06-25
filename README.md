# OOP Project

Учебный Python-проект для отработки объектно-ориентированного программирования на примере каталога товаров интернет-магазина.

Проект демонстрирует работу с классами, наследованием, абстрактными базовыми классами, миксинами, инкапсуляцией, свойствами, магическими методами, итераторами, загрузкой данных из JSON и тестированием бизнес-логики.

## Содержание

- [Возможности](#возможности)
- [Стек](#стек)
- [Структура проекта](#структура-проекта)
- [Основные сущности](#основные-сущности)
- [Формат данных](#формат-данных)
- [Установка](#установка)
- [Пример использования](#пример-использования)
- [Тестирование](#тестирование)
- [Проверка качества кода](#проверка-качества-кода)
- [Особенности реализации](#особенности-реализации)

## Возможности

- создание товаров через класс `Product`;
- хранение цены товара во внутреннем атрибуте `_price`;
- получение и изменение цены через свойство `price`;
- защита от установки нулевой или отрицательной цены;
- подтверждение снижения цены через ввод пользователя;
- создание товара из словаря через `Product.new_product()`;
- объединение одинаковых товаров по названию:
  - количество товара суммируется;
  - цена обновляется только при передаче более высокой цены;
- строковое представление товара через `__str__()`;
- сложение полной стоимости товарных остатков через `__add__()`;
- создание категорий товаров через класс `Category`;
- хранение товаров категории в приватном списке `__products`;
- добавление товара в категорию через `add_product()`;
- подсчёт количества созданных категорий и добавленных товаров через атрибуты класса;
- строковое представление категории с общим количеством единиц товара на складе;
- получение товаров категории в текстовом формате через свойство `products`;
- доступ к списку объектов товаров через свойство `products_list`;
- работа со списком категорий через класс `CategoryList`;
- поиск категории по названию;
- получение списка названий всех категорий;
- перебор товаров категории через итератор `GetProduct`;
- оформление заказа через класс `Order`;
- проверка корректности количества товара в заказе;
- расчёт итоговой стоимости заказа;
- расширение базового класса товара через наследников:
  - `Smartphone`;
  - `LawnGrass`;
- использование абстрактных классов:
  - `BaseProduct`;
  - `BaseOrderCategory`;
- использование миксина `InitMixin` для вывода информации о созданном объекте;
- загрузка категорий и товаров из файла `data/products.json`;
- автоматический поиск корня проекта через `find_project_root()`;
- покрытие основной логики тестами на `pytest`.

## Стек

- Python `^3.14` согласно `pyproject.toml`;
- Poetry для управления проектом и группами зависимостей;
- pytest для тестирования;
- pytest-cov для проверки покрытия тестами;
- flake8 для проверки стиля кода;
- black для форматирования;
- isort для сортировки импортов;
- mypy для статической проверки типов.

## Структура проекта

```text
OOP_Project/
├── data/
│   └── products.json        # исходные данные о категориях и товарах
├── src/
│   ├── __init__.py
│   ├── classes.py           # основные классы проекта
│   └── utils.py             # загрузка данных и поиск корня проекта
├── tests/
│   ├── __init__.py
│   ├── test_classes.py      # тесты классов
│   └── test_utils.py        # тесты утилит
├── main.py                  # точка входа, пока без прикладной логики
├── .flake8                  # настройки flake8
├── pyproject.toml           # настройки проекта, Poetry и инструментов
├── poetry.lock              # lock-файл Poetry
└── README.md
```

Служебные папки и файлы вроде `.git/`, `.idea/`, `.pytest_cache/`, `.mypy_cache/`, `.coverage` и `htmlcov/` могут присутствовать в рабочей директории, но не относятся к основной логике проекта.

## Основные сущности

### `BaseProduct`

Абстрактный базовый класс для товаров.

Он задаёт общий интерфейс и требует реализации конструктора с параметрами:

| Параметр | Описание |
|---|---|
| `name` | название товара |
| `description` | описание товара |
| `price` | цена товара |
| `quantity` | количество товара на складе |

Создать экземпляр `BaseProduct` напрямую нельзя, потому что класс является абстрактным.

### `BaseOrderCategory`

Абстрактный базовый класс для сущностей, которым нужны `name` и `description`.

В проекте от него наследуются:

- `Category`;
- `Order`.

### `InitMixin`

Миксин, который выводит в консоль название класса и аргументы, с которыми был создан объект.

Например, при создании товара:

```python
product = Product("Apple", "Simple apple", 50, 100)
```

в консоль будет выведена строка вида:

```text
Product('Apple', 'Simple apple', 50, 100)
```

### `Product`

Класс, описывающий товар.

Атрибуты экземпляра:

| Атрибут | Описание |
|---|---|
| `name` | название товара |
| `description` | описание товара |
| `price` | цена товара, доступ через property |
| `quantity` | количество товара на складе |

Внутренние и классовые атрибуты:

| Атрибут | Описание |
|---|---|
| `_price` | внутреннее хранение цены товара |
| `_all_products` | общий список всех созданных товаров |

Методы и магические методы:

| Метод | Назначение |
|---|---|
| `__str__()` | возвращает строку вида `Название, цена руб. Остаток: количество шт.` |
| `__add__(other)` | складывает полную стоимость остатков двух товаров совместимого типа |
| `new_product(product_params)` | создаёт новый товар или обновляет уже существующий товар с таким же названием |

Особенности свойства `price`:

- если новая цена `<= 0`, значение не меняется и выводится сообщение `Цена не должна быть нулевая или отрицательная`;
- если новая цена ниже текущей, требуется подтверждение пользователя через ввод `Y`;
- если пользователь вводит не `Y`, операция отменяется;
- если новая цена выше текущей, значение меняется сразу.

Пример:

```python
from src.classes import Product

product = Product("Apple", "Simple apple", 50, 100)

print(product)
print(product.price)

product.price = 60
print(product.price)
```

Пример результата:

```text
Product('Apple', 'Simple apple', 50, 100)
Apple, 50 руб. Остаток: 100 шт.
50
60
```

### `Product.new_product()`

Метод класса для создания товара из словаря.

Если товар с таким же названием уже есть во внутреннем списке `_all_products`, новый объект не создаётся. Вместо этого:

- количество существующего товара увеличивается;
- цена заменяется только в том случае, если новая цена выше текущей;
- возвращается уже существующий объект.

Пример:

```python
from src.classes import Product

product_1 = Product.new_product(
    {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
)

product_2 = Product.new_product(
    {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 190000.0,
        "quantity": 5,
    }
)

print(product_1)
print(product_1 is product_2)
```

Пример результата:

```text
Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)
Samsung Galaxy S23 Ultra, 190000.0 руб. Остаток: 10 шт.
True
```

### `Category`

Класс, описывающий категорию товаров.

Атрибуты экземпляра:

| Атрибут | Описание |
|---|---|
| `name` | название категории |
| `description` | описание категории |
| `products` | строковое представление товаров категории |
| `products_list` | список объектов `Product` |

Атрибуты класса:

| Атрибут | Описание |
|---|---|
| `category_count` | количество созданных категорий |
| `product_count` | количество товаров, переданных в категории и добавленных через `add_product()` |

Методы и свойства:

| Метод / свойство | Назначение |
|---|---|
| `__str__()` | возвращает название категории и общее количество единиц товара на складе |
| `add_product(product)` | добавляет объект `Product` в категорию |
| `products` | возвращает товары категории одной строкой |
| `products_list` | возвращает список объектов товаров |

Пример:

```python
from src.classes import Category, Product

apple = Product("Apple", "Simple apple", 50, 100)
phone = Product("Phone", "Simple phone", 500, 10)

category = Category("Товары", "Разные товары", [apple])
category.add_product(phone)

print(category)
print(category.products)
```

Пример результата:

```text
Product('Apple', 'Simple apple', 50, 100)
Product('Phone', 'Simple phone', 500, 10)
Товары, 110 шт.
Apple, 50 руб. Остаток: 100 шт.
Phone, 500 руб. Остаток: 10 шт.
```

### `Order`

Класс, описывающий заказ одного товара.

При создании заказа проверяется количество товара:

- количество должно быть больше `0`;
- количество не должно превышать остаток товара на складе.

Атрибуты экземпляра:

| Атрибут | Описание |
|---|---|
| `product` | объект товара |
| `quantity` | количество товара в заказе |
| `total_price` | итоговая стоимость заказа |
| `name` | название товара, полученное из `product.name` |
| `description` | описание товара, полученное из `product.description` |

Пример:

```python
from src.classes import Order, Product

product = Product("Apple", "Simple apple", 50, 100)
order = Order(product, 5)

print(order)
print(order.total_price)
```

Пример результата:

```text
Product('Apple', 'Simple apple', 50, 100)
Заказ: Apple, 5 шт., Итого: 250 руб.
250
```

### `CategoryList`

Класс-контейнер для работы со списком категорий.

Методы:

| Метод | Назначение |
|---|---|
| `append(category)` | добавляет категорию в список |
| `find_by_name(name)` | возвращает категорию по названию или `None` |
| `get_all_categories_names()` | возвращает список названий всех категорий |

Пример:

```python
from src.classes import Category, CategoryList, Product

apple = Product("Apple", "Simple apple", 50, 100)
category = Category("Фрукты", "Свежие фрукты", [apple])

category_list = CategoryList()
category_list.append(category)

print(category_list.get_all_categories_names())
print(category_list.find_by_name("Фрукты"))
```

### `GetProduct`

Итератор для последовательного перебора товаров внутри категории.

Пример:

```python
from src.classes import Category, GetProduct, Product

apple = Product("Apple", "Simple apple", 50, 100)
phone = Product("Phone", "Simple phone", 500, 10)

category = Category("Товары", "Разные товары", [apple, phone])

for product in GetProduct(category):
    print(product, end="")
```

Пример результата:

```text
Product('Apple', 'Simple apple', 50, 100)
Product('Phone', 'Simple phone', 500, 10)
Apple, 50 руб. Остаток: 100 шт.
Phone, 500 руб. Остаток: 10 шт.
```

### `Smartphone`

Класс-наследник `Product`, описывающий смартфон.

Дополнительные атрибуты:

| Атрибут | Описание |
|---|---|
| `efficiency` | производительность |
| `model` | модель |
| `memory` | объём памяти |
| `color` | цвет |

Пример:

```python
from src.classes import Smartphone

phone = Smartphone(
    "Apple",
    "Simple apple",
    50,
    100,
    10,
    "iPhone",
    128,
    "Black",
)

print(phone.model)
print(phone.memory)
```

### `LawnGrass`

Класс-наследник `Product`, описывающий газонную траву.

Дополнительные атрибуты:

| Атрибут | Описание |
|---|---|
| `country` | страна-производитель |
| `germination_period` | срок прорастания |
| `color` | цвет |

Пример:

```python
from src.classes import LawnGrass

grass = LawnGrass(
    "Grass",
    "Simple grass",
    50,
    100,
    "Russia",
    10,
    "Green",
)

print(grass.country)
print(grass.germination_period)
```

## Формат данных

Исходные данные хранятся в файле `data/products.json`.

Пример структуры:

```json
[
  {
    "name": "Смартфоны",
    "description": "Описание категории",
    "products": [
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      }
    ]
  }
]
```

Функция `from_file_to_classes()` из модуля `src.utils` читает `data/products.json` и преобразует данные в объекты:

```text
JSON -> CategoryList -> Category -> Product
```

Текущая загрузка из JSON создаёт объекты базового класса `Product`. Подклассы `Smartphone` и `LawnGrass` создаются вручную в коде.

## Установка

### Вариант 1: через Poetry

Клонируйте репозиторий и перейдите в папку проекта:

```bash
git clone <repository-url>
cd OOP_Project
```

Установите зависимости для разработки:

```bash
poetry install --no-root --with dev,lint
```

`--no-root` используется, потому что проект сейчас не настроен как устанавливаемый пакет.

### Вариант 2: через venv и pip

```bash
python -m venv .venv
source .venv/bin/activate
# Для Windows:
# .venv\Scripts\activate

pip install pytest pytest-cov flake8 black isort mypy
```

## Пример использования

Команды нужно выполнять из корня проекта `OOP_Project`.

Получить список категорий из `data/products.json`:

```bash
poetry run python -c "from src.utils import from_file_to_classes; cl = from_file_to_classes(); print(cl.get_all_categories_names())"
```

Пример использования в коде:

```python
from src.classes import GetProduct
from src.utils import from_file_to_classes

category_list = from_file_to_classes()

print(category_list.get_all_categories_names())

category = category_list.find_by_name("Смартфоны")

if category:
    print(category)
    print(category.products)

    for product in GetProduct(category):
        print(product, end="")
```

Ожидаемый результат для текущего `products.json`:

```text
Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)
Product('Iphone 15', '512GB, Gray space', 210000.0, 8)
Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
Product('55" QLED 4K', 'Фоновая подсветка', 123000.0, 7)
['Смартфоны', 'Телевизоры']
Смартфоны, 27 шт.
Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.
Iphone 15, 210000.0 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.
Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.
Iphone 15, 210000.0 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.
```

Товары выводятся дважды, потому что сначала используется свойство `category.products`, а затем итератор `GetProduct`.

## Тестирование

Запуск всех тестов:

```bash
poetry run pytest
```

Краткий запуск:

```bash
poetry run pytest -q
```

Запуск тестов с отчётом о покрытии:

```bash
poetry run pytest --cov=src --cov-report=term-missing
```

Генерация HTML-отчёта о покрытии:

```bash
poetry run pytest --cov=src --cov-report=html
```

После генерации HTML-отчёт будет доступен в папке `htmlcov/`.

В проекте есть тесты для:

- инициализации `Product`;
- создания товара через `new_product()`;
- обновления существующего товара;
- строкового представления товара;
- сложения товаров;
- обработки ошибки сложения с объектом неправильного типа;
- инициализации `Category`;
- добавления товара в категорию;
- обработки ошибки добавления объекта неправильного типа;
- работы свойства `products`;
- работы свойства `price`;
- проверки отрицательной, нулевой, пониженной и повышенной цены;
- строкового представления категории;
- работы `CategoryList`;
- работы итератора `GetProduct`;
- инициализации `Smartphone`;
- инициализации `LawnGrass`;
- проверки абстрактного класса `BaseProduct`;
- проверки наследования `Product` от `BaseProduct`;
- инициализации `Order`;
- проверки ошибок при создании заказа с некорректным количеством;
- строкового представления заказа;
- загрузки данных из JSON;
- ошибки поиска корня проекта.

## Проверка качества кода

Форматирование кода:

```bash
poetry run black src tests
```

Сортировка импортов:

```bash
poetry run isort src tests
```

Проверка стиля:

```bash
poetry run flake8 src tests
```

Статическая проверка типов:

```bash
poetry run mypy src
```

## Особенности реализации

- Основная логика находится в `src/classes.py`.
- Загрузка данных из JSON реализована в `src/utils.py`.
- `main.py` пока не содержит пользовательского сценария запуска.
- Тесты находятся в папке `tests/`.
- `Product._all_products` хранит созданные товары на уровне класса.
- `Product.new_product()` ищет совпадение по названию товара.
- `Product._price` используется как внутреннее хранилище цены.
- `Category.__products` скрыт от прямого доступа и доступен через свойства.
- `Category.product_count` считает количество объектов товаров, а не сумму их остатков на складе.
- `Category.__str__()` считает именно сумму остатков товаров в категории.
- `Order` работает с одним товаром и одним количеством товара.
- `find_project_root()` ищет корень проекта по маркерам `pyproject.toml`, `.git` или `requirements.txt`.
