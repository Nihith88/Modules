"""
Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле
"""

from random import choice


def rand_el(my_list):
    if my_list:
        return choice(my_list)
