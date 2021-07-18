KOI = list(map(int, input().split()))
GOU = 0
for i in KOI:
    GOU += i**2
GOU %= 10
print(GOU)
