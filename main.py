# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list1 =[1, 27, 9, 35, 10, 64]
# sum = 0
# for i in range(len(list1)):
#     if i % 2 != 0:
#         sum += list1[i]
# print(sum)



# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

# from random import randint
#
# number = int(input('Введите размер списка '))
# list1 = []
# list2 = []
#
# for i in range(number):
#     list1.append(randint(0, 9))
#
# for i in range(len(list1)):
#     while i < len(list1)/2 and number > len(list1)/2:
#         number = number - 1
#         a = list1[i] * list1[number]
#         list2.append(a)
#         i += 1
#
# print(list1)
# print(list2)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# digit =int(input("Введите цифру "))
# surplus = ''
# while digit > 0:
#     surplus += str(digit % 2)
#     digit = digit // 2
# print(surplus)


# Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# lst = [1.1, 1.2, 3.1, 5, 10.01]
# diff = 0
# min_num = max_num = 0
# lst1 = []
#
# for item in lst:
#     if item != int(item):
#         item = item - int(item)
#         lst1.append(round(item, 2))
# diff = max(lst1) - min(lst1)
# print(diff)



# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Fn = F(n-1) + F(n-2)


# lst = [0, 1]
#
# for i in range(2, 10):
#     lst.append(lst[i-2] + lst[i-1])
#
# for k in range(2, 10):
#     lst.insert(0, lst[1] - lst[0])
# print(lst)

        #Через функцию
lst = [0, 1]
lst2 = [1, 0]
def func_fibo(lst: list, index: int):
    for i in range(2, index):
        lst.append(lst[i-2] + lst[i-1])
    return lst

def nega_fibo(lst2: list, index: int):
    for k in range(2, index):
        lst2.insert(0, lst2[1] - lst2[0])
    return lst2

fib_pos = func_fibo(lst, 10)
fib_neg = nega_fibo(lst2, 10)

print(fib_neg[:-1] + fib_pos)

