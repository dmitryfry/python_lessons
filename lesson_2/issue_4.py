my_list = input('введите несколько слов разделенных пробелами: ').split()

i = 0
for key in my_list:
    i += 1
    print(f'{i}. {key[0:10]}')
