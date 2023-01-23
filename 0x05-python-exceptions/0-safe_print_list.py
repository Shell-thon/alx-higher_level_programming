#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_printed = 0
    try:
        for i in range(x):
            print(my_list[i], end=" ")
            num_printed += 1
            print()
        except IndexError:
            pass
        return num_printed

    print(safe_print_list([1, 2, 3], 5))  # 3
