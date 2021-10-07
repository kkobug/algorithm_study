def binary_search(l, r, key):
    flagL = flagR = False
    while l <= r:
        mid = (l+r)//2
        if A[mid] == key:  # 중앙값이면 바로 리턴
            return 1
        elif A[mid] > key:  # 키값보다 중앙값이 크면 r값 당기기
            r = mid-1
            if flagR: break  # 전에도 r 당겼으면 return 0
            flagR = True
            flagL = False  # 누적되지않도록 기록 삭제
        else:              # 7~ 9 와 반대
            l = mid+1
            if flagL: break
            flagL = True
            flagR = False
    return 0

for tc in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    ans = 0
    for k in B:
        if binary_search(0, N-1, k):
            ans += 1
    print(f'#{tc+1} {ans}')
