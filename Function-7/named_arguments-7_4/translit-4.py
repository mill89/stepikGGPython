letters = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
           'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
           'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
           'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


# здесь продолжайте программу
def translit(text: str, sep='-') -> str:
    '''
    Переводит символы кириллицы в латиницу
    :param text: текст
    :param sep: символ заменяющий пробел
    :return: преобразованную строку
    '''
    return sep.join(
        ''.join(
            [letters[letter] if letter in letters else letter
             for letter in text.lower()]
        ).split()
    )


if __name__ == '__main__':
    s = input()

    print(translit(s))
    print(translit(s, '+'))
