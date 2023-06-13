a = int(input('первый элемент: '))
n = int(input('числа: '))
d = int(input('разность: '))
progression = []

for i in range(n):
    progression.append(a)
    a = a + d
    
print(*progression)