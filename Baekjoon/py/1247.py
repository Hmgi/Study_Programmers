from sys import stdin

for i in range(3):
    count = 0
    N = int(stdin.readline())
    for j in range(N):
        count += int(stdin.readline())
    if count < 0:
        print("-")
    elif count == 0:
        print(0)
    else:
        print("+")