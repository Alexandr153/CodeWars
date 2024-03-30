def generate_hashtag(s):
    if s == "":
        return False
    else:
        s = '#' + s.title().replace(' ', '')
        if len(s) > 140:
            return False
        else:
            return s

