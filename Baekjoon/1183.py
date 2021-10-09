n = int(input())
answer = []
for _ in range(n):
    a, b = map(int, input().split())
    answer.append(a-b)
answer.sort()
if n % 2 == 1:
    print(1)
else:
    print(answer[n//2] - answer[n//2 - 1] + 1)
