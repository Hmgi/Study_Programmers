def solution(arr):
    if len(arr) > 1 :
        arr.pop(arr.index(min(arr)))
        return arr
    else :
        return [-1]

print(solution([4,3,2,1]))
print(solution([10]))