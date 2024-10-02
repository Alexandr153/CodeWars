def dig_pow(n, p) -> int:
    res = 0
    for i in str(n):
        res += int(i)**p
        p += 1
    return res / n if res % n == 0 else -1
