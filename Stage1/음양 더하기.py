def solution(absolutes, signs):
    answer = 0
    count = 0
    for sign in signs:
        if sign:
            answer += absolutes[count]
        else:
            answer -= absolutes[count]
        count += 1

    return answer


print(solution([4, 7, 12], [True, False, True]))
print(solution([1, 2, 3], [False, False, True]))