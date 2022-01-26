"""
 Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы
 С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
 Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.
"""
import pickle, json

fav_band = {'name': 'Гробовая доска', 'tracks': ['Нож', 'Бык! ЧО?', 'Дайте водки'],
            'albums': [{'name': 'Порча', 'year': 2014, 'songs': ['Труп в плацкарте', 'Нож', 'Передозировка']},
                       {'name': 'По душу пьяницы', 'year': 2017, 'songs': ['Акчибаш', 'Партак', 'Дате водки']}]}
pick_band = pickle.dumps(fav_band)  # Сериализация pickle
print(pick_band)
print(type(pick_band))

js_band = json.dumps(fav_band)
print(js_band)
print(type(js_band))

with open('group.pickle', 'wb') as pf:  # Откроем файл для редактирования
    pickle.dump(fav_band, pf)  # Запишем в него

with open('group.json', 'w', encoding='utf-8') as jf:  # Откроем файл для записи
    json.dump(fav_band, jf)  # И запишем в него результат json
