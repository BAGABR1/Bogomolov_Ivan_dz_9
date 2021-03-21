import random


class Car:
    def __init__(self, s, c, n, ip):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = bool(ip)

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed}')

    def go(self):
        print(f'Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        turn_list = ['право', 'лево', 'зад']
        print(f'Машина повернула на{turn_list[random.randint(0, 2)]}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость превышена, она составляет: {self.speed}')
        else:
            print(f'Скорость не превышена, она составляет: {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость превышена, она составляет: {self.speed}')
        else:
            print(f'Скорость не превышена, она составляет: {self.speed}')


class PoliceCar(Car):
    pass


example1 = TownCar(72, 'зеленый', 'Ока', False)
example2 = WorkCar(37, 'красный', 'Запорожец', False)
example1.go()
example1.stop()
example1.turn()
example1.show_speed()
example2.go()
example2.stop()
example2.turn()
example2.show_speed()
