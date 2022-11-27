people, max_people = 0, 0
for _ in range(4):
    out_people, in_people = map(int, input().split())
    people += in_people - out_people
    if max_people < people:
        max_people = people
print(max_people)