# OOP Project

Учебный Python-проект для отработки объектно-ориентированного программирования на примере каталога товаров. Проект описывает товары, категории товаров и загрузку данных из JSON-файла в объекты Python.

## Возможности

- описание товара через класс `Product`;
- описание категории товаров через класс `Category`;
- хранение списка категорий через класс `CategoryList`;
- поиск категории по названию;
- получение списка названий всех категорий;
- вывод товаров внутри категории в текстовом формате;
- загрузка категорий и товаров из файла `data/products.json`;
- покрытие основной логики тестами на `pytest`.

## Стек

- Python `^3.14` согласно `pyproject.toml`;
- Poetry для управления проектом и dev-зависимостями;
- pytest / pytest-cov для тестирования;
- flake8, black, isort, mypy для контроля качества кода.

## Структура проекта

```text
OOP_Project/
├── data/
│   └── products.json        # исходные данные о категориях и товарах
├── src/
│   ├── __init__.py
│   ├── classes.py           # классы Product, Category, CategoryList
│   ├── main.py              # точка входа, сейчас не содержит логики
│   └── utils.py             # функции загрузки данных и поиска корня проекта
├── tests/
│   ├── __init__.py
│   ├── test_classes.py      # тесты классов
│   └── test_utils.py        # тесты утилит
├── .flake8                  # настройки flake8
├── pyproject.toml           # настройки проекта и инструментов
├── poetry.lock              # lock-файл Poetry
└── README.md
```

## Основные сущности

### `Product`

Класс товара.

Атрибуты:

- `name` — название товара;
- `description` — описание товара;
- `price` — цена товара;
- `quantity` — количество товара на складе.

### `Category`

Класс категории товаров.

Атрибуты экземпляра:

- `name` — название категории;
- `description` — описание категории;
- `products` — список объектов `Product`.

Атрибуты класса:

- `total_categories` — общее количество созданных категорий;
- `total_products` — общее количество товаров во всех созданных категориях.

Метод:

- `show_products()` — возвращает строку со списком товаров категории в формате:

```text
Название - Описание - Цена - Количество
```

### `CategoryList`

Класс-контейнер для работы со списком категорий.

Методы:

- `append(category)` — добавляет категорию в список;
- `find_by_name(name)` — возвращает категорию по названию или `None`, если категория не найдена;
- `get_all_categories_names()` — возвращает список названий всех категорий.

## Формат данных

Исходные данные хранятся в `data/products.json`.

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

Функция `from_file_to_classes()` из модуля `src.utils` читает этот файл и преобразует данные в объекты `CategoryList`, `Category` и `Product`.

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

`--no-root` используется, потому что проект сейчас не настроен как устанавливаемый пакет с отдельной package-конфигурацией.

### Вариант 2: через venv и pip

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

pip install pytest pytest-cov flake8 black isort mypy
```

## Пример использования

Запустите пример из корня проекта:

```bash
poetry run python -c "from src.utils import from_file_to_classes; cl = from_file_to_classes(); print(cl.get_all_categories_names())"
```

Пример использования в коде:

```python
from src.utils import from_file_to_classes

category_list = from_file_to_classes()

print(category_list.get_all_categories_names())

category = category_list.find_by_name("Смартфоны")

if category:
    print(category.show_products())
```

Ожидаемый результат для текущего `products.json`:

```text
['Смартфоны', 'Телевизоры']
Samsung Galaxy C23 Ultra - 256GB, Серый цвет, 200MP камера - 180000.0 - 5
Iphone 15 - 512GB, Gray space - 210000.0 - 8
Xiaomi Redmi Note 11 - 1024GB, Синий - 31000.0 - 14
```

## Тестирование

Запуск всех тестов:

```bash
poetry run pytest
```

Краткий запуск:

```bash
poetry run pytest -q
```

Запуск тестов с отчетом о покрытии:

```bash
poetry run pytest --cov=src --cov-report=term-missing
```

Генерация HTML-отчета о покрытии:

```bash
poetry run pytest --cov=src --cov-report=html
```

После этого отчет будет доступен в папке `htmlcov/`.

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

Статическая типизация:

```bash
poetry run mypy src
```

## Текущий статус

- Основные классы реализованы в `src/classes.py`.
- Загрузка данных из JSON реализована в `src/utils.py`.
- Точка входа `src/main.py` пока не содержит прикладного сценария запуска.
- Тесты находятся в папке `tests/`.

## Возможные направления развития

- добавить валидацию цены и количества товара;
- добавить методы создания товаров и категорий из словарей;
- реализовать сохранение данных обратно в JSON;
- добавить CLI-интерфейс в `src/main.py`;
- расширить модель товаров: скидки, артикулы, остатки по складам;
- настроить проект как полноценный installable package.
