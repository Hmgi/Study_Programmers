T = int(input())
A = list(map(int, input().split()))
count = 0
for i in A:
    if T == i:
        count += 1
print(count)