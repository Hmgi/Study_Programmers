def solution(n):
    answer = 0
    number3 = []
    while n != 0:
        number3.append(int(n % 3))
        n = int(n / 3)
    z = len(number3) - 1
    for i in range(len(number3)):
        answer = answer + number3[i] * (3 ** z)
        z = z - 1
    return answer


print(solution(45))
print(solution(125))
