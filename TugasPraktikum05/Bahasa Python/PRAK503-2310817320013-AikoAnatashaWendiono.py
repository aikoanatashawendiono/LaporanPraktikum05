def minimal(a, b):
    return a if a < b else b

def maksimal(a, b):
    return a if a > b else b

def main():
    n = int(input())
    bil = list(map(int, input().split()))

    maks = -100000
    minim = 100000

    for nilai in bil:
        maks = maksimal(maks, nilai)
        minim = minimal(minim, nilai)

    print(f"{maks} {minim}")

main()
