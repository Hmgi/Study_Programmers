def BW_board(y, x, chess_board):
    answer = ["WBWBWBWB", "BWBWBWBW"]
    before_color = chess_board[0][0]
    count = 0
    for i in range(y, y + 8):
        for j in range(x, x + 8):
            if before_color == "W":
                if answer[0][j - x] != chess_board[i][j]:
                    count += 1
            elif before_color == "B":
                if answer[1][j - x] != chess_board[i][j]:
                    count += 1
        if before_color == "W":
            before_color = "B"
        else:
            before_color = "W"
    return count


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

