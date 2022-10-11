"""3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
 Выполнить подсчет средней величины дохода сотрудников."""


my_file = open('5.3(text).txt', 'r')
content = my_file.readlines()
balance_sum = 0
print('Оклад больше 20000 имеют: ')

for i in range(len(content)):
    content[i] = content[i].split(' ')
    if int(content[i][1]) < 20000:
        print(content[i][0])
    balance_sum += int(content[i][1])

print(f'Средняя выплата: {balance_sum / len(content)}')
my_file.close()
