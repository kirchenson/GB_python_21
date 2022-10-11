"""2. Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк,
 количества слов в каждой строке."""

my_file = open('5.2(text).txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
for i in range(len(content)):
    content[i] = len(content[i].split(' '))
    print(f'Количество слов в строке {i + 1} - {content[i]}')
my_file.close()
