from logger import param_logging

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]
@param_logging(path='logs/logs.log')
class FlatIterator:

    def __init__(self, my_list):
        self.my_list = my_list

    def __iter__(self):
        self.outer_list_cursor = 2
        self.inner_list_cursor = -1
        return self

    def __next__(self):
        self.outer_list_cursor += 1
        if self.outer_list_cursor == len(self.my_list[self.inner_list_cursor]):
            self.outer_list_cursor = 0
            self.inner_list_cursor += 1
        if self.inner_list_cursor == len(self.my_list):
            raise StopIteration
        return self.my_list[self.inner_list_cursor][self.outer_list_cursor]


def flat_list():
    item_list = [item for item in FlatIterator(nested_list)]
    print()
    return item_list


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)

    print(flat_list())


