"""
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
예제 입력 2
4 2
예제 출력 2
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4
"""
def per(cnt=0):
    if cnt == M:
        print(*ans)
        return

    for k in range(N):
        ans.append(nums[k])
        per(cnt+1)
        ans.pop()


N, M = map(int, input().split())
nums = list(range(1, 1+N))
ans = []
per()
