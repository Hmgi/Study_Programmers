N, A, B, C, D = map(int, input().split())
if N % A != 0:
    A = (N // A) + 1
else:
    A = N // A

if N % C != 0:
    C = (N // C) + 1
else:
    C = N // C

print(min(A * B, C * D))