# 5
# Sample Input:
# BOTTOM
# Sample Output:
# Команда bottom

cmd = input()

match cmd:
    case 'top' | 'Top' | 'TOP':
        print('Команда top')
    case 'bottom' | 'Bottom' | 'BOTTOM':
        print('Команда bottom')
    case 'right' | 'Right' | 'RIGHT':
        print('Команда right')
    case 'left' | 'Left' | 'LEFT':
        print('Команда left')
    case _:
        print('Неверная команда')



# 6
def get_data(value):
    match value:
        case int():
            return value
        case str():
            return value
        case float():
            return value

    return None



# 7
def get_data(value):
    match value:
        case int() if value > 0:
            return value
        case str():
            return value
        case float() if -100 <= value <= 100:
            return value
