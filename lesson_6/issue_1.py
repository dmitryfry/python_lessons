from itertools import cycle
import time

class TrafficLight:
    def __init__(self):
        self.__color = [['красный', 7], ['желтый', 2], ['зеленый', 10]]

    def running(self):
        for el in cycle(self.__color):
            print(el[0])
            time.sleep(el[1])

traffic_light = TrafficLight()
traffic_light.running()
