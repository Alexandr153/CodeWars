def nb_year(p0, percent, aug, p):
    counter = 0
    while p0 < p:
        counter += 1
        p0 = int(p0 + (p0 * (percent / 100)) + aug)
    return counter
