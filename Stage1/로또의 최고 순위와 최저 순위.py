def solution(lottos, win_nums):
    answer = []
    count = 0
    zeroCount = 0
    scores = [6, 6, 5, 4, 3, 2, 1]
    for lotto in lottos:
        for win_num in win_nums:
            if lotto == 0:
                zeroCount += 1
                break
            elif lotto == win_num:
                count += 1

    answer.append(scores[count + zeroCount])
    answer.append(scores[count])

    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
