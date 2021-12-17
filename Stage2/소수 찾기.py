import itertools


def solution(numbers):

    temp = []
    for i in numbers:
        temp.append(i)

    temp2 = []
    for i in range(len(temp)):
        test = itertools.permutations(temp, i + 1)

        for j in test:
            j = int("".join(j))
            if j != 0 and j != 1 and j not in temp2 and j % 2 != 0:
                temp2.append(j)
            elif j == 2 and j not in temp2:
                temp2.append(j)

    answer = len(temp2)
    # 소수 판별
    for i in temp2:
        for j in range(3, i):
            if i % j == 0:
                answer -= 1
                break

    return answer


print(solution("17")) # 3
print(solution("011")) # 2
print(solution("2")) # 1
print(solution("7843")) # 12
print(solution("9999999")) # 0
#print(solution("1276543")) # 1336
print(solution("232")) # 4