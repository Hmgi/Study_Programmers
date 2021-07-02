def solution(n):
    answer = ''

    for i in range(n):
        if i % 2 == 0 or i == 0:
            answer = answer + "수"
        else:
            answer = answer + "박"
    return answer


print(solution(3))
print(solution(4))