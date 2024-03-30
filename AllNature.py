array = []
for i in range(1, 1000 + 1):
    for n in range(2, i + 1):
        if i % n > 0:
            continue
        elif n == i:
            array.append(i)
        else:
            break

print(array[1:40])
print(array[40:80])
print(array[80:120])
print(array[120:160])
print(array[160:200])

