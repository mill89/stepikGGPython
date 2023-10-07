cities = list(map(lambda city: city if len(city) > 5 else '-', input().split()))

print(*cities)
