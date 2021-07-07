def solution(N, stages):
    answer = []
    count = 0
    # 전체 플레이어 수
    maxPlayer = len(stages)
    stages.sort()

    while stages[0] == NULL:
        RoundNumber = stages[0]

        for i in stages:
            if i == RoundNumber:
                count += 1

        answer.append(count / len(stages))
        stages.remove(RoundNumber)
        print(stages[0])

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
