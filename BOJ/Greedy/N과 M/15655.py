"""
N개의 자연수 중에서 M개를 고른 수열
고른 수열은 오름차순이어야 한다.

예제 입력 2
4 2
9 8 7 1
예제 출력 2
1 7
1 8
1 9
7 8
7 9
8 9
"""
def per(i=0, cnt=0):
    if cnt == M:
        print(*ans)
        return
    for k in range(i, N):
        ans.append(nums[k])
        per(k+1, cnt+1)
        ans.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []
per()