X, Y = map(int, input().split())
if X % 4 == 0:
    X_x = X // 4 - 1
    X_y = 4
else:
    X_x = X // 4
    X_y = X % 4

if Y % 4 == 0:
    Y_x = Y // 4 - 1
    Y_y = 4
else:
    Y_x = Y // 4
    Y_y = Y % 4

print(abs(X_x - Y_x) + abs(X_y - Y_y))