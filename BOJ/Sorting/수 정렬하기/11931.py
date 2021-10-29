from sys import stdin
N = int(stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(stdin.readline()))

def hoare(st, ed):
    if st >= ed:
        return

    pivot = arr[st]
    L = st + 1
    R = ed
    while L <= R:
        while L <= R and arr[L] > pivot:
            L += 1
        while L <= R and arr[R] <= pivot:
            R -= 1
        if L <= R:
            arr[L], arr[R] = arr[R], arr[L]
    arr[st], arr[R] = arr[R], arr[st]
    hoare(st, R-1)
    hoare(R+1, ed)

hoare(0, N-1)
for i in arr:
    print(i)