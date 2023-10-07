cities = filter(lambda city: len(city) > 5, input().split())

for _ in range(3):
    print(next(cities), end=' ')
