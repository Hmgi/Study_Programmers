n = int(input())
a = list(map(int, input().split()))
a.sort()
sum = 0
min = 0

for i in range(a[0], a[len(a)-1] + 1):
    for j in range(n):
       sum += (i - a[j])

    if min > sum:
        min = sum
        minHouse = i

print(minHouse)