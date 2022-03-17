from collections import deque


def solution(bridge_length, weight, truck_weights):
    # 1. weight >= truck_weights 요소 합
    # 2. 먼저 들어간 트럭이 brige_length 만큼 시간이 지나야 popleft
    # 예시에 1대면 101초 10대면 110초?
    # -> 도착할때 시간 고려 예시 트럭무게가 7 한개라면 3초겠지..?
    # -> 대기 시간 고려
    # 3. sum 사용
    # 4. 선입선출 deque 사용(길이가 10000)
    truck_weights = deque(truck_weights)
    # 다리 위의 트럭들
    onBridge = deque()
    answer = 0  # 시간, 시작과 동시에 if문으로 대기 시간이 없으면 +1
    if sum(truck_weights) <= weight:
        answer += len(truck_weights)
    while True:
        while len(truck_weights):
            # 만약에 다리 위의 트럭 무게의 합이 견딜 수 있는 무게(weight) 보다 작다면
            if sum(onBridge) + truck_weights[0] <= weight:
                # 첫번째 트럭 더하고
                onBridge.append(truck_weights[0])
                truck_weights.popleft()
            else:
                break
            # onBridge에서 bridge_length만큼 시간이 지나면 popleft
        onBridge.popleft()
        answer += bridge_length
        if len(truck_weights) == 0:
            break

    return answer


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

print(solution(bridge_length, weight, truck_weights))
