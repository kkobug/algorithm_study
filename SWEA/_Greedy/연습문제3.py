# 10개 정수 집합에 대한 모든 부분집합 중 원소의 합이 0이 되는 부분집합을 모두 출력
"""
예시 입력
-1 3 -9 6 7 -6 1 5 4 -2
"""

def check(k=0, r=1):
    global ans
    if r == N:
        return

    if k == r:
        if sum(ans) == 0:
            print(*ans)
        return
    else:
        if not visit[k]:
            visit[k] = True
            ans.append(arr[k])
            check(k+1, r)
            ans.pop()
            visit[k] = False
            check(k+1, r)
            # ans = []
            check(0, r+1)
            return



N = 10
arr = list(map(int, input().split()))
visit = [False] * 10
ans = []
check()