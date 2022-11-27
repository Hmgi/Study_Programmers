def solution(s):
    answer = ''
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    changeString = ''

    for i in s:
        if i.isdigit():
            answer += i

        else:
            changeString += i
            # 문자열을 채우다가 해당 문자열이 words 안에 있을 경우 문자 판별
            if changeString in words:
                for j in range(len(words)):
                    if changeString == words[j]:
                        answer += str(j)
                        changeString = ''

    # 문자열 정답을 정수형으로 형변환
    return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))

# 연속 2개의 문자가 나올 경우 판별 불가
