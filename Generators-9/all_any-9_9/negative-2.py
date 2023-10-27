'''
Вводится строка вещественных чисел через пробел. Необходимо определить,
есть ли среди них хотя бы одно отрицательное. Вывести True, если это так и
False - в противном случае.

Задачу реализовать с использованием одной из функций: any или all.
'''

# Sample Input:
# 8.2 -11.0 20 3.4 -1.2
# Sample Output:
# True

# numbers = any(map(lambda n: float(n) < 0, input().split()))  # 1
numbers = any(float(n) < 0 for n in input().split())  # 2
print(numbers)
