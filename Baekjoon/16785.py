A, B, C = map(int, input().split())
count = 0
num = 1
while True:
    count += A
    if num % 7 == 0:
        count += B
    if count >= C:
        print(num)
        break
    num += 1