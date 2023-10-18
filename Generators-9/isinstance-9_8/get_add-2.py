def get_add(a, b):
    if type(a) in (float, int) and type(b) in (float, int):
        return a + b
    if type(a) is str and type(b) is str:
        return a + b


if __name__ == '__main__':
    assert (get_add('1', 4)) == None
    assert (get_add(5, 4)) == 9
    assert (get_add('Hello', ' Milan')) == 'Hello Milan'
