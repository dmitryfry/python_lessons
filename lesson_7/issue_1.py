import numpy as np

class Matrix:
    def __init__(self, my_lists):
        self.my_lists = my_lists

    def __str__(self):
        return self.my_lists

    def __add__(self, other):
        my = np.array(self.my_lists)
        oth = np.array(other.my_lists)
        result = my + oth
        return result

m = Matrix([[2, 2], [3, 3]])
m2 = Matrix([[3, 3], [2, 2]])

print(m + m2)
