
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

def my_range(my_list):
    i = 0
    while i < len(my_list):
        i += 1
        j = 0
        while j < len(my_list[i - 1]):
            yield my_list[i - 1][j]
            j += 1


if __name__ == '__main__':
    for item in my_range(nested_list):
        print(item)