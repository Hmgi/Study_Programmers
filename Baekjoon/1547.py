def getIndex(num, set_answer):
    for i in range(3):
        if set_answer[i] == num:
            return i


M = int(input())
answer = [1, 2, 3]
tempX, tempY = 0, 0
for i in range(M):
    X, Y = map(int, input().split())
    tempX = getIndex(X, answer)
    tempY = getIndex(Y, answer)
    temp = answer[tempX]
    answer[tempX] = answer[tempY]
    answer[tempY] = temp
print(answer[0])
