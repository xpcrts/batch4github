

a = [(1,1,1)]
for i in range (1, 4):
    s = input()
    if not s:
        break
    a.append(tuple(s))
a = tuple(a)   
print (a)