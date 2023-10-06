# 3
def my_first_function():
    print("It's my first function")


# 4
def print_text():
    print(f"Уважаемый, {input()}! Вы верно выполнили это задание!")


# 5
def item_weight(weight: str):
    print(f"Предмет имеет вес: {weight} кг.")


# 6 принимает список, находит максимальное,
# минимальное и сумму значений этого списка и выводит результат в виде строки
def numbers(lst: list):
    print(f"Min = {min(lst)}, max = {max(lst)}, sum = {sum(lst)}")


# 7 Периметр прямоугольника
def perimeter_calculation_rectangle(width: int, height: int):
    print(f"Периметр прямоугольника, равен {(width + height) * 2}")


if __name__ == '__main__':
    # 3
    my_first_function()
    # 4
    print_text()
    # 5
    item_weight(input())
    # 6
    numbers(list(map(int, input().split())))
    # 7
    perimeter_calculation_rectangle(*list(map(int, input().split())))
