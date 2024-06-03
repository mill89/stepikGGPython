class Decor:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, *args, **kwargs):
        result = self.__fn(*args, **kwargs)
        return f'{result} Milan!'


@Decor
def greeting(text):
    return text


print(greeting('Hello,'))


# class Decor:
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return f'{result} {self.name}!'
#         return wrapper
#
#
# @Decor('Milan')
# def greeting(text):
#     return text
#
#
# print(greeting('Hello,'))
