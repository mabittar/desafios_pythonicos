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
    mn = float("inf")

    for k, v in ht.items():
        if v < mn:
            mn = v

    return mn
