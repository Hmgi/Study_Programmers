A = []
for i in range(3):
    a = int(input())
    A.append(a)
A.sort()
if sum(A) == 180:
    if A[0] == A[1] == A[2] == 60:
        print("Equilateral")
    elif A[0] == A[1] or A[1] == A[2]:
        print("Isosceles")
    elif A[0] != A[1] and A[1] != A[2]:
        print("Scalene")
else:
    print("Error")