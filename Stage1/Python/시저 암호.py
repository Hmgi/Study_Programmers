def solution(s, n):
    answer = ''

    for i in s:
        # 소문자 일 때
        if ord("a") <= ord(i) <= ord("z"):
            # 더한 수가 z가 넘어 갈 경우
            if ord(i) + n > ord("z"):
                answer = answer + chr(ord(i) + n - ord("z") - 1 + ord("a"))
            else:
                answer = answer + chr(ord(i) + n)

        # 대문자 일 때
        elif ord("A") <= ord(i) <= ord("Z"):
            # 더한 수가 Z가 넘어 갈 경우
            if ord(i) + n > ord("Z"):
                answer = answer + chr(ord(i) + n - ord("Z") - 1 + ord("A"))
            else:
                answer = answer + chr(ord(i) + n)

        elif i == " ":
            answer = answer + " "

    return answer


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))
