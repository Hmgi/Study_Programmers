def solution(numbers, target):
    temp_number = [0]
    for i in numbers:
        temp = []
        for j in temp_number:
            temp.append(j + i)
            temp.append(j - i)
        temp_number = temp
    return temp_number.count(target)


print(solution([1, 1, 1, 1, 1], 3))
