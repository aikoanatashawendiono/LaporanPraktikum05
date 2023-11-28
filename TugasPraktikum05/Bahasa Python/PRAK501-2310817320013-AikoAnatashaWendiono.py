def MaxBilangan(a, b, c, d):
    bil = a

    if (b > bil):
        bil = b

    if (c > bil):
        bil = c

    if (d > bil):
        bil = d

    return bil

def bilangan():
    a, b, c, d = map(int, input().split())
    hasil = MaxBilangan(a, b, c, d)
    print(hasil)

bilangan()
