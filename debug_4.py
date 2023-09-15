
def custom_filter(data):
    # return sum([i for i in data if type(i) == int and (i % 7 == 0)]) < 83
    return sum(filter(lambda x: type(x) == int and (x % 7 == 0), data)) < 83

some_list = [7, 14, 28, 32, 32, 56]

print(custom_filter(some_list))
