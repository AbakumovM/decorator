from test1 import test_1
from test2 import test_2
from test1 import flat_generator


list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]





if __name__ == '__main__':
    test_1()
    test_2()
    flat_generator(list_of_lists_1)