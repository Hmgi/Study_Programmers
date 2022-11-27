def solution(s):
    answer = True
    ycount = 0
    pcount = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            pcount += 1
        if s[i] == 'y' or s[i] == 'Y':
            ycount += 1
    if ycount == pcount:
        answer = True
    else:
        answer = False

    return answer


print(solution("pPoooyY"))
print(solution("Pyy"))
