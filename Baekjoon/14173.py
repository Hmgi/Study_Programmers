A = list(map(int, input().split()))
B = list(map(int, input().split()))
x = max(A[2], B[2]) - min(A[0], B[0])
y = max(A[3], B[3]) - min(A[1], B[1])
print(max(x, y) ** 2)