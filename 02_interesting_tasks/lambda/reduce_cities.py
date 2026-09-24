from functools import reduce

data = filter(lambda city: city[1] > 10000000 and city[2] == 'primary', data)
data = map(lambda city: city[0], data)
cities = 'Cities: ' + reduce(
    lambda cities, city: cities + ', ' + city, sorted(data)
)

print(cities)
