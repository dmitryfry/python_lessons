my_list = [2,1,3,4,5,6,3]

x = 0
def generator(my_list, x):
    for el in my_list:
        if el > my_list[x]:
            yield el
    x += 1

new_gen = generator(my_list, x)

for i in new_gen:
    print(i)
