def solution(lottos, win_nums):
    answer = []
    count = 0
    zeroCount = 0
    scores = [6, 6, 5, 4, 3, 2, 1]
    for lotto in lottos:
        # 2중 반복문 보다 배열 안에 확인할 수 있으면 더 효율적으로 보임
        if lotto in win_nums:
            count += 1
        if lotto == 0:
            zeroCount += 1

    answer.append(scores[count + zeroCount])
    answer.append(scores[count])

    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
