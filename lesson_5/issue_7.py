import json

my_dict = {}
our_sum = []

with open('lesson_5/files/issue_7.txt', 'r') as f:
    for line in f:
        firm = line.rstrip().split()[0]
        profit = int(line.rstrip().split()[2])
        costs = int(line.rstrip().split()[3])
        net_profit = profit - costs
        my_dict[firm] = net_profit
        if profit > costs:
            our_sum.append(net_profit)

final_list = [ my_dict, {"average_profit": sum(our_sum)} ]

with open('lesson_5/files/issue_7_w.txt', 'w') as f:
    json.dump(final_list, f)
