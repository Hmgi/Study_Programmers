a, b = map(int, input().split())
answer = []
for i in range(1, 46):
    answer += [i] * i

print(sum(answer[a-1:b]))