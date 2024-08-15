def is_valid_walk(walk: list[str]) -> bool:
    x, y = 0, 0
    rules: dict = {
        'n': 1,
        's': -1,
        'e': +1,
        'w': -1
    }
    for i, k in walk:
        if k in 'ns':
            x += rules[k]
        else:
            y += rules[k]

    return True if len(walk) == 10 and x == 0 and y == 0 else False






