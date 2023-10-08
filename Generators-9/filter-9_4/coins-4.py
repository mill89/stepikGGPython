# Alex = map(int, input().split()) #1 5 2 7 10 25 50 100
# Galya = map(int, input().split()) #5 2 3 7 10 25 55
#
# s = set(Alex).intersection(set(Galya))

Sasha = map(int, input().split())
Galya = map(int, input().split())

print(*sorted(filter(lambda x: not x % 2, set(Sasha) & set(Galya))))
