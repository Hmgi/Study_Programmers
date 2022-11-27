while True:
    count = 1
    N = list(map(int, input().split()))
    if N[0] == 0:
        break
    for i in range(N[0]):
        if N[2 * i + 2] == 0:
            count *= N[2 * i + 1]
        else:
            count *= N[2 * i + 1]
            count -= N[2 * i + 2]
    print(count)