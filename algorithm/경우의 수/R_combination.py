"""
배열(집합)의 요소에 대한 중복조합을 구하는 코드
"""

# 중복조합: N개 중 r개를 중복을 허용하여 선택하는 경우의 수
arr = [1, 2, 3, 4]
N = len(arr)
sel = []

def com_BT(r=N, idx=0):
    if len(sel) == r:
        print(*sel)
        return
    for i in range(idx, N):
        sel.append(arr[i])
        com_BT(r, i)
        sel.pop()

com_BT(2)