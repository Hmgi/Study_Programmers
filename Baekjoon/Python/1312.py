'''A, B, N = map(int, input().split())
C, D = str(A / B).split(".")
if N-1 > len(D):
    print(0)
else:
    print(int(D[N - 1]))
'''
a, b, n = map(int, input().split())
a %= b
for i in range(n-1):
    a = (a*10) % b
print((a*10) // b)