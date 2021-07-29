birth = list(map(int, input().split()))
today = list(map(int, input().split()))
answer = [0, 0, 0]
# 연 나이
answer[2] = today[0] - birth[0]
# 세는 나이
answer[1] = answer[2] + 1

# 만 나이
answer[0] = answer[2] - 1
if birth[1] < today[1]:
    answer[0] += 1
elif birth[1] == today[1]:
    if birth[2] <= today[2]:
        answer[0] += 1

for i in range(3):
    print(answer[i])