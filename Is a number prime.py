from math import sqrt


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    else:
        for i in range(1, int(sqrt(num))):
            if i == num:
                return True
            if num % i == 0 and i != 1:
                return False
