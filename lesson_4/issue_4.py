import collections

my_list = [1,2,3,3]
print([item for item, count in collections.Counter(my_list).items() if count <= 1])
