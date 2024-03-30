def friend(x):
    array = []
    for i in x:
        if len(i) == 4:
            array.append(i)
        else:
            continue
    return array