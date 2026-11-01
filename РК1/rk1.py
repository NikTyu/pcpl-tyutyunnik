from operator import itemgetter


class File:
    """Файл"""
    def __init__(self, id, name, size, cat_id):
        self.id = id
        self.name = name
        self.size = size
        self.cat_id = cat_id


class Catalog:
    """Каталог файлов"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class FileCatalog:
    """
    'Файлы каталога' для реализации
    связи многие-ко-многим
    """
    def __init__(self, cat_id, file_id):
        self.cat_id = cat_id
        self.file_id = file_id


catalogs = [
    Catalog(1, 'каталог документов'),
    Catalog(2, 'системный каталог'),
    Catalog(3, 'загрузки'),

    Catalog(11, 'каталог (резервный) документов'),
    Catalog(22, 'системный (резервный) каталог'),
    Catalog(33, '(резервные) загрузки'),
]

files = [
    File(1, 'report.docx', 120, 1),
    File(2, 'config.sys', 4, 2),
    File(3, 'kernel.dll', 850, 2),
    File(4, 'movie.mp4', 700000, 3),
    File(5, 'setup.exe', 35000, 3),
]

files_catalogs = [
    FileCatalog(1, 1),
    FileCatalog(2, 2),
    FileCatalog(2, 3),
    FileCatalog(3, 4),
    FileCatalog(3, 5),

    FileCatalog(11, 1),
    FileCatalog(22, 2),
    FileCatalog(22, 3),
    FileCatalog(33, 4),
    FileCatalog(33, 5),
]


def main():
    """Основная функция"""

    one_to_many = [(f.name, f.size, c.name)
        for c in catalogs
        for f in files
        if f.cat_id == c.id]

    many_to_many_temp = [(c.name, fc.cat_id, fc.file_id)
        for c in catalogs
        for fc in files_catalogs
        if c.id == fc.cat_id]

    many_to_many = [(f.name, f.size, cat_name)
        for cat_name, cat_id, file_id in many_to_many_temp
        for f in files if f.id == file_id]

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []
    for c in catalogs:
        c_files = list(filter(lambda i: i[2] == c.name, one_to_many))
        if len(c_files) > 0:
            c_sizes = [size for _, size, _ in c_files]
            c_sizes_sum = sum(c_sizes)
            res_12_unsorted.append((c.name, c_sizes_sum))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}
    for c in catalogs:
        if 'каталог' in c.name:
            c_files = list(filter(lambda i: i[2] == c.name, many_to_many))
            c_files_names = [x for x, _, _ in c_files]
            res_13[c.name] = c_files_names

    print(res_13)


if __name__ == '__main__':
    main()
