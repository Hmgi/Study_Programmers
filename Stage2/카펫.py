def solution(brown, yellow):
    answer = []
    for i in range(2, max(brown, yellow)):
        if (brown + yellow) % i == 0:
            a = (brown + yellow) // i
            if (a - 2) * (i - 2) == yellow:
                answer.append(max(a, i))
                answer.append(min(a, i))
                break

    return answer


print(solution(10, 2))  # 4, 3
print(solution(8, 1))  # 3, 3
print(solution(24, 24))  # 8, 6
