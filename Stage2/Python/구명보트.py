"""def solution(people, limit):
    answer = 0
    stack = []

    people.sort(reverse=True)
    for i in people:
        # 스택이 비어있을 때
        if len(stack) == 0:
            stack.append(i)

        # 스택에 한명이라도 있을 때
        else:
            # 스택의 값과 뽑은 수의 합이 limit을 넘을 때
            if stack.pop() + i > limit:
                answer += 1
                stack.append(i)

            # limit을 넘지 않을 때
            else:
                answer += 1

    if len(stack) != 0:
        answer += 1

    return answer
"""

"""
def solution(people, limit):
    answer = 0
    people.sort()
    while len(people) != 0:
        temp = people.pop()
        for i in people:
            if temp + i > limit:
                answer += 1
                break
            else:
                answer += 1
                people.remove(i)
                break
        else:
            answer += 1

    return answer
"""


"""def solution(people, limit):
    answer = 0
    people.sort()
    while len(people) != 0:
        temp = people.pop()
        if len(people) != 0:
            if temp + people[0] > limit:
                answer += 1
            else:
                answer += 1
                people.pop(0)
        else:
            answer += 1
    return answer
"""

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    left, right = 0, len(people) - 1
    print(people)
    while left <= right:
        if people[left] + people[right] <= limit:
            right -= 1
        left += 1
        answer += 1
    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
# print(solution([40, 50, 150, 160], 200))  # 2
# print(solution([100, 500, 500, 900, 950], 1000))  # 3
