f1 = int(input())
f2 = int(input())
f3 = int(input())
Time = 0
# 1층일 때
minTime = f3 * 4 + f2 * 2

# 2층일 때
Time = f1 * 2 + f3 * 2
if minTime > Time:
    minTime = Time

# 3층일 때
Time = f1 * 4 + f2 * 2
if minTime > Time:
    minTime = Time

print(minTime)
