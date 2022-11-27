k = int(input())
if 100 < k * 0.01 + 25 < 2000:
    print(k * 0.01 + 25)
elif 100 >= k * 0.01 + 25:
    print(100)
else:
    print(2000)