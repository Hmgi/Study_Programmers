A = int(input())
Car = list(map(int, input().split()))
count = 0
for i in Car:
    if i == A:
        count += 1
print(count)