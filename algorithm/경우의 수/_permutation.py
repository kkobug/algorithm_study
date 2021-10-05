"""
배열(집합)의 요소에 대한 순열을 구하는 코드
"""

# 순열: N개 중 r개를 선택하여 나열하는 경우의 수
arr = [1, 2, 3, 4]
N = len(arr)
sel = []
visit = [False] * N

def per_BT(r=N, idx=0):
    if idx == r:
        print(*sel)
        return
    for i in range(N):
        if visit[i]:
            continue
        sel.append(arr[i])
        visit[i] = True
        per_BT(r, idx+1)
        sel.pop()
        visit[i] = False

per_BT()