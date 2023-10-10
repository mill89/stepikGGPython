# 1
def get_tag(st: str, tag='h1') -> str:
    return f'<{tag}>{st}</{tag}>'


# 2
def get_tag2(st: str, tag='div', up=True) -> str:
    return f'<{tag.upper()}>{st}</{tag.upper()}>' if up else f'<{tag}>{st}</{tag}>'


if __name__ == '__main__':
    text = input()

    # 1
    print(get_tag(text))
    print(get_tag(text, 'div'))

    # 2
    print(get_tag2(text))
    print(get_tag2(text, up=False))
