"""
Тернарный оператор

name = 'Max' if has_name else 'Noname'
number = 1 if is_one else 2
print('привет' if is_ru else 'hello')
"""
word = 'сингулярность'
jword = []

for i in range(len(word)):
    letter = word[i] if i % 2 == 0 else word[i].upper()  # Тернарный оператор вместо условия if else
    jword.append((letter))
#    if i % 2 == 0:
 #       jword.append(word[i])
   # else:
      #  jword.append(word[i].upper()
print(jword)
jlist = ''.join(jword)
print(jlist)

passwrd = input('Введите пароль')
print('enter' if passwrd == 'pass' else 'access denied')