n = int(input())
max_money = 0
for _ in range(n):
    people = list(map(int, input().split()))
    temp = 0
    people.sort()
    if people[0] == people[1] == people[2]:
        temp = 10000 + people[0] * 1000
    elif people[0] == people[1]:
        temp = 1000 + people[0] * 100
    elif people[1] == people[2]:
        temp = 1000 + people[1] * 100
    else:
        temp = max(people) * 100

    if max_money < temp:
        max_money = temp
print(max_money)