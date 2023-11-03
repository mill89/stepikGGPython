# https://stepik.org/lesson/988837/step/5?unit=996322

t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

match book:
    case _, autor, name, *_:
        print('Yes')
    case _, autor, name, price, *_:
        print('Yes')
    case _, autor, name, _, year, *_:
        print('Yes')
    case _, autor, name, price, year, *_:
        print('Yes')
    case _:
        print('No')

