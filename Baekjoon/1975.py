import sys
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    answer = 0
    for i in range(2, n + 1):
        x = n
        while x:
            if x % i == 0:
                answer += 1
                x //= i
            else:
                break
    print(answer)