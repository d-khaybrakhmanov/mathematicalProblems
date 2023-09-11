from tkinter import *
from tkinter import ttk


def input_num(text):
    """
    Возвращает целое число. Цикл работает до тех пор, пока не введут целое число
    """
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Введите число!")

# создание окна
root = Tk()
root.title("Решение математических примеров")
root.geometry("350x200+500+300")





root.mainloop()