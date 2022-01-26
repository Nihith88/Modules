"""
Формат .json (javascript object notation) - текстовый формат обмена данными, основанный на JS.
Применяется для хранения и передачи данных. Чаще всего применяется в веб-разработке (для http)
dump - преобразование объекта в формате json в файл
dumps - преобразование объекта в json (в текст)
load - загрузка объекта из файла
loads - загрузка объекта из формата json (строки)
"""
import json

users = [{'name': "Alex", 'age': 32, 'phones': [56785, 32456], 'hascar': True},
         {'name': 'Kate', 'age': 27, 'phones': [2356, 2466], 'hascar': False}]
print(users)
js_friends = json.dumps(users) # Преобразование объекта (в текст)
print(js_friends)
nojs_friends = json.loads(js_friends) # Преобразуем обратно в объект
print(nojs_friends)