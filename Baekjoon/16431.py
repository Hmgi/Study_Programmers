B = list(map(int, input().split()))
D = list(map(int, input().split()))
J = list(map(int, input().split()))

D_count = max(J[0], D[0]) - min(J[0], D[0]) + max(J[1], D[1]) - min(J[1], D[1])
B_count = max(max(J[0], B[0]) - min(J[0], B[0]), max(J[1], B[1]) - min(J[1], B[1]))
if D_count < B_count:
    print("daisy")
elif D_count > B_count:
    print("bessie")
else:
    print("tie")