class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_of_asphalt(self):
        print(self._length * self._width * 25 * 5)


road = Road(20, 5000)
road.mass_of_asphalt()
