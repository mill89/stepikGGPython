'''
Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту
строку в список чисел и возвращает их сумму.

Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
Примените декоратор со значением start=5 к функции и вызовите декорированную функцию
для введенной строки s:

s = input()
'''

# Sample Input:
# 5 6 3 6 -4 6 -1
# Sample Output:
# 26

def start_sum(start=5):
    def func_decor(func):
        def wrapper(s):
            return start + func(s)

        return wrapper
    return func_decor


@start_sum()
def get_integers_list(s):
    return sum(int(i) for i in s.split())


print(get_integers_list(input()))
