def py_func(a, n):
    return a ** n


def my_func(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res

print(py_func(5,-7))
print(my_func(5,-7))
