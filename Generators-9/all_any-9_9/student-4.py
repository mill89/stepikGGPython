'''
Вводятся оценки студента в одну строчку через пробел. Необходимо определить,
имеется ли в этом списке хотя бы одна оценка ниже тройки. Если это так, то вывести на
экран строку "отчислен", иначе - "учится".

Задачу реализовать с использованием одной из функций: any или all.
'''

# Sample Input:
# 3 3 3 2 3 3
# Sample Output:
# отчислен

marks = any(int(mark) < 3 for mark in input().split())
print('отчислен' if marks else 'учится')

# print(['учится', 'отчислен'][marks])