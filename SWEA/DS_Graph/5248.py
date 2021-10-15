"""
그룹 나누기
수업에서 같은 조에 참여하고 싶은 사람끼리 두 사람의 출석 번호를 종이에 적어 제출하였다.
한 조의 인원에 제한을 두지 않았기 때문에,
한 사람이 여러 장의 종이를 제출하거나 여러 사람이 한 사람을 지목한 경우 모두 같은 조가 된다.
예를 들어 1번-2번, 1번-3번이 같은 조가 되고 싶다고 하면, 1-2-3번이 같은 조가 된다.
번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성하게 된다.
1번부터 N번까지의 출석번호가 있고, M 장의 신청서가 제출되었을 몇 개의 조가 만들어지는가?

[입력]
첫 줄에 테스트 케이스의 개수가 주어지고,
다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M,
다음 줄에 M 쌍의 번호가 주어진다. 2<=N<=100, 1<=M<=100
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4
출력
#1 3
#2 2
#3 3
"""


# Disjoint-sets
def find_set(x):  # find_set with path compression
    if team[x] != x:
        team[x] = find_set(team[x])
    return team[x]


for tc in range(int(input())):
    N, M = map(int, input().split())
    want = list(map(int, input().split()))
    team = list(range(N+1))  # make_set
    for i in range(M):
        team[find_set(want[2*i+1])] = find_set(want[2*i])  # union
    ans = -1  # except 0 team
    cnt = [False]*(N+1)
    for i in set(team):  # team check
        k = find_set(i)
        if not cnt[k]:
            cnt[k] = True
            ans += 1
    print(f'#{tc+1} {ans}')




"""
# DFS solution
def dfs(x):
    global ans
    V[x] = True
    S = [x]
    while S:
        k = S.pop()
        for j in team[k]:
            if not V[j]:
                S.append(j)
                V[j] = True
    ans += 1
    return


for tc in range(int(input())):
    N, M = map(int, input().split())
    want = list(map(int, input().split()))
    team = [[] for _ in range(N+1)]
    for i in range(M):
        team[want[2*i]].append(want[2*i+1])  # 지목 하거나, 지목 당하는 결과가 같으므로 모두 추가
        team[want[2*i+1]].append(want[2*i])
    ans = 0
    V = [False]*(N+1)  # 조를 짰는지 확인
    for i in range(1, 1+N):
        if not V[i]:
            dfs(i)
    print(f'#{tc+1} {ans}')
"""