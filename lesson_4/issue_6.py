from itertools import count, cycle

for el in count(start=100, step=1):
    if el > 1000000000000000000000:
        break
    print(el)

my_list = [1,2]
for el in cycle(my_list):
    print(el)
