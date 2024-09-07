def tribonacci(signature: list[int], n: int) -> list:
    res = [signature[r] for r in range(n)] if n < 3 else [signature.append(sum(signature[:-4:-1])) for i in range(n - 3)]
    return res if n < 3 else signature
