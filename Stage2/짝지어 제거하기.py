def solution(s):
    answer = -1
    lastWord = ''
    s = list(s)
    for i in s:
        if lastWord == i:
            print(s)
            s.remove(lastWord)
            s.remove(i)
            solution(s)
        else:
            lastWord = i


    if s == "":
        answer = 1

    else:
        answer = 0

    return answer


print(solution("baabaa"))
print(solution("cdcd"))
