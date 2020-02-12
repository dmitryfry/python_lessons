my_list = list(input('Введите элементы списка: '))

if len(my_list) % 2 == 0:
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]
    print(my_list)
else:
    last_element = my_list[-1]
    print(type(last_element))
    del my_list[-1]
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]
    my_list.append(last_element)
    print(my_list)
