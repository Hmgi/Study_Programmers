a, b, c = map(int, input().split())
count_1 = 0
count_2 = 0
for i in a, b, c:
    if i == 1:
        count_1 += 1
    else:
        count_2 += 1
if count_1 > count_2:
    print(1)
else:
    print(2)