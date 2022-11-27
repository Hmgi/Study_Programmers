while True:
    a = list(map(int, input().split()))

    if a[0] == a[1] == a[2] == 0:
        break

    a.sort()

    if a[0] + a[1] <= a[2]:
        print("Invalid")

    else:
        if a[0] == a[1] == a[2]:
            print("Equilateral")
        elif a[0] == a[1] or a[1] == a[2]:
            print("Isosceles")
        elif a[0] != a[1] != a[2]:
            print("Scalene")