def gcd(m, n):
    while m and n:
        if m < n:
            n = n % m
        else:
            m = m % n
        if m == 0:
            return int(n)
    return int(m)


def gcd1(n, m):
    while m and n:
        if m < n:
            n = n % m
        else:
            m = m % n
        if m == 0:
            return int(n)
    return int(m)


def lcm(m, n):
    return int(m/gcd(m, n) * n)


def lcm1(n, m):
    return m/gcd1(m, n) * n


def mn_lcm(a, b):
    res = 1
    if a < b:
        for i in range(a, b+1):
            res = lcm(res, i)
    elif a > b:
        for i in range(b, a+1):
            res = lcm1(res, i)
    elif a == b:
        return a

    return int(res)


print(mn_lcm(25, 1))


# long gcd(long m, long n)
# {
#     while(m && n) if (m < n) n %= m; else m %= n;
#     return (m == 0L) ? n : m;
# }
#
# long lcm(long m, long n)
# {
#     return (m/gcd(m,n))*n;
# }