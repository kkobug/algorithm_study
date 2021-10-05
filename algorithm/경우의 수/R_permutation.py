"""
배열(집합)의 요소에 대한 중복순열을 구하는 코드
"""

# 중복순열: N개 중 r개를 중복을 허용하며 선택하여 나열하는 경우의 수
arr = [1, 2, 3, 4]
N = len(arr)
sel = []

def per_BT(r=N, idx=0):
    if idx == r:
        print(*sel)
        return
    for i in range(N):
        sel.append(arr[i])
        per_BT(r, idx+1)
        sel.pop()

per_BT(2)