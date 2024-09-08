from math import sqrt


def find_next_square(sq) -> int:
    i = sq + 1
    if sqrt(sq).is_integer():
        while not sqrt(i).is_integer():
            i += 1
    else:
        return -1
    return i

