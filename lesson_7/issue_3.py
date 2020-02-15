class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return self.count + other

    def __sub__(self, other):
        if self.count >= other:
            return self.count - other
        else:
            return 'соответствующее сообщение'

    def __mul__(self, other):
        return self.count * other

    def __floordiv__(self, other):
        return self.count // other

    def make_order(self, row_count):
        count = self.count // row_count
        my_list = []
        for x in range(0, count):
            my_str = '*'
            my_str *= row_count
            my_str += '\n'
            my_list.append(my_str)
        end_count = self.count % row_count
        end_str = '*' * end_count
        my_list.append(end_str)
        print(my_list)

c = Cell(14)
c.make_order(4)
print(c + 5)
print(c - 5)
print(c * 5)
print(c // 5)
