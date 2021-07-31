X, L, R = map(int, input().split())
if L <= R <= X:
    print(R)
elif X <= L <= R:
    print(L)
elif L <= X <= R:
    print(X)