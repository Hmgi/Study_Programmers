chess = [0 for _ in range(8)]
answer = ["01010101", "10101010"]
count = 0
for i in range(8):
    chess[i] = input()

    for j in range(8):
        if i % 2 == 0 and chess[i][j] == "F" and answer[0][j] == "0":
            count += 1
        elif i % 2 != 0 and chess[i][j] == "F" and answer[1][j] == "0":
            count += 1
print(count)
