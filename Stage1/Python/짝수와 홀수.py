def solution(num):
    answer = ''

    if num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"

    return answer

print(solution(2))
print(solution(3))