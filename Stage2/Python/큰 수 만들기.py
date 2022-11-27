def solution(number, k):
    temp = []

    for i in number:
        while k > 0 and len(temp) != 0 and temp[-1] < i:
            temp.pop()
            k -= 1
        temp.append(i)
    return str("".join(temp[:len(number) - k]))


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
