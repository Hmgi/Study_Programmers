N = int(input())
N_Weight = list(map(int, input().split()))

Box = int(input())
Box_Weight = list(map(int, input().split()))

count = 0
N_Weight.sort(reverse=True)
Box_Weight.sort(reverse=True)

if N_Weight[0] < Box_Weight[0]:
    print(-1)
else:
    while len(Box_Weight) > 0:
        for i in N_Weight:
            for j in range(len(Box_Weight)):
                if i >= Box_Weight[j]:
                    Box_Weight.remove(Box_Weight[j])
                    break
        count += 1
    print(count)