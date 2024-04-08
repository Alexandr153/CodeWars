def printer_error(s):
    count = 0
    count_words = len(s)
    Array = 'nopqrstuvwxyz'
    for i in s:
        if i in Array:
            count += 1
    return str(count) + "/" + str(count_words)


#12
