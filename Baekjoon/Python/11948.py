sci = []
for i in range(4):
    A = int(input())
    sci.append(A)
sci.sort()

E = int(input())
F = int(input())

print(sci[1] + sci[2] + sci[3] + max(E, F))