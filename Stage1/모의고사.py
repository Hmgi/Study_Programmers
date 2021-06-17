def solution(n):
    answer = []

    man1 = [1, 2, 3, 4, 5]
    man2 = [2, 1, 2, 3, 2, 4, 2, 5]
    man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    corrMan1 = 0
    corrMan2 = 0
    corrMan3 = 0

    for ques in range(len(n)):
        if man1[ques%len(man1)] == n[ques]:
            corrMan1 = corrMan1 + 1
        if man2[ques%len(man2)] == n[ques]:
            corrMan2 = corrMan2 + 1
        if man3[ques%len(man3)] == n[ques]:
            corrMan3 = corrMan3 + 1

    maxscore = max(corrMan1, corrMan2, corrMan3)

    if maxscore == corrMan1:
        answer.append(1)
    if maxscore == corrMan2:
        answer.append(2)
    if maxscore == corrMan3:
        answer.append(3)

    return answer


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))