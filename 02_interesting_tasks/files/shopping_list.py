def get_price(filename, product):
    with open(filename) as file:
        data = file.readlines()
    result = {filename: float('inf')}
    for line in data:
        key, value = line.split(':')
        if key == product:
            result = {filename: int(value.strip())}
    return result

products = (input() for _ in range(int(input())))
filenames = {'desyatochka.txt': 'Десяточка', 'kubit.txt': 'Кубит', 'polosa.txt': 'Полоса'}

prices = {}
for product in products:
    for filename in filenames:
        prices[product] = prices.get(product, []) + [get_price(filename, product)]

result = {}
for product, shops in prices.items():
    min_price = float('inf')
    min_shop = None
    for shop in shops:
        for filename, price in shop.items():
            if price < min_price:
                min_price = price
                min_shop = filename
    result[min_shop] = result.get(min_shop, []) + [product]

for filename in filenames:
    print(filenames[filename] + ':')
    if filename in result:
        print(*result[filename], sep=', ')
    else:
        print('–')
