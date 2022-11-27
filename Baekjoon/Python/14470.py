A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
count = 0
while A != B:
    if A < 0:
        count = count + (0 - A) * C
        A = 0

    elif A == 0:
        count += D
        count = count + (B - A) * E
        A = B

    else:
        count = count + (B - A) * E
        A = B
print(count)