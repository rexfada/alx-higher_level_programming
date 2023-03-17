#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    dif_1 = set_1.difference(set_2)
    dif_2 = set_2.difference(set_1)
    set_3 = dif_1.union(dif_2)
    return set_3
