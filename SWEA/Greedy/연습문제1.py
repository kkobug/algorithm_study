# 선택정렬 함수를 재귀적으로 만들어보기

def sel_sort(idx=0):
    if idx == N:
        return

    min_val = arr[idx]
    j = idx
    for i in range(idx, N):
        if min_val > arr[i]:
            min_val = arr[i]
            j = i
    arr[idx], arr[j] = arr[j], arr[idx]
    sel_sort(idx+1)

N = 5
arr = [4, 3, 5, 1, 2]
sel_sort()
print(arr)