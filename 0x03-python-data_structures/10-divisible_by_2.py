#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    div = []
    for i in my_list:
        if (i % 2) == 0:
            return div.append(True)
        else:
            div.append(False)
    return div
