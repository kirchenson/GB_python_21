'''Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, 
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.'''


def registration(name='Name', surname='Surname', date='Date', city='City', email='Email', phone='Phone'):
    """Форма для вывода данных о пользователе в одну строку"""
    print(f"Имя: {name} {surname} Дата рождения: {date} Город: {city} Контакты: {email} , {phone}")


name = input('Введите  имя ')
surname = input('Введите  фамилию ')
date = input('Введите дату рождения ')
city = input('Город проживания ')
email = input('Электронная почта ')
phone = input('Номер телефона ')

registration(name, surname, date, city, email, phone)
