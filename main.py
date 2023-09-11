import random
from tkinter import *
from tkinter import ttk

def input_num(text):
    """Возвращает целое число. Цикл работает до тех пор, пока не введут целое число"""
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Введите число!")

def math_operations(a, ops, b):
    """Возвращает результат арифметической операции: 'a','ops','b'"""
    if ops == "+":
        return a + b
    elif ops == "-":
        return a - b
    elif ops == "*":
        return a * b
    elif ops == "/":
        return a / b
    else:
        raise ValueError("Неподдерживаемая математическая операция")

total_score = 10
correct = 0
nums = range(1, 99)
for _ in range(total_score):
    ops = random.choice("+-*/")
    a, b = random.choices(nums, k=2)

    # Разрешается только целочисленный ввод
    # Поэтому деление ограниченно только целочисленными результатами
    # Цикл переворачивает a,b до тех пор, пока они не совпадут
    while ops == "/" and (a % b != 0 or a <= b):
        a, b = random.choices(nums, k=2)

    # убедиться, что значение не опускается ниже 0 для операции вычитания
    while ops == "-" and a < b:
        a, b = random.choices(nums, k=2)

    result = input_num("Чему равно {} {} {} = ".format(a, ops, b))

    # расчет правильного результата
    corr = math_operations(a, ops, b)
    if result == corr:
        correct += 1
        print("Правильно")
    else:
        print("Не правильно. Правильный ответ: {} {} {} = {}".format(a, ops, b, corr))

print("У вас {} из {} правильных ответов.".format(correct, total_score))