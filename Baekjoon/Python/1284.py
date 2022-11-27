while True:
    n = input()
    if n == "0":
        break
    else:
        count = 0
        for i in n:
            if i == "1":
                count += 2
            elif i == "0":
                count += 4
            else:
                count += 3
        count += len(n) + 1
        print(count)
