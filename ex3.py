class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()

print(True if p1 in p1.__dict__ else False)
