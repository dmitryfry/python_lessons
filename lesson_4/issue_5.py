from functools import reduce

my_list = [ num for num in range(100, 1000 + 1) if num % 2 == 0 ]

def my_f(num1, num2):
    return num1 + num2

print(reduce(my_f, my_list))
