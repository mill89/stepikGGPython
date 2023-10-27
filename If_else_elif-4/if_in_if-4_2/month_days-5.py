'''
Вводится порядковый номер месяца (1, 2, ..., 12).
Вывести на экран количество дней в этом месяце.
Принять, что год не является високосным.
Реализовать через условный оператор, в котором следует использовать не более трех ветвей (блоков).

P.S. Число дней в месяцах не високосного года, начиная с января:
31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
'''

# Sample Input:
# 2
# Sample Output:
# 28

month = int(input())
a = [1, 3, 5, 7, 8, 10, 12]
if month in a:
    print(31)
else:
    if month == 2:
        print(28)
    else:
        print(30)
        