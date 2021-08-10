n = int(input())
data = list(map(int, input().split()))

m = int(input())
weight = list(map(int, input().split()))

count = 0
data = sorted(data, reverse=True)
weight = sorted(weight, reverse=True)

if data[0] < weight[0]:
    print(-1)
else:
    while len(weight) > 0:
        for l in data:
            for j in range(len(weight)):
                if l >= weight[j]:
                    weight.remove(weight[j])
                    break
        count += 1
    print(count)