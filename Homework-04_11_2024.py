import random
from random import randint

# Модуль 4/1-1
# def show_quote(name):
#     print(f"“Don't compare yourself with anyone in this world...\nif you do so, you are insulting yourself.”\n{name.rjust(50, ' ')}")
#
# show_quote("Bill Gates")


# Модуль 4/1-2
# def even_nums(start, end):
#     for i in range(start, end + 1):
#         if i % 2 == 0:
#             print(i, end=', ')
#     print(f"- Четные числа в диапазоне от {start} до {end}")
#
# start = int(input("Начало диапазона"))
# end= int(input("Конец диапазона"))
# even_nums(start, end)

# Модуль 4/1-3
# def square(length, symbol, is_filled):
#     if bool(is_filled == 1) == False:
#         for i in range(length):
#             for j in range(length):
#                 if i == 0 or j == 0 or i == length - 1 or j == length - 1:
#                     print(symbol, end="")
#                 else:
#                     print(" ", end="")
#             print("")
#     elif bool(is_filled == 1) == True:
#         for i in range(length):
#             print(symbol * length)
#
# length = int(input("Введите длину стороны квадрата"))
# symbol = input("Введите любой символ из которого будет состоять квадрат")
# is_filled = int(input("Введите 1 - заполеннный квадрат/ 0 - пустой квадрат"))
# square(length, symbol, is_filled)

# Модуль 4/1-4
# def min_num(first, second, third, fourth, fifth):
#     num_list = []
#     num_list.append(first)
#     num_list.append(second)
#     num_list.append(third)
#     num_list.append(fourth)
#     num_list.append(fifth)
#     ans = min(num_list)
#     print(f"Все 5 чисел: {num_list}\nМинимальное из 5 чисел = {ans}")
#
# first = randint(1, 15)
# second = randint(1, 15)
# third = randint(1, 15)
# fourth = randint(1, 15)
# fifth = randint(1, 15)
# min_num(first, second, third, fourth, fifth)

# Модуль 4/1-5
# def product_in_range(start, end):
#     if start > end:
#         start, end = end, start
#     result = 1
#     for number in range(start, end + 1):
#         result *= number
#
#     print(f"произведением всех чисел от {start} до {end} = {result}")
#
# start = int(input("Введите начало диапазона"))
# end = int(input("Введите конец диапазона"))
# product_in_range(start, end)

# Модуль 4/1-6
# def quantity_of_nums(num):
#     if num < 0:
#         num = num * -1
#         quantity = len(str(num))
#     else:
#         quantity = len(str(num))
#     print(quantity)
#
# num = int(input("Введите любое число"))
# quantity_of_nums(num)

# Модуль 4/1-7
# def palindrome(num):
#     reverse_num = str(num)[::-1]
#     if reverse_num == str(num):
#         print(f"Число {num} палиндром? {bool(reverse_num == str(num))}")
#     else:
#         print(f"Число {num} палиндром? {bool(reverse_num == str(num))}")
#
# num = int(input("Введите любое число"))
# palindrome(num)
