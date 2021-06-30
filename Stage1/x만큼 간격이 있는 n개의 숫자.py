"""def solution(x, n):
    answer = []

    if x > 0:
        transNum = 1

    else:
        transNum = -1

    for i in range(x, x * n + transNum, x):
        answer.append(i)

    return answer
"""

def solution(x, n):
    answer = []

    for i in range(1, n+1):
        answer.append(x*i)

    return answer

print(solution(2,5))
print(solution(4,3))
print(solution(-4,2))