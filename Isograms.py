def is_isogram(string: str):
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if string.lower().count(i) > 1:
            return False
    else:
        return True
