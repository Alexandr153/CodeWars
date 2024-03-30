def f(num):
    if num == '':
        return False
    else:
        return True


def decode(m):
    m = m.split(m[0])
    m = list(filter(f, m))
    m.reverse()

    alpha = 'a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z. '.split('.')
    dict = '/\\.]3.(.|).[-./=.(_,.|-|.|._T./<.|_.|\\/|.|\\|.().|^.()_./?._\\~.~|~.|_|.\\/.\\/\\/.><.`/.~/_.__'.split('.')

    c = []
    for i in m:
        c.append(dict.index(i))

    res = []
    for n in c:
        res.append(alpha[n])
    res = ''.join(res)

    return res




#decode("]()]|_]|_]][-]|-|]") #'hello'
#decode('{|^{|{{|_{]3{'), #'blip'
#decode('..[-.|_.|^....().[-.|^.__..|)...|.|^.|_|..~|~._\\~.__...[-..|.|)..') #'die stupid people'
#decode("'''_\\~'|_|'()'|''('|'|_'[-'|)''__'_\\~'/<'()'()'|_'''__'|\\|'|''/\\'/?']3'__''/?'|_|''()'`/''")  #'your brain looks delicious'
#decode('}/\\}~|~}/\\}/<}__}|)}}}[-}~|~}/\\}(}|}|_}|^}|_|}|)}__}|)}}}|\\|}|}/=}__}()}}}~|~}__}`/}/?}}~|~}') #'try to find duplicated kata'