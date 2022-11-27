def solution(nums):
    answer = 0
    poArray = []

    # 우선 뽑을 수 있는 최대의 포켓몬 수를 측정
    maxPo = int(len(nums) / 2)

    # 빈 배열을 생성 poArray에 존재하지 않으면 append
    # 이 부분을 nums.set()으로 중복제거 처리 가능!!!!
    for i in nums:
        if i not in poArray:
            poArray.append(i)

    # 최대 갯수 보다 많은 수의 포켓몬을 뽑았다면 최대수를 리턴
    if maxPo < len(poArray):
        answer = maxPo
    else:
        answer = len(poArray)

    return answer


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
