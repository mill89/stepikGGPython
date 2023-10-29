'''
На вход программы подается целое десятичное число. Используя битовые операции,
выполните целочисленное деление введенного числа на 2.

Sample Input:
22
Sample Output:
11
'''

number = int(input())
number = number >> 1
print(number)

# print(int(input()) >> 1)