def solution(left, right):
    answer = 0
    count = 0
    for i in range(left, right + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                count = count + 1

        if count % 2 == 0:
            answer = answer + i
        else:
            answer = answer - i
        count = 0

    return answer


print(solution(13, 17))
print(solution(24, 27))

