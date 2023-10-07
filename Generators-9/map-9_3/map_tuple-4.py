# tp = map(lambda s: tuple(s.split('=')), input().split())

# for x in tp:
#     print(x)

s = input()
s_lst = s.split()

tp = tuple(map(lambda x: tuple(x.split('=')), s_lst))

print(tp)
