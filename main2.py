# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

N = int(input())
min = int(input('мин: '))
max = int(input('макс: '))

import random
list1 = []
for i in range(N):
    list1.append(random.randint(-10, 11))
print(list1)

index_list = []
for i in range(len(list1)):
    if list1[i] >= min and list1[i] <= max:
        index_list.append(i)
        
print(index_list)