'''
Имеется график функции f(x) = 0.5x^2 - 2.
Необходимо записать генератор, который бы выдавал значения этой функции для аргумента x
в диапазоне [a; b] с шагом 0.01
'''

a, b = map(int, input().split())

gen = (0.5 * pow(x / 100, 2) - 2.0 for x in range(a * 100, b * 100 + 1))

for _ in range(20):
    print(round(next(gen), 2), end=' ')
