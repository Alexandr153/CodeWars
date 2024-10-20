def first_non_repeating_letter(s: str):
    for k, i in enumerate(s.lower()):
        if s.lower().count(i) == 1:
            return s[k]
        else:
            continue
    return ''
