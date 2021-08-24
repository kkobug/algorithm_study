"""
배열(집합)의 요소에 대한 순열을 구하는 코드
"""


arr = [1, 2, 3]
N = len(arr)
sel = [0] * N
check = [0] * N
# 순열: 비트연산 다시
def permutation(idx, check):
    # if check == (1 << N) -1:
    if idx == N:
        print(sel)
        return

    for j in range(N):
        if check & (1 << j): continue
        sel[idx] == arr[j]
        permutation(idx + 1, check | (1 << j))


# permutation(0, 0)


# 순열: 백트래킹(재귀)
def perm_BT(idx):
    if idx == N:
        print(sel)
        return
    for i in range(N):
        if check[i] == 0:
            sel[idx] = arr[i]
            check[i] = 1
            perm_BT(idx+1)
            check[i] = 0


# perm_BT(0)


# 순열: 스왑(nPr)
def perm_swap(arr, N, r, idx=0):
    if idx == r:
        print(arr[0:r])
    else:
        for j in range(idx, N):
            arr[idx], arr[j] = arr[j], arr[idx]
            perm_swap(arr, N, 2, idx+1)
            arr[idx], arr[j] = arr[j], arr[idx]

# perm_swap(arr, N, 2)