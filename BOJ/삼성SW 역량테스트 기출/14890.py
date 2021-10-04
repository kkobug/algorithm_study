"""
https://www.acmicpc.net/problem/14890
예제 입력
6 2
3 3 3 3 3 3
2 3 3 3 3 3
2 2 2 3 2 3
1 1 1 2 2 2
1 1 1 3 3 1
1 1 2 3 3 2
예제 출력
3
"""
def check(X):
    f = 0
    p = 1
    st = X[0]
    while p < N:
        if st == X[p]:  # 검사하는 칸이 앞칸과 같은 높이일 경우 기준 칸을 최신화 하고, 지나가기
            p += 1
        elif st + 1 == X[p]:  # 검사하는 칸이 기준칸보다 한칸 높을 경우
            if L <= p-f:  # 기준 칸으로부터 L이상 떨어져있으면 기준 칸을 최신화하고 통과
                f = p
                st = X[p]
                p += 1
                continue
            else:         # 기준 칸으로부터 L만큼의 여유가 없다면 실패
                return False
        elif st - 1 == X[p]:  # 검사하는 칸이 기준칸보다 한칸 낮을 경우
            k = 0
            st = X[p]
            while k < L:  # 앞으로 L칸동안 경사로를 깔기
                try:
                    if st == X[p+k]:
                        k += 1
                    else:
                        return False
                except:  # 인덱스 에러의 경우 False
                    return False
            if p+k == N:  # 다음칸이 마지막이면 검사끝
                return True
            if X[p+k] == st or X[p+k] == st-1:  # 다음칸이 마지막이 아니면, 1칸 이내일때만 통과
                f = p+k
                p = p+k
            else:
                return False
        else:  # 기준칸과의 높이차가 1이내가 아닐 경우엔 False
            return False
    return True  # 무사히 길을 통과하면 True

N, L = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    A, B = [], []
    for j in range(N):
        A.append(road[i][j])
        B.append(road[j][i])
    if check(A):
        ans += 1
    if check(B):
        ans += 1
print(ans)

