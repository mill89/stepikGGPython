#  Вводится строка из слов, записанных через пробел.
#  Необходимо на их основе составить прямоугольную таблицу из трех столбцов и N строк
#  (число строк столько, сколько получится). Лишнее (выходящее) слово - отбросить.
#  Реализовать эту программу с использованием функции zip.

cities = ['Москва', 'Уфа', 'Тула', 'Самара', 'Омск', 'Воронеж', 'Владивосток',
          'Лондон', 'Калининград', 'Севастополь']

table = zip(*[iter(cities)] * 3)

for i in table:
    print(*i)
