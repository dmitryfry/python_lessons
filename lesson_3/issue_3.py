def my_fync(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    return sum(my_list)

print(my_fync(5, 6, 24))
