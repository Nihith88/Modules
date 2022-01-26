"""
Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
И получить объект: словарь из предыдущего задания.
"""
import pickle, json

with open('group.pickle', 'rb') as pf:
    new_list_p = pickle.load(pf)
print(new_list_p)
print(type(new_list_p))

with open('group.json', 'r', encoding='utf-8') as jf:
    new_list_j = json.load(jf)

print(new_list_j)
print(type(new_list_j))