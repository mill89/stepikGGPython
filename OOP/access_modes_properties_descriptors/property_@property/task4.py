class Car:
    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if type(model) is str and 2 <= len(model) <= 100:
            self.__model = model


if __name__ == '__main__':
    car = Car()
    print(car.model)
    car.model = 'milan'

    print(car.model)
