'''Генератор, который бы возвращает все сочетания из двух букв латинского алфавита'''
from string import ascii_lowercase


gen = (a + b for a in ascii_lowercase for b in ascii_lowercase)

for _ in range(50):
    print(next(gen), end=" ")
    