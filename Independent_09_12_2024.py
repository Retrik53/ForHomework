"""Задача 8.1"""
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def length(self):
#         return 2 * 3.14 * self.radius
#
#     def CircleArea(self):
#         return 3.14 * self.radius ** 2
#
# class Square:
#     def __init__(self, diameter):
#         # Диаметр квадрата равен удвоенной стороне
#         self.side_length = diameter
#
#     def side(self):
#         return self.side_length
#
#     def SquareArea(self):
#         return self.side_length ** 2
#
# class Circle_in_square(Circle, Square):
#     def __init__(self, radius):
#         super().__init__(radius)
#         diameter = 2 * radius
#         Square.__init__(self, diameter)
#
# circle_in_square = Circle_in_square(radius=5)
#
# print(f"Радиус окружности: {circle_in_square.radius}")
# print(f"Длина окружности: {circle_in_square.length():.2f}")
# print(f"Площадь окружности: {circle_in_square.CircleArea():.2f}")
#
# print(f"Сторона квадрата: {circle_in_square.side()}")
# print(f"Площадь квадрата: {circle_in_square.SquareArea():.2f}")

"""Задача 8.2"""
# class Wheel:
#     def __init__(self, size, material):
#         self._size = size
#         self._material = material
#
#     @property
#     def size(self):
#         return self._size
#
#     @property
#     def material(self):
#         return self._material
#
# class Engine:
#     def __init__(self, power, type):
#         self._power = power
#         self._type = type
#
#     @property
#     def power(self):
#         return self._power
#
#     @property
#     def type(self):
#         return self._type
#
#     @type.setter
#     def type(self, new_type):
#         self._type = new_type
#
# class Door:
#     def __init__(self, color, is_open=False):
#         self._color = color
#         self._is_open = is_open
#
#     @property
#     def color(self):
#         return self._color
#
#     @property
#     def is_open(self):
#         return self._is_open
#
# class Car:
#     def __init__(
#             self,
#             wheel_size=16,
#             wheel_material="Резина",
#             engine_power=150,
#             engine_type="Бензиновый",
#             door_color="Черный"
#     ):
#         self.wheels = [Wheel(wheel_size, wheel_material) for _ in range(4)]
#         self.engine = Engine(engine_power, engine_type)
#         self.doors = [Door(door_color) for _ in range(4)]
#
#     def open_door(self, index):
#         if 0 <= index < len(self.doors):
#             self.doors[index]._is_open = True
#
#     def close_door(self, index):
#         if 0 <= index < len(self.doors):
#             self.doors[index]._is_open = False
#
#     def change_engine_type(self, new_type):
#         self.engine.type = new_type
#
# car = Car()
#
# print("Размер колеса:", car.wheels[0].size)
# print("Материал колеса:", car.wheels[0].material)
# print("Мощность двигателя:", car.engine.power)
# print("Тип двигателя:", car.engine.type)
# print("Цвет двери:", car.doors[0].color)
#
# car.open_door(0)
# print("Открыта ли дверь?", car.doors[0].is_open)
#
# car.close_door(0)
# print("Открыта ли дверь?", car.doors[0].is_open)
#
# # Изменим тип двигателя
# car.change_engine_type("Электрический")
# print("Новый тип двигателя:", car.engine.type)

"""Задача 8.3"""
# class DomesticAnimal:
#     def __init__(self, name, sound, animal_type):
#         self._name = name
#         self._sound = sound
#         self._animal_type = animal_type
#
#     def get_sound(self):
#         print(f"{self._name} говорит: {self._sound}")
#
#     def get_name(self):
#         print(f"Имя этого домашнего животного: {self._name}")
#
#     def get_type(self):
#         print(f"Это {self._animal_type}.")
#
# class Dog(DomesticAnimal):
#     def __init__(self, name, breed=None):
#         super().__init__(name, "Гав!", "Собака")
#         self._breed = breed
#
#     def get_breed(self):
#         if self._breed:
#             print(f"Порода этой собаки: {self._breed}")
#         else:
#             print("У этой собаки нет определенной породы.")
#
# class Cat(DomesticAnimal):
#     def __init__(self, name, fur_color=None):
#         super().__init__(name, "Мяу!", "Кошка")
#         self._fur_color = fur_color
#
#     def get_fur_color(self):
#         if self._fur_color:
#             print(f"Цвет шерсти этой кошки: {self._fur_color}")
#         else:
#             print("У этой кошки неизвестен цвет шерсти.")
#
# class Parrot(DomesticAnimal):
#     def __init__(self, name, species=None):
#         super().__init__(name, "Чирик-чирик!", "Попугай")
#         self._species = species
#
#     def get_species(self):
#         if self._species:
#             print(f"Вид этого попугая: {self._species}")
#         else:
#             print("Вид этого попугая не определен.")
#
# class Hamster(DomesticAnimal):
#     def __init__(self, name, coat_color=None):
#         super().__init__(name, "Писк-писк!", "Хомяк")
#         self._coat_color = coat_color
#
#     def get_coat_color(self):
#         if self._coat_color:
#             print(f"Цвет шерстки этого хомячка: {self._coat_color}")
#         else:
#             print("Цвет шерстки этого хомячка неизвестен.")
#
# dog = Dog("Шарик", "Такса")
# cat = Cat("Васька", "Рыжий")
# parrot = Parrot("Кеша", "Жако")
# hamster = Hamster("Пушок", "Серый")
#
# dog.get_name()
# dog.get_sound()
# dog.get_type()
# dog.get_breed()
# print("===========================")
# cat.get_name()
# cat.get_sound()
# cat.get_type()
# cat.get_fur_color()
# print("===========================")
# parrot.get_name()
# parrot.get_sound()
# parrot.get_type()
# parrot.get_species()
# print("===========================")
# hamster.get_name()
# hamster.get_sound()
# hamster.get_type()
# hamster.get_coat_color()

