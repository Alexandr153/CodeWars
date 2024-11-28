def exchange_sort(sequence: list) -> int:
    sequenceCopy = sequence.copy()
    counter = 0
    counter2 = 0
    sevenCounter = sequence.count(7)
    eightCounter = sequence.count(8) + sevenCounter
    nineCounter = sequence.count(9) + eightCounter
    for i in range(len(sequence)-1):
        if i < sevenCounter:
            if sequence[i] == 7:
                continue
            else:
                for k in range(sevenCounter, eightCounter):
                    if sequence[k] == 7:
                        counter += 1
                        sequence[k] = sequence[i]
                        sequence[i] = 7
                        break
                else:
                    for n in range(eightCounter, nineCounter):
                        if sequence[n] == 7:
                            counter += 1
                            sequence[n] = sequence[i]
                            sequence[i] = 7
                            break
        elif i < eightCounter:
            if sequence[i] == 8:
                continue
            else:
                for k in range(0, sevenCounter):
                    if sequence[k] == 8:
                        counter += 1
                        sequence[k] = sequence[i]
                        sequence[i] = 8
                        break
                else:
                    for n in range(eightCounter, nineCounter):
                        if sequence[n] == 8:
                            counter += 1
                            sequence[n] = sequence[i]
                            sequence[i] = 8
                            break
        elif i < nineCounter:
            if sequence[i] == 9:
                continue
            else:
                for k in range(0, sevenCounter):
                    if sequence[k]:
                        counter += 1
                        sequence[k] = sequence[i]
                        sequence[i] = 9
                        break
                else:
                    for n in range(sevenCounter, eightCounter):
                        if sequence[n] == 9:
                            counter += 1
                            sequence[n] = sequence[i]
                            sequence[i] = 9
                            break

    for i in range(len(sequenceCopy)-1, 0, -1):
        if i < sevenCounter:
            if sequenceCopy[i] == 7:
                continue
            else:
                for k in range(sevenCounter, eightCounter):
                    if sequenceCopy[k] == 7:
                        counter2 += 1
                        sequenceCopy[k] = sequenceCopy[i]
                        sequenceCopy[i] = 7
                        break
                else:
                    for n in range(eightCounter, nineCounter):
                        if sequenceCopy[n] == 7:
                            counter2 += 1
                            sequenceCopy[n] = sequenceCopy[i]
                            sequenceCopy[i] = 7
                            break
        elif i < eightCounter:
            if sequenceCopy[i] == 8:
                continue
            else:
                for k in range(0, sevenCounter):
                    if sequenceCopy[k] == 8:
                        counter2 += 1
                        sequenceCopy[k] = sequenceCopy[i]
                        sequenceCopy[i] = 8
                        break
                else:
                    for n in range(eightCounter, nineCounter):
                        if sequenceCopy[n] == 8:
                            counter2 += 1
                            sequenceCopy[n] = sequenceCopy[i]
                            sequenceCopy[i] = 8
                            break
        elif i < nineCounter:
            if sequenceCopy[i] == 9:
                continue
            else:
                for k in range(0, sevenCounter):
                    if sequenceCopy[k] == 9:
                        counter2 += 1
                        sequenceCopy[k] = sequenceCopy[i]
                        sequenceCopy[i] = 9
                        break
                else:
                    for n in range(sevenCounter, eightCounter):
                        if sequenceCopy[n] == 9:
                            counter2 += 1
                            sequenceCopy[n] = sequenceCopy[i]
                            sequenceCopy[i] = 9
                            break
    return counter if counter < counter2 else counter2


print(exchange_sort([9, 9, 7, 7, 9, 8, 8, 9, 9, 7, 9, 8, 7, 7, 9, 9, 8, 8, 8, 7, 8, 7, 9, 7, 7, 8, 9, 7, 7, 8, 8, 9, 8, 8, 9]))


