def check(num):
    answer = 0
    while True:
        a = num // 2
        b = num % 2
        answer += b
        num = a
        if num == 0:
            break
    return answer


n, k = map(int, input().split())
if k >= n:
    print(0)
else:
    i = n
    while True:
        if check(i) <= k:
            print(i-n)
            break
        else:
            i += 1
