l, r = map(int, input().split())
a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

found = False # TODO
x, y, z, t = 0, 0, 0, 0
taras = {e, f}
def oriyentatsii(x1, y1):
    return [(x1, y1), (y1, x1)]

for l_d, p_d in [((a,b),(c,d)),((c,d),(a,b))]:
    for x, y in oriyentatsii(*l_d):
        if y != l:
            continue
        print(x, y, "l_d", l_d)

        for z, t in oriyentatsii(*p_d):
            if z != r:
                continue
            print(z, t, "p_d", p_d)
            if x not in taras and t not in taras:
                found = True
                x, y, z, t = x, y, z, t
                break
        if found:
            break
    if found:
        break
if not found:
    print(-1)
else:
    print(x, y)
    print(z, t)
