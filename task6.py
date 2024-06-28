class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list if type_list in ('ul', 'ol') else 'ul'

    def __call__(self, lst, *args, **kwargs):
        return '\n'.join([f'<{self.type_list}>', *map(lambda x: f'<li>{x}</li>', lst), f'</{self.type_list}>'])


if __name__ == '__main__':
    lst = ['Пункт меню 1', 'Пункт меню 2', 'Пункт меню 3', 'Пункт меню 4']
    render = RenderList('<ul>')
    html = render(lst)
    print(html)
