A = []
for i in range(4):
    A.append(int(input()))
if (A[0] == 9 or A[0] == 8) and (A[1] == A[2]) and (A[3] == 9 or A[3] == 8):
    print("ignore")
else:
    print("answer")