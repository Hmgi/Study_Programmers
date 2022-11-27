P, K = map(int, input().split())

a = [False, False] + [True] * (K - 2)
for i in range(2, int(K ** 0.5) + 1):
    if a[i]:
        for j in range(i * 2, K, i):
            if a[j]:
                a[j] = False
flag = True
for i in range(2, K):
    if a[i]:
        if P % i == 0:
            flag = False
            break

if flag:
    print("GOOD")
else:
    print("BAD", i)