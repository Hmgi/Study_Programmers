def solution(n):
    # 2 ~ n 까지의 수를 변수 a에 담는다.
    a = set(range(2, n+1))
    
    # 2 ~ n 까지의 수 i에 대해 
    for i in range(2, n+1):
        # i 가 num 안에 있으면
        if i in a:
            # i 의 배수 set(i의 2배수 부터 n까지 수 중 i 만큼 간격있는 수들)를 num 에서 빼주기
            a -= set(range(2*i, n+1, i))
    # 나머지 a의 길이 리턴
    return len(a)


print(solution(10))
print(solution(5))
