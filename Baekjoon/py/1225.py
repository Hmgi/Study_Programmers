A, B = map(str, input().split())
answer = 0
for i in A:
    for j in B:
        answer += int(i) * int(j)
print(answer)