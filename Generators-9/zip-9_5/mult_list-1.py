# Необходимо попарно перебрать их элементы и перемножить между собой.
# При реализации программы используйте функции zip и map

# 1
# z = zip(map(int, input().split()), map(int, input().split()))
#
# mul = map(lambda x: x[0] * x[1], z)
#
# for _ in range(3):
#     print(next(mul), end=' ')

# 2
mul = map(lambda x: (int(x[0]) * int(x[1])), zip(input().split(), input().split()))

for _ in range(3):
    print(next(mul), end=' ')
