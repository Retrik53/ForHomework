"""Задание 8.1.1"""
# class Vehicle:
#     def __init__(self, name, mileage):
#         self.name = name
#         self.mileage = mileage
#
#     def get_vehicle_type(self, wheels_count):
#         if wheels_count == 2:
#             return f"Это мотоцикл марки {self.name}."
#         elif wheels_count == 3:
#             return f"Это трицикл марки {self.name}."
#         elif wheels_count == 4:
#             return f"Это автомобиль марки {self.name}."
#         else:
#             return "Я не знаю таких транспортных средств."
#
#     def get_vehicle_advice(self):
#         if self.mileage < 50_000:
#             return f"Неплохо, {self.name} можно брать.({self.mileage})"
#         elif 50_001 <= self.mileage <= 100_000:
#             return f"{self.name} надо внимательно проверить.({self.mileage})"
#         elif 100_001 <= self.mileage <= 150_000:
#             return f"{self.name} надо провести полную диагностику.({self.mileage})"
#         else:
#             return f"{self.name} лучше не покупать.({self.mileage})"
#
#
# vehicle1 = Vehicle("BMW", 30_000)
# vehicle2 = Vehicle("Audi", 75_000)
# vehicle3 = Vehicle("Honda", 120_000)
# vehicle4 = Vehicle("Toyota", 180_000)
#
#
# print(vehicle1.get_vehicle_type(2))
# print(vehicle2.get_vehicle_type(4))
# print(vehicle3.get_vehicle_type(5))
# print(vehicle4.get_vehicle_type(3))
# print("=======================")
# print(vehicle1.get_vehicle_advice())
# print(vehicle2.get_vehicle_advice())
# print(vehicle3.get_vehicle_advice())
# print(vehicle4.get_vehicle_advice())
#
# print("=======================")
# mark = input("Введите марку транспорта:")
# mileage = int(input("Введите пробег транспорта:"))
# wheels = int(input("Введите количество колес транспорта"))
#
# vehicle = Vehicle(mark, mileage)
#
# print(vehicle.get_vehicle_type(wheels))
# print("=======================")
# print(vehicle.get_vehicle_advice())

"""Задание 8.1.2"""
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def describe_book(self):
        print(f"Книга '{self.title}' написана автором {self.author}. В ней {self.pages} страниц")

    def recommend_book(self):
        if self.genre in ["Фантастика", "Роман"]:
            return f"Вам может понравиться книга '{self.title}'."
        else:
            return f"Попробуйте почитать книгу '{self.title}', возможно она вас заинтересует."


book1 = Book("1984", "Джордж Оруэлл", 328, "Антиутопия")
book2 = Book("Мастер и Маргарита", "Михаил Булгаков", 480, "Роман")

book1.describe_book()
book2.describe_book()

print(book1.recommend_book())
print(book2.recommend_book())

Title = input("Введите название книги")
Author = input("Введите имя Автора книги")
Pages = int(input("Введите количество страниц в книге"))
Genre = input("Введите жанр книги")

user_book = Book(Title, Author, Pages, Genre)

user_book.describe_book()

print(user_book.recommend_book())