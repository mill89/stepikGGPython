import time


def work_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        # time.sleep(2)
        res = func(*args, **kwargs)
        end = time.time()
        print(f'~~~ Время выполнения програмы: {end - start} ~~~~')
        return res

    return wrapper


@work_time
def get_s(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    print(get_s(1, 5))
