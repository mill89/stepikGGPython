'''
Вводятся два целых положительных числа n и m, причем, n < m. Вывести в строку через
пробел квадраты целых чисел в диапазоне [n; m]. Программу реализовать при помощи цикла while.
'''

# Sample Input:
# 2 4
# Sample Output:
# 4 9 16

import math

n, m = map(int, input().split())
lst = list()
while n <= m:
    lst.append(round(math.pow(n, 2)))
    n += 1

if __name__ == '__main__':
    print(*lst)
