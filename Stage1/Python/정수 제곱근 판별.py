def solution(n):
    answer = 0

    n = pow(n, 0.5)

    if n == int(n):
        answer = int((n + 1) ** 2)
    else:
        return -1

    return answer


print(solution(121))
print(solution(-3))
