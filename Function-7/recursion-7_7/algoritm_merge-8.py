# Вводится список из целых чисел в одну строчку через пробел.
# Необходимо выполнить его сортировку по возрастанию с помощью алгоритма сортировки слиянием.
# Функция должна возвращать новый отсортированный список.

# Sample Input:
# 8 11 -6 3 0 1 1
# Sample Output:
# -6 0 1 1 3 8 11

def merge_list(list1, list2):
    m_list = []
    i, n = 0, 0

    while i < len(list1) and n < len(list2):
        if list1[i] <= list2[n]:
            m_list.append(list1[i])
            i += 1
        else:
            m_list.append(list2[n])
            n += 1

    m_list += list1[i:] + list2[n:]
    return m_list


def split_and_merge_list(lst):
    N = len(lst) // 2
    lst1 = lst[:N]
    lst2 = lst[N:]

    if len(lst1) > 1:
        lst1 = split_and_merge_list(lst1)
    if len(lst2) > 1:
        lst2 = split_and_merge_list(lst2)

    return merge_list(lst1, lst2)


if __name__ == '__main__':
    print(*split_and_merge_list(list(map(int, input().split()))))
