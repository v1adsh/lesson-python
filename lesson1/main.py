# from random import randint
#
# input_user = input("Select number: ")
#
# sys_num = randint(1, 5)
#
# if int(input_user) == int(sys_num):
#     print("Congratulation!")
# else:
#     print("Fail")
#
# print(sys_num)

# age = input('Enter your age: ')
#
# print(f'Your age is: {age}')

#КАЛЬКУЛЯТОР

# import math
#
# a = input('Введите первое число: ')
# b = input('Введите второе число: ')
# operand = input('Выберите математическую операцию: "+" - сложение, "-" - вычитание, "*" - умножение, "/" - деление: ')
#
# if operand == "+":
#     result = int(a) + int(b)
#     print(result)
# elif operand == "-":
#     result = int(a) - int(b)
#     print(result)
# elif operand == "*":
#     result = int(a) * int(b)
#     print(result)
# elif operand == "/":
#     result = int(a) / int(b)
#     print(result)
# else:
#     print('Ошибка')

from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.BLACK + Back.WHITE + 'some text')