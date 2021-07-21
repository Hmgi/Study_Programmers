X, K = map(int, input().split())

answer = 0
# K가 가장 큰수일 때
K1 = K / 2
K2 = K1 / 2
sum = K + K1 + K2
if answer < sum <= X:
    answer = sum

# K가 중간 수일 때
K1 = K / 2
K2 = K * 2
sum = K + K1 + K2
if answer < sum <= X:
    answer = sum

# K가 최소일 때
K1 = K * 2
K2 = K1 * 2
sum = K + K1 + K2
if answer < sum <= X:
    answer = sum

print(int(answer * 1000))
