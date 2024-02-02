from csv import reader

def import_csv_layout(path):
    platform_map = []
    with open(path) as map:
        level = reader(map,delimiter = ',')
        for row in level:
            platform_map.append(list(row))
        return platform_map
