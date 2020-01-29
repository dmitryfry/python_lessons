my_list = [7, 5, 3, 3, 2]

user_int = int(input('введите натуральное число: '))

my_list.append(user_int)
my_list.sort(reverse=True)
print(my_list)
