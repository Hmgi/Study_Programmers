A, B = map(str, input().split())
min_count = len(A)
for i in range(len(B) - len(A) + 1):
    count = 0
    for jdx, j in enumerate(A):
        if B[jdx + i] != j:
            count += 1
    if min_count > count:
        min_count = count
print(min_count)
