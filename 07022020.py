# Задание 1
#Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

first_list = ['qwerty', 123, 234.4, None, 9876]
print(first_list)
for el in first_list:
    type_list = type(el)
    print(type_list)

# Задание 2
# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

#second_list = input('Введите через запятую элементы списка: ', )
#print(second_list)
#pos_list = int(0)
#for el in second_list:
#    second_list[pos_list], second_list[pos_list + 1] = second_list[pos_list + 1], second_list[pos_list]
#    pos_list += 2
#print(second_list)



# Задание 3
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

number_month = int(input('Введите номер месяца в диапазоне от 1 до 12:   ', ))
number_month = number_month - 1
month_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(month_list[number_month])
month_dict = {0: 'зима', 1: 'зима', 2: 'весна', 3: 'весна', 4: 'весна', 5: 'лето',
              6: 'лето', 7: 'лето', 8: 'осень', 9: 'осень', 10: 'осень', 11: 'зима'}
print(month_dict.get(number_month))

# Задание 4
# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

text_user = input('Введите строку с пробелами:   ', ).split()
number_str = 1
for el in text_user:
    print(number_str, el[0:9])
    number_str += 1

# Задание 4
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
