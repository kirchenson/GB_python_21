'''4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.'''


def biggest_num(n):
    max = 0
    while n > 0:
        a = n % 10
        if a > max:
            max = a
        n = n // 10
    return max


n = int(input('Введите число: '))
print(f'Самая большая цифра: {biggest_num(n)}')