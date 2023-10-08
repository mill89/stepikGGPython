# Необходимо оставить только двузначные числа.
# 1
numbers = filter(lambda i: 9 < i < 100 or -100 < i < -9, map(int, input().split()))

# 2
# numbers = filter(lambda i: len(i.lstrip('-')) == 2, input().split())

print(*numbers)
