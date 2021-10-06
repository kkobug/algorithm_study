"""
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.
화물이 실려 있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려고 한다.
트럭당 한 개의 컨테이너를 운반 할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.
컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량이 주어지고,
A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행한다고 한다.
이때 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면,
옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램을 만드시오.
화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다.
컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 컨테이너 수 N과 트럭 수 M이 주어지고,
다음 줄에 N개의 화물이 무게wi, 그 다음 줄에 M개 트럭의 적재용량 ti가 주어진다.
1<=N, M<=100, 1<=wi, ti<=50

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력
3
3 2
1 5 3
8 3
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13
출력
#1 8
#2 45
#3 84
"""
def get_idx(X, V):  # 가장 큰 값의 인덱스 찾기
    if sum(V) == len(V):  # 남은 컨테이너/트럭이 없으면 -1
        return -1
    for B in range(len(V)):  # ret = V.index(False) 랑 같음
        if not V[B]:
            ret = B
            break

    for i in range(len(X)):  # 컨테이너/트럭 중 가장 큰 값 찾기
        if not V[i] and X[ret] < X[i]:
            ret = i
    return ret


for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    cont = list(map(int, input().split()))
    cont_V = [False] * N  #
    truck = list(map(int, input().split()))
    truck_V = [False] * M
    ans = 0

    while True:
        c = get_idx(cont, cont_V)
        t = get_idx(truck, truck_V)
        if c == -1 or t == -1:
            break

        cont_V[c] = True  # 컨테이너는 무조건 방문체크
        if cont[c] <= truck[t]:
            truck_V[t] = True  # 트럭은 실을 수 있을 때만 방문체크
            ans += cont[c]  # 실은만큼 더하기

    print(f'#{tc} {ans}')
