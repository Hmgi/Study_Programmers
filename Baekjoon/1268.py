n = int(input())

arr = [input().split() for _ in range(n)]
answer = []

for i in range(n):
    friend = []
    for j in range(5):
        for k in range(n):
            if i == k:
                continue
            else:
                if arr[i][j] == arr[k][j]:
                    if k not in friend:
                        friend.append(k)
    answer.append(len(friend))
print(answer.index(max(answer)) + 1)