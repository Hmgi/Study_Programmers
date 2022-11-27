A, B = map(int, input().split())
C = int(input())
B += C
if B // 60 != 0:
    A += (B // 60)
    if A >= 24:
        A -= 24
    B = B - (60 * (B // 60))
print(A, B)