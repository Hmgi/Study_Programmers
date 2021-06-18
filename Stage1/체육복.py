def solution(n, lost, reserve):
    answer = 0
    students = [0] * 31

    for x in range(n):
        students[x] = 1

    for lost_student in lost:
        students[lost_student - 1] = 0

    for reserve_student in reserve:
        students[reserve_student - 1] = students[reserve_student - 1] + 1

    for number in range(n):
        if students[number] == 0:
            if students[number - 1] == 2:
                students[number - 1] = students[number - 1] - 1
                students[number] = students[number] + 1
            elif students[number + 1] == 2:
                students[number + 1] = students[number + 1] - 1
                students[number] = students[number] + 1

    for y in students:
        if y >= 1:
            answer = answer + 1

    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
