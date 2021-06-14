def romb(oldv):
    v = int(oldv)
    znak = "*"
    n = int(v - 2)
    m = int(v)
    s = []
    z = v * 2 - 1 
    for i in range (z):
            s.append([' '] * z)
    s[0][v - 1] = znak
    s[z - 1][v - 1] = znak
    for i in range (z):
        for j in range (z):
            if i != 0 and i != z - 1:
                s[i][n] = znak
                s[i][m] = znak
        if i != 0 and i < v - 1:
            m += 1
            n -= 1
        if i != z - 1 and i >= v - 1:
            m -= 1
            n += 1
    return s


def output(s, v):
    for i in range (v * 2 - 1):
        for j in range (v * 2 - 1):
            print(s[i][j], end = '')
        print()

v = int(input('Введите сторону ромба: '))
if (v > 0):
    s = romb(v)
    output(s, v)