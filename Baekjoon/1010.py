def fact(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


T = int(input())
answer = []
for _ in range(T):
    n, m = map(int, input().split())
    answer.append(fact(m) // (fact(n) * fact(m-n)))

for i in answer:
    print(i)