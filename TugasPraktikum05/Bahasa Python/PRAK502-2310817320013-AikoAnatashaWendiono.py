def hitung(nilai1, nilai2):
    return nilai1 - nilai2

def mutlak(bil):
    return -bil if bil < 0 else bil

a, c, b, d = map(int, input().split())

hasil = mutlak(hitung(a, b)) + mutlak(hitung(c, d))

print(hasil)
