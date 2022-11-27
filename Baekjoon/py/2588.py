A = str(input())
B = str(input())
for i in range(len(B) - 1, -1, -1):
    print(int(A) * int(B[i]))
print(int(A) * int(B))