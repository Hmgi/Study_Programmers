import heapq
def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while len(scoville) >= 2: # 리스트 길이는 최소 2개여야 한다.
        if scoville[0] >= K:
            return answer
        answer += 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + (b * 2))
    if scoville[0] < K: # 계산이 완료 되었을 때 나머지 1개가 K보다 작으면 -1 출력
        return -1

    return answer