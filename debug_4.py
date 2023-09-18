
# def anonymous_filter(data):
#     return len(__import__('re').findall(r'[яЯ]', data)) >= 23


anonymous_filter = lambda x: len(__import__('re').findall(r'[яЯ]', x)) >= 23


print(anonymous_filter('Я - последняя буква в алфавите!'))
print(anonymous_filter('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))
