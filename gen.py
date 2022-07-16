
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

def flat_generator(my_list):
    i = 0
    while i < len(my_list):
        i += 1
        j = 0
        while j < len(my_list[i - 1]):
            yield my_list[i - 1][j]
            j += 1


def flat_list():
    item_list = [item for item in flat_generator(nested_list)]
    print()
    return item_list


if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)

    print(flat_list())