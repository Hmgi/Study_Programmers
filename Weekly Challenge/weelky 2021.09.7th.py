def solution(enter, leave):
    meet = [[] for _ in range(len(enter))]
    room = []
    enter_index, leave_index = 0, 0
    while enter_index < len(enter) or leave_index < len(leave):
        if leave[leave_index] in room:
            room.remove(leave[leave_index])
            meet[leave[leave_index] - 1] = room[:]
            leave_index += 1
        else:
            room.append(enter[enter_index])
            enter_index += 1
    for idx, i in enumerate(meet):
        for met in i:
            meet[met - 1].append(idx + 1)

    return [len(set(i)) for i in meet]


print(solution([1, 3, 2], [1, 2, 3]))
print(solution([1, 4, 2, 3], [2, 1, 3, 4]))