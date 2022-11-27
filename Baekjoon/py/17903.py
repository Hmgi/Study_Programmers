a, b = map(int, input().split())
for _ in range(a):
    c, d, e = map(int, input().split())
print("unsatisfactory" if a < 8 else "satisfactory")