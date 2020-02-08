import re

regex = r"\b\d+\b"

def sum_digits(str):
    return re.findall(regex, str)

my_dict = {}

with open('lesson_5/files/issue_6.txt', 'r') as f:
    for line in f:
        my_sum = sum_digits(line)
        my_dict[(line.split()[0])] = sum(map(int, my_sum))

print(my_dict)
