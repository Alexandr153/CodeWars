def narcissistic(value: int) -> bool:
    return sum(int(i) ** len(str(value)) for i in str(value)) == value

