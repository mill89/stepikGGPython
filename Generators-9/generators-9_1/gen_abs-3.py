a, b = map(int, input().split())     # (a < b)
gen = (abs(i) for i in range(a, b + 1))     # генератор, выдает модули целых чисел из диапазона [a; b]

for c in range(5):
    print(next(gen))
    