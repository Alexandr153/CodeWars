def to_camel_case(text):
    if text == '':
        return ''
    c = text[0]
    text_format = text.title()
    text_format = text_format[1:]
    text_format = str(c) + text_format
    for i in text_format:
        if i == '-':
            text_format = text_format.replace('-', "", 1)
        elif i == '_':
            text_format = text_format.replace('_', "", 1)
        else:
            continue
    return text_format



