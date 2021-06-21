def solution(string, n):
    answer = []
    for word in string:
        word = word[n] + word
        answer.append(word)
    answer.sort()
    for i in range(len(answer)):
        answer[i] = answer[i][1:]

    return answer


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))
