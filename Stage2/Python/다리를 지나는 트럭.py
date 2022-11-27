def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 0
    temp_bridge = []
    temp_time = []
    while True:
        # 전체적인 시간 1씩 증가
        time += 1
        for i in range(len(temp_time)):
            temp_time[i] += 1

        if len(temp_time) != 0:
            if temp_time[0] == bridge_length:
                temp_time = temp_time[1:]
                temp_bridge = temp_bridge[1:]

        # 현재 다리위에 있는 트럭
        if len(truck_weights) != 0:
            if sum(temp_bridge) + truck_weights[0] <= weight:
                temp_bridge.append(truck_weights[0])
                temp_time.append(0)
                truck_weights = truck_weights[1:]

        if len(truck_weights) == 0 and len(temp_bridge) == 0:
            break

    return time


print(solution(2, 10, [7, 4, 5, 6]))
