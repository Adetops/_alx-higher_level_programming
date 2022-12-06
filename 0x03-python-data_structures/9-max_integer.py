#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list = [int(x) for x in my_list]
    for i in range(len(my_list)):
        if len(my_list) == 0:
            return 'None'
        elif my_list[i] < my_list[i + 1]:
            temp = my_list[i]
            my_list[i] = my_list[i + 1]
            my_list[i + 1] = temp
        return my_list[0]

