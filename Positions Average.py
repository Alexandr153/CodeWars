def pos_average(s):
    s = s.split(', ')
    sum = 0
    counter = 0
    while len(s) > 1:
        x = 0
        while x < len(s[0]):
            i = s[0]
            for k in s[1:]:
                sum += 1
                if k[x] == i[x]:
                    counter += 1
            else:
                x += 1
        s = s[1:]
    return counter / 270 * 100



