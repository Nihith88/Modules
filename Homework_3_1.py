"""
Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). В нем создайте функцию
создающую директории от dir_1 до dir_9 в папке из которой запущен данный код. Затем создайте вторую
функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.
"""

import sys, os

def add_fold():
    for i in range(1,10):
        os.mkdir(os.path.join(os.getcwd(), 'dir_{}' .format(i)))

# add_fold()

def rem_fold():
    for j in range(1, 10):
        os.rmdir('dir_{}' .format(j))

# rem_fold()