N = int(input())
prices = []
for i in range(N):
    a = float(input())
    prices.append(a * 0.8)

for price in prices:
    print("$%.2f" %price)