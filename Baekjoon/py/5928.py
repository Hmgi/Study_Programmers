D, H, M = map(int, input().split())
d, h, m = 11, 11, 11

# 분
if M - m < 0:
    H -= 1
    M += 60
useM = M - m

# 시
if H - h < 0:
    D -= 1
    H += 24
useH = H - h

# 일
useD = D - d
useM = useM + useH * 60 + useD * 24 * 60
if useM < 0:
    print(-1)
else:
    print(useM)
