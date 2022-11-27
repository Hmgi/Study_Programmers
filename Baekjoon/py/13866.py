A = list(map(int, input().split()))
A.sort()
B = A[3] + A[0]
C = A[1] + A[2]
print(B-C if B-C >= 0 else C-B)