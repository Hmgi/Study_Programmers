X, Y = map(int, input().split())
print(Y // (Y - X) if Y % (Y - X) == 0 else Y // (Y - X) + 1)