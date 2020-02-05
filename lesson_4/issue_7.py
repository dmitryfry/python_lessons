from itertools import count

def factorial():
    res = 1
    for x in count(1):
        res = x*res
        yield res

x = 1
for el in factorial():
    print(el)
    x += 1
    if x > 15:
        break
