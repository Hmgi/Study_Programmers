n = int(input())

for i in range(n):
    print(" " * i, end='')
    print("*" * ((-1 * i + n - 1) * 2 + 1))

for j in range(n-1):
    print(" " * (-1 * j + n - 2), end='')
    print("*" * (2 * j + 3))