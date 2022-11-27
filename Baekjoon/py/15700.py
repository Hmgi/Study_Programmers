N, M = map(int, input().split())
count = 0

while max(N, M) // 2 != 0:
    nm_max = max(N, M)
    count += nm_max // 2 * min(N, M)
    if N > M:
        N -= nm_max // 2 * 2
    else:
        M -= nm_max // 2 * 2
print(count)