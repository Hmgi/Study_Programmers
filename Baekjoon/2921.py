n = int(input())
count = 0
for i in range(n + 1):
    for j in range(i + 1):
        count += i + j
print(count)