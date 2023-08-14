class FlatIterator:

    def __init__(self, list_of_list):
        self.orig_list = list_of_list

    def __iter__(self):
        self.orig_list_cursor = 0
        self.incl_list_cursor = -1
        return self

    def __next__(self):
        self.incl_list_cursor += 1
        if self.incl_list_cursor > len(self.orig_list[self.orig_list_cursor])-1:
            self.orig_list_cursor +=1
            self.incl_list_cursor = 0

        if self.orig_list_cursor > len(self.orig_list)-1:
            raise StopIteration
        return self.orig_list[self.orig_list_cursor][self.incl_list_cursor]


# list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]
# for item in FlatIterator(list_of_lists_1):
#     print(item)
#
# print(list(FlatIterator(list_of_lists_1)))


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]


    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        # print(flat_iterator_item, check_item)
        assert flat_iterator_item == check_item
    # print(list(FlatIterator(list_of_lists_1)))
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()