"""6. Необходимо создать (не программно) текстовый файл, где каждая
строка описывает учебный предмет и наличие лекционных, практических и
лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и
 общее количество занятий по нему. Вывести словарь на экран."""


my_file = open('5.6(text).txt', 'r')
content = my_file.readlines()
dict = {}

for i in range(len(content)):
    subject, lecture, practice, lab = content[i].split()
    lecture = lecture.split('(')
    practice = practice.split('(')
    lab = lab.split('(')
    dict[subject] = int(lecture[0]) + int(practice[0]) + int(lab[0])

print(dict)
