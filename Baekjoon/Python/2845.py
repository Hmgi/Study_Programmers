L, P = input().split()
peo = list(map(int, input().split()))
max = int(L) * int(P)
for i in peo:
    i -= max
    print(i, end=' ')