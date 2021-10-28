a, b = map(int, input().split())
c, d = map(int, input().split())

answer = []

case1 = a / c + b / d
case2 = c / d + a / b
case3 = d / b + c / a
case4 = b / a + d / c

answer.append(case1)
answer.append(case2)
answer.append(case3)
answer.append(case4)

print(answer.index(max(answer)))