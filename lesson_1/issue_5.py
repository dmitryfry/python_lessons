earnings = int(input('введите выручку: '))
costs = int(input('введите издержки: '))

if earnings > costs:
    net = earnings - costs
    print(f'поздравляю фирма работает в плюс: {net}')
    number_of_employees = int(input('введите число сотрудников: '))
    net_for_one = net / number_of_employees
    print(f'прибыль в расчете на одного сотрудника составила: {net_for_one}')
elif earnings < costs:
    print('пора идти учить python')
else:
    print('поздравляю мы свели концы с концами')



