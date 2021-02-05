import sys
a = int(sys.argv[1])
b = []
c = 0
e = 1
for x in range(a):
    c+=1
    if c == a:
        for x in range(e):
            b.append("*")
        pass
    else:
        for x in range(a-c):
            b.append(" ")
        for x in range(e):
            b.append("*")
        for x in range(a - c):
            b.append(" ")
        e = e+2
c = 0
d = (a*2)-1
for x in range(a):
    print("".join(b[c:d]))
    c = c + ((a*2)-1)
    d = d + ((a*2)-1)
c = c - ((a * 2) - 1)
d = d - ((a * 2) - 1)
for x in range(a):
    c = c - ((a * 2) - 1)
    d = d - ((a * 2) - 1)
    print("".join(b[c:d]))