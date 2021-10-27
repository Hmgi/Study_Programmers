x, y = map(int, input().split())

min_money = x / y * 1000

n = int(input())
for _ in range(n):
    x1, y1 = map(int, input().split())
    calc = x1 / y1 * 1000
    if min_money > calc:
        min_money = calc
print(min_money)