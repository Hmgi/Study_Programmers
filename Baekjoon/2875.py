n, m, k = map(int, input().split())

max_team = (n + m - k) // 3

for i in range(max_team, -1, -1):
    if 2 * i <= n and i <= m and 3 * i + k <= n + m:
        print(i)
        break
