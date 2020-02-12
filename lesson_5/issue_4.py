my_dict = { 1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
with open('lesson_5/files/issue_4.txt', 'r') as fr:
    with open('lesson_5/files/issue_4_w.txt', 'w') as fw:
        for line in fr:
            fw.write(f'{my_dict[int(line.split()[2])]} {line.split()[1]} {line.split()[2]} \n')
