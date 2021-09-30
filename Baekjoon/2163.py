def solve(n, m):
    return (n-1) + n * (m-1)


n, m = map(int, input().split())
print(solve(n, m))
