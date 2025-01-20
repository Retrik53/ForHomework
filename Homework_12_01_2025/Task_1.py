import pickle

class CountriesCapitals:
    def __init__(self):
        self.data = {}

    def add(self, country, capital):
        if country in self.data:
            print(f"Страна {country} уже существует.")
        else:
            self.data[country] = capital
            print(f"Добавлена новая запись: страна {country}, столица {capital}.")

    def remove(self, country):
        if country not in self.data:
            print(f"Страны {country} не найдено.")
        else:
            del self.data[country]
            print(f"Запись о стране {country} удалена.")

    def find_capital(self, country):
        if country not in self.data:
            return f"Страны {country} не найдено."
        else:
            return f"Столицей страны {country} является {self.data[country]}."

    def edit_capital(self, country, new_capital):
        if country not in self.data:
            print(f"Страны {country} не найдено.")
        else:
            old_capital = self.data[country]
            self.data[country] = new_capital
            print(f"Столица страны {country} изменена с {old_capital} на {new_capital}.")

    def show_all(self):
        for country, capital in self.data.items():
            print(f"{country}: {capital}")

    def save_data(self, filename="data.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self.data, file)
        print("Данные успешно сохранены.")

    def load_data(self, filename="data.pkl"):
        try:
            with open(filename, "rb") as file:
                self.data = pickle.load(file)
            print("Данные успешно загружены.")
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")


def main():
    cc = CountriesCapitals()
    while True:
        print("Меню:")
        print("1. Добавить страну и столицу")
        print("2. Удалить страну")
        print("3. Найти столицу по стране")
        print("4. Изменить столицу")
        print("5. Показать все страны и столицы")
        print("6. Сохранить данные")
        print("7. Загрузить данные")
        print("8. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            country = input("Введите название страны: ")
            capital = input("Введите название столицы: ")
            cc.add(country, capital)

        elif choice == '2':
            country = input("Введите название страны для удаления: ")
            cc.remove(country)

        elif choice == '3':
            country = input("Введите название страны для поиска столицы: ")
            result = cc.find_capital(country)
            print(result)

        elif choice == '4':
            country = input("Введите название страны для изменения столицы: ")
            new_capital = input("Введите новое название столицы: ")
            cc.edit_capital(country, new_capital)

        elif choice == '5':
            cc.show_all()

        elif choice == '6':
            cc.save_data()

        elif choice == '7':
            cc.load_data()

        elif choice == '8':
            break

        else:
            print("Неверный ввод. Попробуйте еще раз.")


if __name__ == "__main__":
    main()