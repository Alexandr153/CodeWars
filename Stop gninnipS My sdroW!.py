def spin_words(sentence: str) -> str:
    sentence = sentence.split(' ')
    for i, k in enumerate(sentence):
        if len(k) >= 5:
            sentence[i] = ''.join(reversed(k))

    return ' '.join(sentence)
