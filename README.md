# Программа для поиска товара с максимальной ценой

Эта программа предназначена для поиска товара с самой высокой ценой из текстового файла, содержащего информацию о товарах. Каждый товар представлен строкой, включающей дату, категорию, имя товара и цену, разделенные запятой.

Программа включает:

- Чтение данных из текстового файла с товарами.
- Нахождение товара с самой высокой ценой.
- Возврат информации о товаре с максимальной ценой в виде словаря.

---

## Требования

- Python 3.x.
- Для работы программы используется стандартная библиотека Python.

---

## Формат входного файла

Файл должен быть текстовым `.txt` и иметь следующий формат:
<дата>,<время>,<категория>,<имя товара>,<цена>

Каждая строка должна содержать информацию о товаре, разделенную запятыми, где:

- **дата** — дата записи в формате `YYYY-MM-DD`.
- **категория** — категория товара.
- **имя товара** — название товара.
- **цена** — цена товара в целочисленном формате.

---

## Как запустить программу

1. **Склонировать репозиторий**:

    Для начала склонируйте репозиторий с программой:

    ```bash
    git clone https://github.com/yourusername/price-finder.git
    cd price-finder
    ```

2. **Подготовить файл с товарами**:
   
   Создайте текстовый файл с данными о товарах в формате, описанном выше. Пример файла может быть сохранен как `products.txt`.

3. **Запуск программы**:

   Внесите путь к вашему файлу в программу и запустите ее. Пример вызова функции:

    ```python
    find_max_price_product_from_txt('path_to_your_file.txt')
    ```

   Эта функция вернет словарь с информацией о товаре с самой высокой ценой, например:

    ```python
    {
        'дата': '2025-01-26',
        'категория': 'электроника',
        'имя товара': 'Ноутбук',
        'цена': 70000
    }
    ```

---

## Тестирование

Программа включает модульные тесты с использованием библиотеки `unittest`. Для тестирования создается временный файл с данными. Воспользуйтесь следующими шагами для запуска тестов:

1. Убедитесь, что у вас установлены все зависимости (если они требуются).
2. Для запуска тестов выполните команду:

    ```bash
    python -m unittest test_file.py
    ```

Тесты проверят, что функция правильно находит товар с максимальной ценой.

---

## Результат работы программы:

```python
{
    'дата': '2025-01-26',
    'категория': 'электроника',
    'имя товара': 'Ноутбук',
    'цена': 70000
}
:

