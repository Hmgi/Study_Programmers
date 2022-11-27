a, b = map(int, input().split())
answer = 0
if a - b < 0:
    temp = b - a
else:
    temp = a - b

print((temp * (temp + 1)) // 2 + (min(a, b) * (temp + 1)))
'''
for i in range(a, b+1, 1):
    answer += i
'''
