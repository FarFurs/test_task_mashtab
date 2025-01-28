# Функция анализирует файл и возвращает товар с самой большой стоимостью
def analyze_sales_data(file_name) -> dict:
    max_price = -1
    result = {}

    with open(file_name, 'r',) as file:
        for line in file:
            date, time, category, name, price = line.split(",")
            price = float(price)

            if price > max_price:
                max_price = price
                result = {
                    'date': date,
                    'time': time,
                    'category': category,
                    'name': name,
                    'price': price
                }
    return result


def main() -> None:
    file_name = 'text.txt'
    result = analyze_sales_data(file_name)
    print(result)


if __name__ == "__main__":
    main()
