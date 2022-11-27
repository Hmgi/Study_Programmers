def solution(s):
    answer = ''
    count = 0
    for i in s:
        if count % 2 == 0 and i != ' ':
            i = i.upper()
            count = count + 1

        elif i == ' ':
            count = 0

        else:
            i = i.lower()
            count = count + 1

        answer = answer + i

    return answer


print(solution("try hello world"))