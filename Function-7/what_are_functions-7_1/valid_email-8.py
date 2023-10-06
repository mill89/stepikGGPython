'''
 Функция, которая проверяет корректность переданного ей email-адреса в виде строки.
 Если email верен, то функция выводит ДА, иначе - НЕТ.
'''
def check_email(email: str):
    for s in email:
        if not ('A' <= s <= 'Z' or 'a' <= s <= 'z' or '0' <= s <= '9' or s in '_@.'):
            print('НЕТ')
            break
    else:
        print('ДА' if '@' in email and '.' in email else 'НЕТ')


if __name__ == '__main__':
    check_email(input())