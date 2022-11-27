N = int(input())
Y, M = 0, 0
t = list(map(int, input().split()))
for i in t:
    Y += ((i // 30) + 1) * 10
    M += ((i // 60) + 1) * 15
if Y > M:
    print("M", M)
elif Y < M:
    print("Y", Y)
else:
    print("Y M", Y)