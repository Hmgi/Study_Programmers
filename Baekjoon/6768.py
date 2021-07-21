def factor(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


answer = 0
n = int(input())
if n - 3 <= 0:
    print(0)
else:
    while n != 3:
        answer += factor(n-3)
        n -= 1
    print(answer)
