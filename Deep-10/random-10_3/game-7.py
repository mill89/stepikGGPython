'''
Имеется двумерное игровое поле размером N x N (N - натуральное число, вводится с клавиатуры),
представленное в виде вложенного списка:

P = [[0] * N for i in range(N)]

Требуется расставить в нем случайным образом M = 10 единиц (целочисленных) так, чтобы они не
соприкасались друг с другом (то есть, вокруг каждой единицы должны быть нули, либо граница поля).

P.S. Поле на экран выводить не нужно (вообще ничего не нужно выводить), только сформировать.

Sample Input:
10
Sample Output:
True
'''

import random


N = int(input())
P = [[0] * N for i in range(N)]
M = 10


def is_valid_position(row, col):
    for x in range(row - 1, row + 2):
        for y in range(col - 1, col + 2):
            if 0 <= x < N and 0 <= y < N and P[x][y] == 1:
                return False
    return True
#  if not np.any(P[i-1:i+2, j-1:j+2]):

random.seed(1)

while M > 0:
    row = random.randint(0, N - 1)
    col = random.randint(0, N - 1)

    if P[row][col] == 0 and is_valid_position(row, col):
        P[row][col] = 1
        M -= 1

# Вывод полученного игрового поля с единицами
for row in P:
    print(' '.join(map(str, row)))
