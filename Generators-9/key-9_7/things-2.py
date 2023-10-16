things = ['ножницы=100', 'котелок=500', 'спички=20', 'зажигалка=40', 'зеркальце=50']

things = (x.split('=') for x in things)

print(*dict(sorted(things, key=lambda x: int(x[1]), reverse=True)))
