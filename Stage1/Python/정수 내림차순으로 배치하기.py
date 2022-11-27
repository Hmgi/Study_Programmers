def solution(n):
    n = str(n)
    answer = ''
    lst = []

    for i in n:
        lst.append(i)

    for i in range(len(lst)):
        answer = answer + max(lst)
        lst.remove(max(lst))

    answer = int(answer)
    return answer

print(solution(118372))