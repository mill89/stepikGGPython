# https://stepik.org/lesson/988837/step/6?unit=996322

t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

# match book:
#
#     case (int(), str() as autor, str() as name) if len(autor) >= 6 and len(name) >= 10:
#         print('Yes1')
#     case (int(), str() as autor, str() as name, float() as price) if len(autor) >= 6 and price > 0:
#         print('Yes2')
#     case (int(), str() as autor, str() as name, _, int() as year) if year >= 2020:
#         print('Yes3')
#     case (int(), str() as autor, str() as name, float() as price, int() as year) if price > 0 and year >= 2020:
#         print('Yes4')
#     case _:
#         print('No')


match book:
    case (_, autor, title) if len(autor) > 5 and len(title) > 9:
        print('Yes')
    case (_, autor, title, price) if len(autor) >= 6 and price > 0:
        print('Yes')
    case (_, autor, title, _, year) if year >= 2020:
        print('Yes')
    case (_, autor, title, price, year) if price > 0 and year >= 2020:
        print('Yes')
    case _:
        print('No')
