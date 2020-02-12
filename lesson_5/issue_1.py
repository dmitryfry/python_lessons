with open('lesson_5/files/my_file.txt', 'w') as f:
    while True:
        line = input('введите строку: ')
        if line is '' : break
        f.write(line + '\n')
