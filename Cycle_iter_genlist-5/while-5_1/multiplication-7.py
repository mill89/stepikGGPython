'''
Вводится натуральное (то есть, целое положительное) число (от трехзначного и более).
Найти произведение всех его цифр. Результат вывести на экран. Программу реализовать
при помощи цикла while.
'''

# Sample Input:
# 821
# Sample Output:
# 16

num = list(map(int, input()))
i = 1
res = num[0]

while i != len(num):
    res = res * num[i]
    i += 1

if __name__ == '__main__':
    print(res)
