import time

start = time.time() ## точка отсчета времени

def top_3_words(text):
    text = text.lower()
    TopOne, TopTwo, TopThree = [0, ''], [0, ''], [0, '']

    liquid: str = "abcdefghijklmnopqrstuvwxyz' "

    # Проверка на содержание левых символов
    for i in text:
        if i not in liquid:
            text = text.replace(i, ' ')

    # Разделение слво по элементам массивов без лишних пробелов
    text: list = text.split()

    # Проверка, не является ли строка целиком из апострофов
    for i in text:
        for k in range(len(i)):
            if k == len(i)-1:
                if i[k] == "'":
                    text.remove(i)
            elif i[k] == "'":
                continue
            else:
                break

    # Созание словаря для отслеживания топ по стратегии Слово: Количество вхождений
    counter = {}

    # Заполнение словаря по стратегии
    for k in text:
        if k in counter.keys():
            counter[k] += 1
        else:
            counter[k] = 1

    # Заполнение топ 3 массива
    for n, l in counter.items():
        if l > TopOne[0]:
            if TopTwo[0] != 0:
                TopThree[1] = TopTwo[1]
                TopThree[0] = TopTwo[0]
            if TopOne[0] != 0:
                TopTwo[1] = TopOne[1]
                TopTwo[0] = TopOne[0]
            TopOne[0] = l
            TopOne[1] = n
        elif l > TopTwo[0]:
            if TopTwo[0] != 0:
                TopThree[1] = TopTwo[1]
                TopThree[0] = TopTwo[0]
            TopTwo[0] = l
            TopTwo[1] = n
        elif l > TopThree[0]:
            TopThree[0] = l
            TopThree[1] = n
        else:
            continue

    # Конечная проверка на количество элементов
    if TopOne[1] == '':
        return []
    elif TopTwo[1] == '':
        return [TopOne[1]]
    elif TopThree[1] == '':
        return [TopOne[1], TopTwo[1]]
    else:
        return [TopOne[1], TopTwo[1], TopThree[1]]


print(top_3_words("  //wont won't won't "))

end = time.time() - start ## собственно время работы программы

print(end) ## вывод времени