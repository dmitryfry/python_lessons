def my_division(a,b):
    if b != 0:
        print(a / b)
    else:
        print('сегодня делим на ноль, а завтра?')

a = int(input('введите делимое: '))
b = int(input('введите делитель: '))

my_division(a,b)
