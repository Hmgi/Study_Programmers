import itertools

n = int(input())
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
answer = []
for i in range(1, 11):
    for temp in itertools.combinations(num, i):
        temp = list(temp)
        temp.sort(reverse=True)
        answer.append(int("".join(map(str, temp))))
answer.sort()
if n >= len(answer):
    print(-1)
else:
    print(answer[n])

