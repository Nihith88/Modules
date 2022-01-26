"""
Истина: не пустая строка, не пустой список, число не равное нулю, число с пл.точкой
Ложь: пустая строка (последовательность), None, 0

abb = 'string'
if abb"
    <do this>
result = [number for number in numbers if number > 0 and math.sqrt(number) < 2]
"""
# Добавление элемента в список

def add_el(t_list= None):
    t_list = t_list or []
    t_list.append(2)
    return t_list

result = add_el()  # без указания аргумента
print(result)
result = add_el([0, 1])  # с указанием аргумента
print(result)