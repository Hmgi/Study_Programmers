def solution(n):
    answer = []
    
    # 1번 사람이 문제를 찍는 패턴
    man1 = [1, 2, 3, 4, 5]
    # 2번 사람
    man2 = [2, 1, 2, 3, 2, 4, 2, 5]
    # 3번 사람
    man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 각각 사람이 문제를 맞춘 수
    corrMan1 = 0
    corrMan2 = 0
    corrMan3 = 0

    # 정답 배열 n 만큼 반복한다.
    # 여기서 사람들 마다 찍는 패턴의 길이가 다르기 때문에 나머지 연산을 사용하여 맞춘 문제 수를 판별한다.
    for ques in range(len(n)):
        if man1[ques%len(man1)] == n[ques]:
            corrMan1 = corrMan1 + 1
        if man2[ques%len(man2)] == n[ques]:
            corrMan2 = corrMan2 + 1
        if man3[ques%len(man3)] == n[ques]:
            corrMan3 = corrMan3 + 1

    # 파이썬의 max 함수를 사용하여 3개의 정수형 변수 중 가장 큰 수를 뽑아 maxscore에 저장한다.
    maxscore = max(corrMan1, corrMan2, corrMan3)

    # 동점일 경우 정답자를 각각 배열에 넣는다.
    if maxscore == corrMan1:
        answer.append(1)
    if maxscore == corrMan2:
        answer.append(2)
    if maxscore == corrMan3:
        answer.append(3)

    return answer


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))