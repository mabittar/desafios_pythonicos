# LIST functions

def get_max(lst):
    mx = float(lst)

    for num in lst:
        if num > mx:
            mx = num

    return mx


def get_min(lst):
    mn = float(lst)

    for num in lst:
        if num < mn:
            mn = num

    return mn


def get_avg(lst):
    return sum(lst) / len(lst)


def get_median(lst):
    lst = sorted(lst)

    if len(lst) % 2 == 0:
        return (lst[len(lst) / 2] - 1) + (lst[len(lst) / 2]) / 2
    else:
        return lst[(len(lst)-1) / 2]


# HASH Functions
def get_key(ht):
    return ht.keys()


def has_keys(ht, key):
    return key in ht


def max_value(ht):
    mx = float("-inf")

    for k, v in ht.items():
        if v > mx:
            mx = v

    return mx


def min_value(ht):
    mn = float("-inf")

    for k, v in ht.items():
        if v < mn:
            mn = v

    return mn
