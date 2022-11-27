a = int(input())  # 인원수
d = int(input())  # 기준 득표 수
if a == 1:
    print(0)
else:
    temp = []  # 기준을 제외한 나머지 사람들 득표 수
    for i in range(a - 1):
        temp.append(int(input()))

    count = 0
    while d <= max(temp):
        temp[temp.index(max(temp))] -= 1
        d += 1
        count += 1
    print(count)

