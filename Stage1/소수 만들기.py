from itertools import combinations
import math


def checkPrime(n):
    sqrt = math.sqrt(n)
    if sqrt < 2:
        return False

    for i in range(2, int(sqrt+1)):
        if n % i == 0:
            return False
    return True


def solution(nums):
    answer = 0

    result = list(combinations(nums, 3))

    for n1, n2, n3 in result:
        if checkPrime(n1+n2+n3):
            answer += 1

    return answer


print(solution([1, 2, 3, 4]))
