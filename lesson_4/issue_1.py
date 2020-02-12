from sys import argv

def salary(hours, per_hour, prize):
    salary = hours * per_hour + prize
    return salary

salary(argv[1], argv[2], argv[3])
