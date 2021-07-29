A, B = map(int, input().split())
if B < 0:
    print(A//B + 1)
    print(A - (B * (A//B + 1)))
else:
    print(A//B)
    print(A - (B * (A//B)))
