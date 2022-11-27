L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
if A % C != 0:
    A = A // C + 1
else:
    A //= C

if B % D != 0:
    B = B // D + 1
else:
    B //= D

print(L-max(A, B))