f = list(map(int, input().split(":")))
s = list(map(int, input().split(":")))
answer = [0, 0, 0]

if f[2] > s[2]:
    s[1] -= 1
    s[2] += 60
answer[2] = s[2] - f[2]

if f[1] > s[1]:
    s[0] -= 1
    s[1] += 60
answer[1] = s[1] - f[1]

if f[0] > s[0]:
    s[0] += 24
answer[0] = s[0] - f[0]

time = answer[0] * 3600 + answer[1] * 60 + answer[2]
print(time)
