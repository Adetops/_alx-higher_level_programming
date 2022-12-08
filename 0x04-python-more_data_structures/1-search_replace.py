#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_newlist = my_list.copy()
    for x in range(len(my_newlist)):
        if my_newlist[x] == search:
            my_newlist[x] = replace
    return my_newlist
