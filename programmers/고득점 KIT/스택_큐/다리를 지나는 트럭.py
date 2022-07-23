"""
https://programmers.co.kr/learn/courses/30/lessons/42583
"""
from collections import deque as Q

def solution(bridge_length, weight, truck_weights):
    answer = 0
    waiting_trucks = Q(truck_weights)      # 대기중인 트럭
    running_trucks = Q([0]*bridge_length)  # 다리 위의 트럭
    bridge_weight = 0
    
    while waiting_trucks:
        bridge_weight -= running_trucks.popleft()
        
        if waiting_trucks[0] + bridge_weight <= weight:
            temp = waiting_trucks.popleft()
            bridge_weight += temp
        else:
            temp = 0
        running_trucks.append(temp)
        answer += 1
    answer += bridge_length
    return answer

bridge_length_list = [2, 100, 100]
weight_list = [10, 100, 100]
truck_weights_list = [[7,4,5,6], 
                      [10], 
                      [10,10,10,10,10,10,10,10,10,10]]
for i in range(3):
    print(solution(bridge_length_list[i],
             weight_list[i],
             truck_weights_list[i]))
