class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('the car went')

    def stop(self):
        print('the car stopped')

    def turn(self, direction):
        print(f'the car turn {direction}')

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print('speed limit!')

class WorkCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print('speed limit!')

class PoliceCar(Car):
    pass

class SportCar(Car):
    pass

town_car = TownCar(61, 'blue', 'truck', False)
town_car.show_speed()
town_car.go()
town_car.stop()
town_car.turn('left')
print(town_car.color)
