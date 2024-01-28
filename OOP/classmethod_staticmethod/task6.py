class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = fac.build_sequence()
        for sub in string.split(','):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


class Factory:
    @staticmethod
    def build_sequence():
        pass

    @staticmethod
    def build_number(string):
        pass


res1 = Loader.parse_format('4, 5 , -6', Factory)
res2 = Loader.parse_format("1, 2, 3, -5, 10", Factory)
