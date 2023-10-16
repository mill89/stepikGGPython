rivers = input().split()

print(*sorted(rivers, key=len, reverse=True))