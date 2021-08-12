def solution(s):
    answer = ''
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for idx, num in enumerate(words):
        if num in s:
            s = s.replace(num, str(idx))
        answer = s
    return int(answer)