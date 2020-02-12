import itertools

sum_list = []

with open('lesson_5/files/issue_5.txt', 'w') as f:
    while True:
        line = input('введите числа: ')
        if line is '' : break
        f.write(line + '\n')

with open('lesson_5/files/issue_5.txt', 'r') as f:
    for line in f:
        sum_list.append(line.rstrip().split())
        merged = list(itertools.chain(*sum_list))

print(sum(map(int, merged)))
