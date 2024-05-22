from math import sqrt, pow


def list_squared(m: int, n: int) -> [int]:
    sortList: list = []
    for i in range(m, n+1):
        temp: list = []
        for k in range(1, i+1):
            if i % k == 0:
                temp.append(pow(k, 2))
        temp: int = int(sum(temp))

        if sqrt(temp) % 1 == 0.0:
            sortList.append([i, temp])
        if i == n:
            return sortList


print(list_squared(1, 250))