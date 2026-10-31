filename = 'files.txt'
filesizes = {}
filenames = {}
size_ext = 1024
sizes = ['B', 'KB', 'MB', 'GB']

with open(filename, 'rt', encoding='utf-8') as file:
    for line in file:
        name_ext, filesize, units = line.split()
        name, ext = name_ext.split('.')
        filesize = int(filesize)
        for _ in range(sizes.index(units)):
            filesize *= size_ext
        filesizes[ext] = filesizes.get(ext, 0) + filesize
        filenames.setdefault(ext, []).append(name)


for key in sorted(filesizes):
    for filename in sorted(filenames[key]):
        print(filename + '.' + key)
    print('-' * 10)
    filesize = filesizes[key]
    count = 0
    while filesize > 1024:
        filesize = round(filesize / 1024)
        count += 1

    print(f'Summary: {filesize} {sizes[count]}')
    print()
