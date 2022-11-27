n = list(map(int, input().split()))
n.sort()
if n[0] == n[1] and n[0] == n[2]:
    print(10000 + n[0] * 1000)
elif n[0] == n[1] or n[1] == n[2]:
    print(1000 + n[1] * 100)
else:
    print(max(n) * 100)
