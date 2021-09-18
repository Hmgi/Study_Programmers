n = int(input())

for i in range(n):
    print(" " * (-1 * i + n - 1), end='')
    print("*" * (2 * i + 1))

for j in range(n-1):
    print(" " * (j + 1), end='')
    print("*" * ((-1 * j + n - 2) * 2 + 1))