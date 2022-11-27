a = list(map(int, input().split()))
isTrue = False
temp = 1
count = 0
min_num = min(a)

while True:
    for i in range(5):
        if min_num % a[i] == 0:
            count += 1
            if count == 3:
                isTrue = True

    if isTrue:
        print(min_num)
        break
    else:
        min_num += 1
        count = 0