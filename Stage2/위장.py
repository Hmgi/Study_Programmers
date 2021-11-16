def solution(clothes):
    answer = []
    temp = []
    result = 1
    for i in clothes:
        if i[1] in temp:
            answer[temp.index(i[1])] += 1
        else:
            temp.append(i[1])
            answer.append(1)

    for i in answer:
        result *= i + 1

    return result - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
