def BW_board(y, x, chess_board):
    answer = ["WBWBWBWB", "BWBWBWBW"]
    before_color = chess_board[y][x]
    a_count, b_count = 0, 0
    for i_a in range(y, y + 8):
        for j_a in range(x, x + 8):
            if (i_a - y) % 2 == 0:
                if answer[0][j_a - x] != chess_board[i_a][j_a]:
                    a_count += 1
            elif (i_a - y) % 2 != 0:
                if answer[1][j_a - x] != chess_board[i_a][j_a]:
                    a_count += 1

    for i_b in range(y, y + 8):
        for j_b in range(x, x + 8):
            if (i_b - y) % 2 == 0:
                if answer[1][j_b - x] != chess_board[i_b][j_b]:
                    b_count += 1
            elif (i_b - y) % 2 != 0:
                if answer[0][j_b - x] != chess_board[i_b][j_b]:
                    b_count += 1
    return min(a_count, b_count)


N, M = map(int, input().split())
chess_board = [0 for _ in range(N)]
for i in range(N):
    chess_board[i] = list(map(str, input()))
min_count = 64
for y in range(N - 7):
    for x in range(M - 7):
        count = BW_board(y, x, chess_board)
        if min_count > count:
            min_count = count
print(min_count)

