"""
N개의 자연수 중에서 M개를 고른 수열

예제 입력 2
4 2
9 8 7 1
예제 출력 2
1 7
1 8
1 9
7 1
7 8
7 9
8 1
8 7
8 9
9 1
9 7
9 8
"""
def per(i=0, cnt=0):
    if cnt == M:
        print(*ans)
        return
    for k in range(N):
        if nums[k] in ans:
            continue
        ans.append(nums[k])
        per(i+1, cnt+1)
        ans.pop()

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = []
per()