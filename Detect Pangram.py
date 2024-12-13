def is_pangram(st: str) -> bool:
    dictionary = 'abcdefghijklmnopqrstuvwxyz'
    for i in dictionary:
        if i in st.lower():
            continue
        else:
            return False
    else:
        return True
