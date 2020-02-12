lower_that_20 = []
sum_list = []
with open('lesson_5/files/issue_3.txt', 'r') as f:
    for line in f:
        sum_list.append(line.split()[1])
        if int(line.rstrip().split()[1]) < 20:
            lower_that_20.append(line.rstrip().split()[0])
print(lower_that_20)
print(sum(map(int, sum_list)))
