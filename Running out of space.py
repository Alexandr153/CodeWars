def spacey(array):
    mas = []
    temp = ''
    for i in array:
        temp += i
        mas.append(temp)
    return mas


print(spacey(['kevin', 'has','no','space']))


# test.assert_equals(spacey(['kevin', 'has','no','space']), [ 'kevin', 'kevinhas', 'kevinhasno', 'kevinhasnospace'])
# test.assert_equals(spacey(['this','cheese','has','no','holes']), ['this','thischeese','thischeesehas','thischeesehasno','thischeesehasnoholes'])
#ок