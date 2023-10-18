# 3
# Имеется программа, где читается глобальная переменная WIDTH и функция с именем func1.
# Допишите в теле функции команду, которая бы позволяла изменять глобальную переменную WIDTH.

WIDTH = int(input())


def func1():
    global WIDTH
    WIDTH += 1
    return WIDTH


print(func1())


# 4
# Имеется программа. Необходимо в теле функции func2 дописать команду,
# которая бы меняла значение уже существующей переменной msg, объявленной в функции func1.

# Sample Input:
# Сергей
# Балакирев
# Sample Output:
# Балакирев
# Балакирев

def func1():
    msg = input()

    def func2():
        nonlocal msg
        msg = input()
        print(msg)

    func2()
    print(msg)


func1()


# 5
#  Объявите функцию с именем create_global, которая имеет, следующую сигнатуру:
# def create_global(x): ...
#
# Эта функция должна создавать глобальную переменную с именем TOTAL и присваивать ей значение x.

def create_global(x):
    global TOTAL
    TOTAL = x
