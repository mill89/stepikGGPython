# 1 list, tuple
s = input()

lst = list(map(int, s.split()))
lst.sort()
tp_lst = tuple(sorted(lst))

# print(lst)
# print(tp_lst)


# 2 dict
d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}


def get_sort(d):
    return list(d[k] for k in sorted(d.keys(), reverse=True))


# 3 int
numbers = set(map(int, input().split()))

# print(*sorted(numbers, reverse=True)[:4])


# 4
list1 = sorted(map(int, input().split()))
list2 = sorted(map(int, input().split()), reverse=True)

# print(map(sum, zip(list1, list2)))
