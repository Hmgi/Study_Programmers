n = int(input())
num = 3
for i in range(1, n):
    num += (2 ** i)
print(num ** 2)