def read_csv(filename):
    with open(filename, 'rt', encoding='utf-8') as file:
        keys = file.readline().rstrip().split(',')
        lines = file.readlines()
    result = []
    for line in lines:
        values = line.rstrip().split(',')
        result.append(dict(zip(keys, values)))
    return result
