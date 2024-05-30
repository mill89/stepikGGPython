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
    login = StringValue(ValidateString)

