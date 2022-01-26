"""
Генераторы - применяются для заполнения списков или словарей. Вместо цикла for, позволяет писать читаемый код
работают быстрее
[number for number in numbers if number > 0]
"""

numbers = [-1, 3, 6, -5, 8, -3, 0]
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
newnums = [number for number in numbers if number > 0]  # генерируем новый список
print(newnums)

newdict = {pair[0]: pair[1] for pair in pairs}  # Генерируем словарь
print(newdict)

spisok_sto = [num for num in range(1, 101)]  # Сгенерировать список от 1 до 100
print(spisok_sto)

spis_sq = [num**2 for num in spisok_sto]  # из этого списка создать список квадратов
print(spis_sq)

# Создать список имен на букву А
names = ['Alex', 'Andrew', 'Joe', 'Anna']
newnames = [name for name in names if name.startswith('A')]
print(newnames)