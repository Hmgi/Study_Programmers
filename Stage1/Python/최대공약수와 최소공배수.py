def solution(n, m):
    answer = []
    maxnum = 0

    # 최대공약수
    for i in range (1, n+1):
        if n % i == 0 and m % i == 0 and maxnum < i:
            maxnum = i

    answer.append(maxnum)

    # 최소공배수
    for i in range (m, n*m+1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break

    return answer


print(solution(3,12))
print(solution(2,5))