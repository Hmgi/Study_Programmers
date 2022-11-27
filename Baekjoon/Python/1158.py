n, k = map(int, input().split())
people_list = [i for i in range(1, n + 1)]

answer = []
people = 0

for i in range(n):
    people += k - 1
    if people >= len(people_list):
        people = people % len(people_list)
    answer.append(str(people_list.pop(people)))

print("<", ", ".join(answer)[:], ">", sep='')
