# 2 числа в квадрат
get_sq = lambda n: n ** 2

# 3
# бъявите анонимную (лямбда) функцию с двумя параметрами для деления одного
# целого числа на другое. Если происходит деление на ноль, то функция должна
# возвращать значение None, иначе - результат деления.
get_div = lambda a, b: None if  b == 0 else a / b

# 4
# Объявите анонимную (лямбда) функцию для вычисления модуля числа
# (то есть, отрицательные числа нужно делать положительными).
l = lambda x: abs(x)
print(l(float(input())))

# 5
# Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей
# строку фрагмента "ra". То есть, функция должна возвращать True, если такой
# фрагмент присутствует в строке и False - в противном случае.
print((lambda st: "ra" in st)(input()))