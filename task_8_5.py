class Stationery:
    def __init__(self, a):
        self.title = a

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


example = Stationery('Атрибут')
example1 = Pen('Ручка')
example2 = Pencil('Карандащ')
example3 = Handle('Маркер')
example.draw()
example1.draw()
example2.draw()
example3.draw()
