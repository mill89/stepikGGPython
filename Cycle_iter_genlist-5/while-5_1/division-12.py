'''
Составить программу поиска всех трехзначных чисел, которые при делении на 47 дают в остатке
43 и кратны 3. Вывести найденные числа в строчку через пробел. Программу реализовать при помощи
цикла while.
'''

# Sample Input:
# Sample Output:
# 231 372 513 654 795 936

lst = []
i = 100

while i < 1000:
    if i % 47 == 43 and i % 3 == 0:
        lst.append(i)
    i += 1

if __name__ == '__main__':
    print(*lst)