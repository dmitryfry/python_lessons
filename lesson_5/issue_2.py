with open('lesson_5/files/issue_2.txt', 'r') as f:
        for line in f:
            print(len(line.split()))
