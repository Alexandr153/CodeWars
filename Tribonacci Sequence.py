def tribonacci(signature: list[int], n: int) -> list:
    res = signature[:n] if n < 3 else [signature.append(sum(signature[-3:])) for _ in range(n - 3)]
    return res if n < 3 else signature

