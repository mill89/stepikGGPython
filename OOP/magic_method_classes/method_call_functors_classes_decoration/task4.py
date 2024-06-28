from string import ascii_lowercase, digits

class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ''
        self.password = ''

    def post(self, request):
        self.login = request.get('login', '')
        self.password = request.get('password', '')

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, _string, *args, **kwargs):
        return self.min_length <= len(_string) <= self.max_length


class CharsValidator:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, _string, *args, **kwargs):
        return set(_string) <= set(self.chars)


if __name__ == '__main__':
    lg = LoginForm('Enter site', validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase+ digits)])
    lg.post({'Login': 'root ', 'password': 'panda'})
    if lg.is_validate():
        print('Next processing datas')

    # lv = LengthValidator(min_length, max_length)
    # cv = CharsValidator(chars)
    # res = lv(string)
    # res = cv(string)
