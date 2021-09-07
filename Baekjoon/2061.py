K, L = map(int, input().split())

if K % 2 == 0 and L > 2:
    print("BAD 2")
else:
    for i in range(3, L, 2):
        if K % i == 0:
            print("BAD %d" %i)
            break
    else:
        print("GOOD")