def solution(x):
    x = str(x)
    xsum = 0
    for i in range(len(x)):
        xsum = xsum + int(x[i])

    if int(x) % xsum == 0:
        answer = True
    else:
        answer = False

    return answer

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))