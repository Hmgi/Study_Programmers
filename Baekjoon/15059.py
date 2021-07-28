C = list(map(int, input().split()))
B = list(map(int, input().split()))
count = 0
for i in range(3):
    if C[i] < B[i]:
        count += B[i] - C[i]
print(count)