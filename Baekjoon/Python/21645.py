n, m, k = map(int, input().split())
if m < k:
    print(int(n*m))
else:
    print(int(n * ((k - 1) + m // k)))