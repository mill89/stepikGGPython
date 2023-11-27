'''
Имеется список базовых нот:

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

Вводятся три целых числа в диапазоне от 1 до 7 - номера нот, в одну строчку через пробел.
Необходимо отобразить указанные ноты в виде строки через пробел, но перед нотами до и фа
дополнительно ставить символ диеза '#'. Реализовать эту программу с использованием
тернарного условного оператора (он может использоваться несколько раз).
'''

# Sample Input:
# 1 6 7
# Sample Output:
# #до ля си

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a, b, c = map(int, input().split())

res1 = '#' + m[a-1] if m[a-1] == m[0] or m[a-1] == m[3] else m[a-1]
res2 = '#' + m[b-1] if m[b-1] == m[0] or m[b-1] == m[3] else m[b-1]
res3 = '#' + m[c-1] if m[c-1] == m[0] or m[c-1] == m[3] else m[c-1]

print(res1, res2, res3, sep=' ')