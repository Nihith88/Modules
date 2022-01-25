"""
Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле
"""

from random import choice

my_list = []

def rand_el(my_list):
    if len(my_list) == 0:
        el = None
    else:
        return choice(my_list)