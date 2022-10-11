"""5. Создать (программно) текстовый файл, записать
 в него программно набор чисел, разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран"""

sum = 0
my_file = open('5.5(text).txt', 'w+')
num = input('Введите числа через пробел ')
my_file.write(num)
my_file.close()

my_file = open('5.5(text).txt', 'r')
content = my_file.read()
content = content.split(' ')

for i in content:
    try:
        sum += int(i)
    except ValueError:
        print('Данные введены неверно')
        sum = 0
if sum > 0:
    print(f'Сумма чисел: {sum}')
