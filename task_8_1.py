import time


class TrafficLight:
    color = 'red'

    def __init__(self):
        self.__color = 'red'
        print(f'Светофор')

    def running(self):
        if self.__color == 'red':
            time.sleep(7)
            self.__color = 'yellow'
        elif self.__color == 'yellow':
            time.sleep(2)
            self.__color = 'green'
        elif self.__color == 'yellow':
            time.sleep(4.5)
            self.__color = 'red'


example = TrafficLight()
example.running()
print(f'Цвет свечения: {example.color}')
