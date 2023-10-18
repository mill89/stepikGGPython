def get_even_sum(it):
    return sum(filter(lambda n: type(n) is int and not n % 2, it))


if __name__ == '__main__':
    assert (get_even_sum([1, 2, 3, "a", True, [4, 5], "c", (4, 5)])) == 6
    assert (get_even_sum({5, 6, 7, '8', 5, '4'})) == 18
    assert (get_even_sum((10, "f", '33', True, 12))) == 22
    assert (get_even_sum(['1', True, False, (1, 23)])) == 0
