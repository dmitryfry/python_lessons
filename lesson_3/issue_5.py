
final_sum = 0
quit = 'q'
while True:
    my_list = input("введите числа через пробел: ").split()
    if quit in my_list:
        my_list.remove(quit)
        if len(my_list) >= 1:
            my_int_list = list(map(int, my_list))
            final_sum += sum(my_int_list)
            print(final_sum)
            break
        else:
            print(final_sum)
            break
    else:
        my_int_list = list(map(int, my_list))
        final_sum += sum(my_int_list)
