'''Вводятся три целых числа в одну строку через пробел.
Необходимо определить наименьшее среди них и вывести его на экран.
Реализовать программу, используя условный оператор, без использования функции min.
'''

# Sample Input:
# 8 11 -1
# Sample Output:
# -1

a, b, c = map(int, input().split())

if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)
    