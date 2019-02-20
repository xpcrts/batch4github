from operator import itemgetter, attrgetter

l = []
for n in range (1, 4):
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print (sorted(l))


a = [1,2,3,4,54,4,24,1,3,74,35,24,3,1,68,9,42,8]

def max_order():
    b = []
    cont = 0
    max = a[0]
    for i in a:
        cont += 1
        if a[cont] > max:
            max = a[cont]
            b.append(max)
    return b

max_order()