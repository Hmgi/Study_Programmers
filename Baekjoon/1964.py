n = int(input())
answer = 5
for i in range(1, n):
    answer += 3 * i + 4
print(answer % 45678)