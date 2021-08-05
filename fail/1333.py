N, L, D = map(int, input().split())

# N곡을 표시
for i in range(N):
    if D < i * L:
        D *= 2
    if i * L < D < i * L + 5:
        print(D)