"""
배열(집합)의 부분집합, 또는 그 합을 구하는 알고리즘 구현
"""


# 부분집합 완전검색(반복문: Yes/No 형태로 출력)
def powerset_loop(arr):
    for i in range(2):
        arr[0] = i
        for j in range(2):
            arr[1] = j
            for k in range(2):
                arr[2] = k
                print(arr)


def powerset_loop_v2(arr):
    subset = [[]]
    for i in arr:
        for j in range(len(subset)):
            subset.append(subset[j] + [i])
    print(subset)


# powerset_loop([0, 0, 0])
# powerset_loop_v2([1, 2, 3])


# 부분집합 완전검색(비트연산자)
def powerset(arr):
    for i in range(1 << len(arr)):
        for j in range(len(arr)):
            if i & (1 << j):
                print(arr[j], end=" ")
        print()


array = [1, 2, 3]
# powerset(array)


# 부분집합 백트래킹
def powerset_BT(k, n):
    if n == k:
        for i in range(k):
            if A[i] == 1:
                print(arr[i], end=" ")
        print()

    else:
        A[k] = 1
        powerset_BT(k+1, n)
        A[k] = 0
        powerset_BT(k+1, n)


arr = [1, 2, 3]
N = len(arr)
A = [0] * N
# powerset_BT(0, N)