"""Задача 8.4"""
# class Employer:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def print_info(self):
#         print(f"Это работник: {self.first_name} {self.last_name}, Возраст: {self.age}")
#
# class President(Employer):
#     def __init__(self, first_name, last_name, age, company):
#         super().__init__(first_name, last_name, age)
#         self.company = company
#
#     def print_info(self):
#         print(f"Президент - {self.company}: {self.first_name} {self.last_name}, Возраст: {self.age}")
#
# class Manager(Employer):
#     def __init__(self, first_name, last_name, age, department):
#         super().__init__(first_name, last_name, age)
#         self.department = department
#
#     def print_info(self):
#         print(f"Менеджер - {self.department}: {self.first_name} {self.last_name}, Возраст: {self.age}")
#
# class Worker(Employer):
#     def __init__(self, first_name, last_name, age, position):
#         super().__init__(first_name, last_name, age)
#         self.position = position
#
#     def print_info(self):
#         print(f"Работник на позиции - {self.position}: {self.first_name} {self.last_name}, Возраст: {self.age}")
#
# president = President("Семен", "Петрович", 50, "Корпорация АКМЕ")
# manager = Manager("Анна", "Павловна", 40, "Маркетинг")
# worker = Worker("Борис", "Дмитриевич", 30, "Разработчик")
#
# president.print_info()
# manager.print_info()
# worker.print_info()

"""Задача 8.5"""
class Employer:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_info(self):
        print(f"Это сотрудник: {self.first_name} {self.last_name}, Возраст: {self.age}")

    def __str__(self):
        return f"Сотрудник: {self.first_name} {self.last_name}"

    def __int__(self):
        return self.age

class President(Employer):
    def __init__(self, first_name, last_name, age, company):
        super().__init__(first_name, last_name, age)
        self.company = company

    def print_info(self):
        print(f"Президент - {self.company}: {self.first_name} {self.last_name}, Возраст: {self.age}")

    def __str__(self):
        return f"Президент: {self.first_name} {self.last_name} ({self.company})"

    def __int__(self):
        return self.age

class Manager(Employer):
    def __init__(self, first_name, last_name, age, department):
        super().__init__(first_name, last_name, age)
        self.department = department

    def print_info(self):
        print(f"Менеджер - {self.department}: {self.first_name} {self.last_name}, Возраст: {self.age}")

    def __str__(self):
        return f"Менеджер: {self.first_name} {self.last_name} ({self.department})"

    def __int__(self):
        return self.age

class Worker(Employer):
    def __init__(self, first_name, last_name, age, position):
        super().__init__(first_name, last_name, age)
        self.position = position

    def print_info(self):
        print(f"Работник на позиции - {self.position}: {self.first_name} {self.last_name}, Возраст: {self.age}")

    def __str__(self):
        return f"Работник: {self.first_name} {self.last_name} ({self.position})"

    def __int__(self):
        return self.age

president = President("Семен", "Петрович", 50, "Корпорация АКМЕ")
manager = Manager("Анна", "Павловна", 40, "Маркетинг")
worker = Worker("Борис", "Дмитриевич", 30, "Разработчик")

print(president)
print(f"Возраст: {int(president)}")

print(manager)
print(f"Возраст: {int(manager)}")

print(worker)
print(f"Возраст: {int(worker)}")
