def get_list_dig(lst):
    return list(filter(lambda n: type(n) in (int, float), lst))


if __name__ == '__main__':
    assert (get_list_dig((10, "f", '33', True, 12))) == [10, 12]
    assert (get_list_dig(['1', True, False, (1, 23)])) == []
    assert (get_list_dig([1, 2, 3, "a", True, [4, 5], "c", (4, 5)])) == [1, 2, 3]
