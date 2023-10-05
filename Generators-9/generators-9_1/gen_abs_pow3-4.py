a = int(input())
gen = (abs(i) ** 3 for i in range(-a, a + 1))  # генератор, вычисляет модули и возводит их в 3 степень

for c in range(4):
    print(next(gen), end=' ')
