class InputValues:
    '''Декорирование стандартной функции с параметрами'''
    def __init__(self, render):
        self.__render = render

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            return list(map(self.__render, func(*args, **kwargs).split()))

        return wrapper


class RanderDigit:
    def __call__(self, string, *args, **kwargs):
        try:
            return int(string)
        except:
            return


render = RanderDigit()
input_dg = InputValues(render)(input)
res = input_dg()
print(res)
