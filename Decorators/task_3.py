from task_1 import logger

@logger
def flat_generator(list_of_lists):
    list_of_lists_cursor = -1

    while list_of_lists_cursor < len(list_of_lists):
        incl_list_cursor = 0
        list_of_lists_cursor += 1
        if list_of_lists_cursor == len(list_of_lists):
            break

        while incl_list_cursor < len(list_of_lists[list_of_lists_cursor]):
            yield list_of_lists[list_of_lists_cursor][incl_list_cursor]
            incl_list_cursor +=1


list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
for item in flat_generator(list_of_lists_1):
    print(item)