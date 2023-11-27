# Вводится натуральное число n (то есть, целое положительное). В цикле перебрать все целые числа в интервале
# [1; n] и сформировать список из чисел, кратных 3 и 5 одновременно. Вывести полученную последовательность чисел
# в виде строки через пробел, если значение n меньше 100. Иначе вывести на экран сообщение "слишком большое значение n"
# (без кавычек). Использовать в программе оператор else после цикла while.
#
# Sample Input 1:
# 49
# Sample Output 1:
# 15 30 45
# Sample Input 2:
# 100
# Sample Output 2:
# слишком большое значение n

n = int(input())
lst = []
i = 1

if n >= 100:
    print('слишком большое значение n')
else:
    while i < n + 1:
        if i % 3 == 0 and i % 5 == 0:
            lst.append(i)
        i += 1
    else:
        print(*lst)
