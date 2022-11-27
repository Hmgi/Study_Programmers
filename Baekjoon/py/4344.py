C = int(input())
for _ in range(C):
    student = list(map(int, input().split()))
    student_sum, student_avg = 0, 0
    count = 0

    for i in range(1, len(student)):
        student_sum += student[i]
    student_avg = student_sum / student[0]

    for j in range(1, len(student)):
        if student_avg < student[j]:
            count += 1

    print("%0.3f%%" % (count / student[0] * 100))

