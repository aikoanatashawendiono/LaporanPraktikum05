def reverse(a):
    reverse_a = 0
    while a > 0:
        reverse_a = reverse_a * 10 + a % 10
        a //= 10
    return reverse_a

def main():
    A, B = map(int, input().split())

    A = reverse(A)
    B = reverse(B)

    C = A + B
    print(reverse(C))

main()
