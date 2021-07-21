def calcTime(name):
    # 초
    if name[5]-name[2] < 0:
        name[4] -= 1
        name[5] += 60
    s = name[5]-name[2]

    # 분
    if name[4]-name[1] < 0:
        name[3] -= 1
        name[4] += 60
    m = name[4]-name[1]

    # 시
    h = name[3]-name[0]

    print(h, m, s)


A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

calcTime(A)
calcTime(B)
calcTime(C)


