def solution(numbers, hand):
    answer = ''

    for i in numbers:
        if i == 1 or 4 or 7:
            answer += "L"
            lastL = i
        elif i == 3 or 6 or 9:
            answer += "R"
            lastR = i

        # else:
            # Java.키패드 사이의 거리 구하기 실패

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
