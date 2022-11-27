def solution(N, stages):
    answer = []
    temp = []
    user = len(stages)

    for i in range(1, N + 1):
        fail = 0
        for j in range(len(stages)):
            if stages[j] == i:
                fail += 1
        if fail == 0:
            temp.append(0)
        else:
            temp.append(fail / user)
        user -= fail

    a = sorted(temp, reverse=True)

    for i in range(len(a)):
        answer.append(temp.index(a[i]) + 1)
        temp[temp.index(a[i])] = -1

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
'''
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
'''
