def dig_pow(n, p):
    result = 0
    for i in str(n):
        result += int(i)**p
        p += 1
    if result % n == 0:
        return result / n
    else:
        return -1

