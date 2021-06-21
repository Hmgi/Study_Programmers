def solution(s):
    answer = ''

    #짝수
    if len(s) % 2 == 0:
        answer = s[int(len(s)/2)-1:int(len(s)/2)+1]
    #홀수
    else:
        answer = s[int(len(s)/2):int(len(s)/2)+1]

    return answer


print(solution("abcde"))
print(solution("qwer"))
