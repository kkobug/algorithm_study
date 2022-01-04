"""
1부터 N까지 자연수 중 중복 없이 M개를 오름차순으로 골라 출력
예제 입력 2
4 2
예제 출력 2
1 2
1 3
1 4
2 3
2 4
3 4
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
nums = list(range(1, 1+N))
ans = []
per()
