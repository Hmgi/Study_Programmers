n = int(input())
a = list(map(int, input().split()))

a.sort()

sum = 0

for i in range(n):
    if sum + 1 >= a[i]:
        sum += a[i]

    else:
        break

print(sum + 1)