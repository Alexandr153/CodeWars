def disemvowel(string_: str) -> str:
    return ''.join(list(filter(lambda x: x if x not in 'aeouiAEOUI' else '', string_)))
