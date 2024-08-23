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
