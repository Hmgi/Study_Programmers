def solution(participant, completion):
    # 동명이인이 있을 수 있기 때문에 배열을 정리 해준다.
    participant.sort()
    completion.sort()

    # 미완주자는 1명이기 때문에 return 배열 1개만 하면 된다.
    # 완주자 배열의 길이만큼 반복을 진행하며
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]
    # 반복문이 끝난다면 참가자의 맨 뒤 배열의 참가자가 미완주자이다.
    return participant[i + 1]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
