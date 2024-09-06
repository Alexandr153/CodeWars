def tribonacci(signature: list[int], n: int) -> list:
    [r for r in signature[:n]] if n <= 3 else [signature.append(sum(signature[:-4:-1])) for i in range(n - 3)]
    return signature

