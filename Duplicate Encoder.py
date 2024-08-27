def duplicate_encode(word: str) -> str:
    res = ""
    word = word.lower()
    for i in word:
        if word.count(i) == 1:
            res += '('
        else:
            res += ')'
    else:
        return res
