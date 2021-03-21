class Road:

    def __init__(self):
        self._length = 5000
        self._width = 20
        print('Длина-ширина-масса для 1м^2 1см толщиной-толцина в см')

    def calculate(self, m, z):
        h = self._length
        w = self._width
        print(f'{int((h*w*m*z)/1000)} т')


example = Road()
example.calculate(25, 5)
