n, m = map(int, input().split())
p = []
for _ in range(m):
    p.append(int(input()))
p.sort(reverse=True)
max_money = 0
max_cost = 0
for idx, i in enumerate(p):
    if idx + 1 <= n:
        if (idx + 1) * i > max_money:
            max_money = (idx + 1) * i
            max_cost = i
    else:
        break
print(max_cost, max_money)
