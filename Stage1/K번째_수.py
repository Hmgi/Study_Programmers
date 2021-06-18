def solution(array, commands):
    answer = []
    cutArray = []
    for cut in range(len(commands)):
        cutArray = array[commands[cut][0] - 1:commands[cut][1]]
        cutArray.sort()
        answer.append(cutArray[commands[cut][2] - 1])

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
