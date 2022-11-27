def check_knight(t_x, t_y, n_x, n_y):
    if (abs(t_x - n_x) ** 2) + (abs(t_y - n_y) ** 2) == 5:
        return True
    else:
        return False


chess = [[0, 0, 0, 0, 0, 0] for _ in range(6)]
alpha = {'A': 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}
answer = True
temp_x, temp_y = 0, 0
first_x, first_y = 0, 0

for i in range(36):
    knight = input()
    if i == 0:
        temp_x = alpha[knight[0]]
        temp_y = int(knight[1]) - 1
        first_x = alpha[knight[0]]
        first_y = int(knight[1]) - 1
        chess[temp_x][temp_y] = 1

    else:
        now_x = alpha[knight[0]]
        now_y = int(knight[1]) - 1

        # 나이트가 갈 수 있는 곳인지 체크
        if not check_knight(temp_x, temp_y, now_x, now_y):
            answer = False

        # 이미 해당하는 곳이 한번 들렸던 경우
        if chess[now_x][now_y] == 1:
            answer = False

        if i == 35:
            if not check_knight(first_x, first_y, now_x, now_y):
                answer = False

        chess[now_x][now_y] = 1
        temp_x = now_x
        temp_y = now_y

if answer:
    print("Valid")
else:
    print("Invalid")
