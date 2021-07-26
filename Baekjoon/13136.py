R, C, N = map(int, input().split())
countx = 0
county = 0
if R % N != 0:
    countx = R // N + 1
else:
    countx = R // N
if C % N != 0:
    county = C // N + 1
else:
    county = C // N
print(countx * county)