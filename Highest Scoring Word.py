word = 'kfksdf sdsllf dsf ldfs'
a = 'abcdefghijklmnopqrstuvwxyz'
c = {}
_max = {'word': "", "counter": 0}

for i, k in enumerate(a):
    c[k] = i+1

for i in word.split():
    _sum = 0
    for k in i:
        _sum += c[k]
    if _sum > _max['counter']:
        _max['counter'], _max['word'] = _sum, i

print(_max["word"])