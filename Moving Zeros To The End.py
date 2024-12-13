def move_zeros(lst: list):
    zero_counter = lst.count(0)
    for i in range(zero_counter):
        lst.remove(0)
        lst.append(0)
    return lst


def duplicate_encode(string_: str):
    a = [")" if string_.count(i) > 1 else "(" for i in string_.lower()]
    return ''.join(a)
