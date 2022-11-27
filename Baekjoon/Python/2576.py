number = []
for _ in range(7):
    n = int(input())
    if n % 2 != 0:
        number.append(n)

if len(number) != 0:
    print(sum(number))
    print(min(number))
else:
    print(-1)