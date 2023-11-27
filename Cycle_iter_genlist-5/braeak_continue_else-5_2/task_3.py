# На каждой итерации цикла вводится целое число. Необходимо подсчитать произведение только положительных
# чисел, до тех пор, пока не будет введено значение 0. Реализовать пропуск вычислений с помощью оператора continue,
# а также использовать цикл while. Результат произведения вывести на экран.

# Sample Input:
# 2
# -1
# 3
# 2
# -5
# 7
# 0
# Sample Output:
# 84

i = 1

while True:
    num = int(input())
    if num == 0:
        break
    else:
        if num > 0:
            i *= num
        else:
            continue

print(i)