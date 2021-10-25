"""
https://www.acmicpc.net/problem/17140
"""
def my_sort(arr):
    global max_len
    counting = [[0, i] for i in range(101)]
    for a in arr:
        counting[a][0] += 1
    ans_arr = []
    counting.sort()
    for i, j in counting:
        if i and j:
            ans_arr.append(j)
            ans_arr.append(i)
            if len(ans_arr) >= 100:
                break
    max_len = max(max_len, len(ans_arr))
    return ans_arr


r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

for ans in range(0, 101):
    try:
        if A[r-1][c-1] == k:
            break
    except:
        pass
    # 행의 개수, 열의 개수
    num_row = len(A)
    num_col = len(A[0])
    max_len = 0
    if num_row < num_col:
        A = list(zip(*A))
    for i in range(len(A)):
        A[i] = my_sort(A[i])
    for i in range(len(A)):
        while len(A[i]) < max_len:
            A[i].append(0)
    if num_row < num_col:
        A = list(zip(*A))
else:
    ans = -1

print(ans)