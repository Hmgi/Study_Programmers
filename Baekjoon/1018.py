def BW_board(y, x, chess_board):
    answer = ["WBWBWBWB", "BWBWBWBW"]
    before_color = chess_board[y][x]
    a_count, b_count = 0, 0
    for i in range(y, y + 8):
        for j in range(x, x + 8):
            if (i - y) % 2 == 0:
                if answer[0][j - x] != chess_board[i][j]:
                    a_count += 1
                if answer[1][j - x] != chess_board[i][j]:
                    b_count += 1
            elif (i - y) % 2 != 0:
                if answer[1][j - x] != chess_board[i][j]:
                    a_count += 1
                if answer[0][j - x] != chess_board[i][j]:
                    b_count += 1
    return min(a_count, b_count)


N, M = map(int, input().split())
chess_board = [0 for _ in range(N)]
for i_chess in range(N):
    chess_board[i_chess] = list(map(str, input()))
min_count = 64
for y in range(N - 7):
    for x in range(M - 7):
        count = BW_board(y, x, chess_board)
        if min_count > count:
            min_count = count
print(min_count)

