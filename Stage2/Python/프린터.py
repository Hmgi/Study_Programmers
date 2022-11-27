def solution(priorities, location):

    temp = priorities
    temp_index = [i for i in range(len(priorities))]

    stack = []

    for _ in range(len(priorities)):
        max_index = temp.index(max(temp))
        temp = temp[max_index + 1:] + temp[:max_index]
        stack.append(temp_index[max_index])
        temp_index = temp_index[max_index + 1:] + temp_index[:max_index]
        if location in stack:
            return stack.index(location) + 1
    return 0


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))