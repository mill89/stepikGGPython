'''
Дата некоторого дня характеризуется двумя натуральными числами: m (порядковый номер месяца)
и n (число). По введенным m и n (в одну строку через пробел) определить:

а) дату предыдущего дня (принять, что m и n не характеризуют 1 января);
б) дату следующего дня (принять, что m и n не характеризуют 31 декабря).

В задаче принять, что год не является високосным. Вывести предыдущую дату
и следующую дату (в формате: mm.dd, где m - число месяца; d - номер дня) в
одну строчку через пробел.

P.S. Число дней в месяцах не високосного года, начиная с января:
31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
'''

# Sample Input:
# 8 31
# Sample Output:
# 08.30 09.01

m, n = map(int, input().split())
lst = [1, 3, 5, 7, 8, 10, 12] # 31
lst2 = [4, 6, 9, 11] # 30
prev_month = m
prev_day = n - 1
next_month = m
next_day = n + 1

if n == 1:
    if m == 1:
        prev_month = 12
        prev_day = 31
    elif m - 1 in lst:
        prev_day = 31
        prev_month = m - 1
    elif m - 1 in lst2:
        prev_day = 30
        prev_month = m - 1
    else:
        prev_day = 28
        prev_month = m - 1

elif n == 30:
    if m in lst:
        next_day = 31
        next_month = m
    elif m in lst2:
        next_day = 1
        next_month = m + 1

elif n == 31:
    if m == 12 and n == 31:
        next_month = 1
        next_day = 1
    else:
        next_day = 1
        next_month = m + 1

elif n == 28:
    if m in lst:
        next_day = 29
        next_month = m
    elif m in lst2:
        next_day = 29
        next_month = m
    else:
        next_day = 1
        next_month = m + 1


print(f'{str(prev_month).rjust(2, "0")}.{str(prev_day).rjust(2, "0")} {str(next_month).rjust(2, "0")}.{str(next_day).rjust(2, "0")}')
