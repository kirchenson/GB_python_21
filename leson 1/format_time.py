'''2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и 
выведите в формате чч:мм:сс. Используйте форматирование строк.'''


def format_time(time):
    hours = time // 3600
    minutes = (time % 3600) // 60
    sec = (time % 3600) % 60
    return ('{}:{}:{}'.format(hours, minutes, sec))


time = int(input('Введите время в секундах: '))
print(format_time(time))
