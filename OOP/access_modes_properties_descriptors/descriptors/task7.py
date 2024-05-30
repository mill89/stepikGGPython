class ValidateString:
    def __init__(self, min_length=3, max_length=100):
        self.min = min_length
        self.max = max_length

    def validate(self, string):
        return type(string) == str and self.min <= len(string) <= self.max


class StringValue:
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '-' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)


class RegisterForm:
    login = StringValue(ValidateString())
    password = StringValue(ValidateString())
    email = StringValue(ValidateString())

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f'<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: {self.email}\n</form>')


if __name__ == '__main__':
    form = RegisterForm('логин', 'пароль', 'email')
    form.show()
    print(form.get_fields())
