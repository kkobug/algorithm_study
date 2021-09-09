"""
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

예제 입력 2
4 2
예제 출력 2
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4
"""
def per(i=0, cnt=0):
    if cnt == M:
        print(*ans)
        return

    for k in range(i, N):
        ans.append(nums[k])
        per(k, cnt+1)
        ans.pop()

N, M = map(int, input().split())
nums = list(range(1, 1+N))
ans = []
per()