"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""


from itertools import count,cycle
count_1=0
n = int(input("Введите целое число:"))
for i in count(n):
    print(i, end=' ')
    count_1+=1
    if count_1==10:
        break
print('\n Повторение элементов списка')
count=0
list = [5, 3, 3, 1, 0, 4, 2, 4, 7, 3]
for i in cycle(list):
    print(i, end=' ')
    count+=1
    if count==20:
        break
