# функциональный подход - (то есть, более сложные функции реализуются путем вызова более простых)
def str_min(a, b):
    return a if a < b else b


def str_min3(a, b, c):
    return str_min(a, str_min(b, c))


def str_min4(a, b, c, d):
    return str_min(a, str_min3(b, c, d))