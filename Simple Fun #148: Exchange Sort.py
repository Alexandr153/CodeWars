def find_value(value: int, start: int, end: int, secondStart: int, secondEnd: int, sequence: list, counter: int) -> bool:
    try:
        index = sequence.index(value, start, end)
        sequence[index], sequence[counter] = sequence[counter], value
        return True
    except ValueError:
        try:
            index = sequence.index(value, secondStart, secondEnd)
            sequence[index], sequence[counter] = sequence[counter], value
            return True
        except ValueError: return False


def exchange_sort(sequence: list) -> int:
    counter, sevenCounter = 0, sequence.count(7)
    eightCounter = sequence.count(8) + sevenCounter
    nineCounter = sequence.count(9) + eightCounter
    for i in range(len(sequence)-1):
        if i < sevenCounter:
            if sequence[i] == 7:
                continue
            elif sequence[i] == 8:
                if find_value(7, sevenCounter, eightCounter, eightCounter, nineCounter, sequence, i) is True: counter += 1
            elif sequence[i] == 9:
                if find_value(7, eightCounter, nineCounter, sevenCounter, eightCounter, sequence, i) is True: counter += 1
        elif i < eightCounter:
            if sequence[i] == 8:
                continue
            elif sequence[i] == 7:
                if find_value(8, 0, sevenCounter, eightCounter, nineCounter, sequence, i) is True: counter += 1
            elif sequence[i] == 9:
                if find_value(8, eightCounter, nineCounter, 0, sevenCounter, sequence, i) is True: counter += 1
        elif i < nineCounter:
            if sequence[i] == 9:
                continue
            elif sequence[i] == 7:
                if find_value(9, 0, sevenCounter, sevenCounter, eightCounter, sequence, i) is True: counter += 1
            elif sequence[i] == 8:
                if find_value(9, sevenCounter, eightCounter, 0, sevenCounter, sequence, i) is True: counter += 1
    return counter
