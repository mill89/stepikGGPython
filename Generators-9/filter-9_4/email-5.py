# нужно оставить только корректно записанные адреса
from string import ascii_letters as alt, digits as dig


def check_email(email):
    for char in email:
        if char not in alt + dig + '@._':
            return False
    else:
        if email.count('@') == 1 and email.find('@') > 1 and email.find('@') < email.find('.'):
            return True
        return False


emails = input().split()
print(*filter(check_email, emails))
