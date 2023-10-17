# 2
*lst, x, y, z = input().split()
print(*lst)

# 3
# Sample Input:
# Москва Уфа Тверь Самара
# Sample Output:
# ('Москва', 'Уфа', 'Тверь', 'Самара')

lst_c = input().split()
print((*lst_c,))   # print(tuple(lst_c))

# 4
# Sample Input:
# 3 11
# Sample Output:
# 3 4 5 6 7 8 9 10 11
a, b = map(int, input().split())
print(*range(a, b + 1))

# 5
# Sample Input:
# 5.8 11.0 4.3
# Уфа Омск Тверь Самара
# Sample Output:
# 5.8 11.0 4.3 Уфа Омск Тверь Самара
print(*map(float, input().split()), *input().split())

# 6
# Sample Input:
# Города=about-cities
# Машины=read-of-cars
# Самолеты=airplanes
# Sample Output:
# Архив Главная Города Машины Новости Самолеты
# about-cities airplanes archive home news read-of-cars
menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
menu = {**menu, **dict([lst.split('=') for lst in lst_in])}