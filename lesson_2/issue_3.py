
seasons_list = [
            ['зима',[1, 2, 12]],
            ['весна', [3, 4, 5]],
            ['лето',[6, 7, 8]],
            ['осень',[9, 10, 11]]]


seasons_dict = {'Зима': (1, 2, 12),
               'Весна': (3, 4, 5),
               'Лето': (6, 7, 8),
               'Осень': (9, 10, 11)}

my_int = int(input('введите номер месяца: '))

for key in seasons_dict.keys():
    if my_int in seasons_dict[key]:
        print(key)

for key in seasons_list:
    if my_int in key[1]:
        print(key[0])
