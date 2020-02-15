class Clother:
    def __init__(self, name, v, h):
        self.name = name
        self.v = v
        self.h = h

    @property
    def coat(self):
        print(self.v / 6.5 + 0.5)

    @property
    def costume(self):
        print(2 * self.h + 0.3)

c = Clother('имя', 2, 4)
c.coat
c.costume
