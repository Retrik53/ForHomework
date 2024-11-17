"""Задача 5.1.1"""
# genres = ('Роман', 'Новелла', 'Фэнтези', 'Научная', 'Фантастика')
# numbers = (3, 7, 9, 1, 6, 8, 2, 5, 4)
#
# # Длина каждого кортежа
# print(f"длина кортежа с жанрами - {len(genres)}")
# print(f"длина кортежа с числами - {len(numbers)}")
#
# # Максимальный элемент
# print(f"максимальный элемент кортежа с жанрами - {max(genres)}")
# print(f"максимальный элемент кортежа с числами - {max(numbers)}")
#
# # Минимальный элемент
# print(f"Минимальный элемент кортежа с жанрами - {min(genres)}")
# print(f"Минимальный элемент кортежа с числами - {min(numbers)}")
#
# # Сумма элементов в кортеже
# print(f"сумма элементов кортежа с числами - {sum(numbers)}")
# # Кортеж с жанрами невозможно ссумировать так как строки сумме не поддаются
#
# # Сортировка кортежей
# genres_list = list(genres)
# genres_list.sort()
# print(f"Отсортированный кортеж с жанрами - {tuple(genres_list)}")
#
# numbers_list = list(numbers)
# numbers_list.sort()
# print(f"Отсортированный кортеж с цифрами - {tuple(numbers_list)}")

"""Задача 5.1.2"""
# cinema_genres = ("Комедия", "Экшн", "Пеплум", "Триллер")
# cinema_genres_list = list(cinema_genres)
# cinema_genres_list[1] = "Боевик"
# cinema_genres_list.insert(2, "Фэнтези")
# cinema_genres = tuple(cinema_genres_list)
# print(f"{cinema_genres}")
# print(f"преобразованные жанры кино: {", ".join([i for i in  cinema_genres])}")

"""Задача 5.1.3"""
my_list = {
    "Нож",
    "Спички",
    "Палатка",
    "Аптечка",
    "Рыболовные снасти",
    "Книга",
    "Компас",
    "Водонепроницаемая одежда",
    "Посуда",
    "Фонарик"
}
their_list = {
    "Вода",
    "Продукты питания",
    "Одежда",
    "Зеркало для подачи сигналов",
    "Веревка",
    "Топор",
    "Карманная рация",
    "Солнцезащитный крем",
    "Мачете",
    "Свисток",
    "Фонарик",
    "Компас",
    "Книга",
    "Нож"
}

common_items = my_list & their_list
print(f"Предметы, которые взяли бы вы оба: {common_items}")

only_your_items = my_list - their_list
print(f"Предметы, которые взяли бы только вы: {only_your_items}")

only_their_items = their_list - my_list
print(f"Предметы, которые взял бы только ваш близкий человек: {only_their_items}")

shared_items = my_list.intersection(their_list)
print(f"Предметы, которые есть и у вас, и у вашего близкого человека: {shared_items}")


"""Задача 5.1.4"""
# cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия", "пеплум"]
#
# # Преобразование списка в множество (убрались все повторяющиеся элементы)
# cinema_genres_set = set(cinema_genres)
# print(f"1. Список преобразован в множество {type(cinema_genres_set)}\n")
#
# # Добавлено 2 новых жанра
# cinema_genres_set.add("Боевик")
# cinema_genres_set.add("Научный")
# print(f"2. Добавлены 2 новых элемента в множество {cinema_genres_set} это - Боевик и Научный\n")
#
# # Удален 1 жанр (комедия)
# cinema_genres_set.remove("комедия")
# print(f"3. из множества {cinema_genres_set} удален элемент - Комедия\n")
#
# # Удален 1 СЛУЧАЙНЫЙ жанр
# random_deleted_element = cinema_genres_set.pop()
# print(f"4. из множества {cinema_genres_set} удален 1 случайный элемент - {random_deleted_element}\n")
#
# # Множество преобразовано обратно в список
# new_cinema_genres_list = list(cinema_genres_set)
# print(f"5. множество {cinema_genres_set} преобразован обратно в список {type(new_cinema_genres_list)}")
# print(f"\t\t{new_cinema_genres_list}")
