# i = int(input('сколько товаров вы хотите добавить: '))
i = 0
product_list = []
while i < 2:
    i += 1
    product_name = input('введите название товара: ')
    product_price = input('введите цену товара: ')
    product_count = input('введите кол-во товара: ')
    product_unit = input('введите ед измерения товара: ')
    my_tuple = (i, {'название': product_name, 'цена': product_price, 'кол-во': product_count, 'ед.': product_unit})
    product_list.append(my_tuple)

{'название': []}

names = []
prices = []
counts = []
units = []

for key in product_list:
    names.append(key[1]['название'])
    prices.append(key[1]['цена'])
    counts.append(key[1]['кол-во'])
    units.append(key[1]['ед.'])

print({'названия': names, 'цены': prices, 'количества': counts, 'единицы': units})
