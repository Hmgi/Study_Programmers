l = int(input())
temp = list(map(int, input().split()))
n = int(input())

if n in temp:
    print(0)
else:
    answer = [n]
    for i in range(n-1, 0, -1):
        if i in temp:
            break
        else:
            answer.append(i)

    for j in range(n+1, 1000, 1):
        if j in temp:
            break
        else:
            answer.append(j)

    answer.sort()
    print(answer)

    '''for kdx, k in enumerate(answer):
        if k > n:
            break
        else:
            count += len(answer) - (answer.index(n) + 1)
        print(count)
    '''
    print((answer.index(n) + 1) * (len(answer) - answer.index(n)) - 1)