def Biodata(tahunLahir, nama, asal):
    tahunSekarang = 2023
    umur = tahunSekarang - tahunLahir

    print(f"Perkenalkan Nama Saya : {nama}")
    print(f"Umur Saya : {umur}")
    print(f"Saya Adalah Angkatan : {tahunSekarang}")
    print(f"Asal Saya dari : {asal}")

def output():
    tahunLahir = int(input())
    nama = input()
    asal = input()

    Biodata(tahunLahir, nama, asal)

output()
