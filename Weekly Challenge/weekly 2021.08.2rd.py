def make(student, num):
    min_score = min(student)
    max_score = max(student)

    if min_score == student[num]:
        student.remove(min_score)
        if min_score in student:
            student.append(min_score)
    elif max_score == student[num]:
        student.remove(max_score)
        if max_score in student:
            student.append(max_score)

    sum = 0

    for i in student:
        sum += i

    avg = sum / len(student)

    if 90 <= avg:
        return "A"
    elif 80 <= avg < 90:
        return "B"
    elif 70 <= avg < 80:
        return "C"
    elif 50 <= avg < 70:
        return "D"
    else:
        return "F"


def solution(scores):
    answer = ''
    temp = []

    # 인원 수
    count = len(scores)

    for j in range(count):
        for i in range(count):
            temp.append(scores[i][j])
        answer += make(temp, j)
        temp = []
    return answer


print(solution(
    [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))
print(solution([[50, 90], [50, 87]]))
