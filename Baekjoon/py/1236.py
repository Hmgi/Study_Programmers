n, m = map(int, input().split())

answer = []

for i in range(n):
    answer.append(input())

x_count, y_count = 0, 0

for i in range(n):
    if "X" not in answer[i]:
        x_count += 1

for j in range(m):
    if "X" not in [answer[i][j] for i in range(n)]:
        y_count += 1

print(max(x_count, y_count))