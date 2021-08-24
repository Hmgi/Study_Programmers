def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < N and 0 <= w < M and S[q][w] == 1:
                S[q][w] = 0
                queue.append([q, w])


T = int(input())
for i in range(T):
    M, N, K = map(int, input().split())
    S = [[0] * M for _ in range(N)]
    cnt = 0
    for j in range(K):
        a, b = map(int, input().split())
        S[b][a] = 1
    for q in range(N):
        for w in range(M):
            if S[q][w] == 1:
                bfs(q, w)
                S[q][w] = 0
                cnt += 1
    print(cnt)
