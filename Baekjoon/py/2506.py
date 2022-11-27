N = int(input())
p = input().split()
score = 0
count = 0
for i in p:
    if i == "1":
        if count == 0:
            score += 1
            count = 1

        else:
            count += 1
            score += count
    elif i == "0":
        count = 0
print(score)