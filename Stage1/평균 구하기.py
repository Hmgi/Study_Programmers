def solution(arr):
    answer = 0

    for i in arr:
        answer = answer + i

    answer = float(answer / len(arr))

    return answer


print(solution([1,2,3,4]))
print(solution([5,5]))