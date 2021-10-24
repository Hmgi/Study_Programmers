n = int(input())

arr = [input().split() for _ in range(n)]

max_friend = 0
leader = 0

for i in range(n):
    count = 0
    for j in range(5):
        for k in range(n):
            if i != k and arr[k][j] == arr[i][j]:
                count += 1
        if max_friend < count:
            max_friend = count
            leader = i + 1
if leader == 0:
    print(leader + 1)
print(leader)