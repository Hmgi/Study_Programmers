def solution(progresses, speeds):
    answer = []
    temp = []
    count = 0
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] != 0:
            temp.append((100 - progresses[i]) // speeds[i] + 1)
        else:
            temp.append((100 - progresses[i]) // speeds[i])

    day = temp[0]
    for i in temp:
        if day >= i:
            count += 1
        else:
            answer.append(count)
            day = i
            count = 1
    answer.append(count)
    return answer


#print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([96, 94], [3, 3]))