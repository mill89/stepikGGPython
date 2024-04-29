class Car:
    def __init__(self, model):
        self.__model = model
        self.verify_model(self.model)
        self.verify_str(self.model)

    @classmethod
    def verify_model(cls, model):
        if type(model) is not str:
            raise TypeError('Должна быть сторока')

    @classmethod
    def verify_str(cls, model):
        if len(model) < 2 or len(model) > 100:
            raise TypeError('Неверная длина строки [2; 100]')

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model


if __name__ == '__main__':
    car = Car('kjjhjhjh')
    print(car.model)
    car.model = 'mazda'

    print(car.model)
