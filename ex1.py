t = ('milan', 'men', 1989)

match t:
    case tuple() as info:
        print(f'info: {info}')
    case _:
        print('Error!!!')
