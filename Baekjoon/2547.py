t = int(input())

for _ in range(t):
    space = input()

    candy = 0
    n = int(input())
    for _ in range(n):
        candy += int(input())
    if candy % n == 0:
        print("YES")
    else:
        print("NO")