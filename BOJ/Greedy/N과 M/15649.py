"""
n, r을 입력받을 때, 1 ~ n의 정수 중 r개를 뽑아 나열하는 경우의 수를 모두 찾아 사전순으로 출력할 것

예제 입력 2
4 2
예제 출력 2
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
"""
def per(cnt=0):
    if cnt == r:
        print(*ans)
        return

    for i in range(n):
        if nums[i] in ans:
            continue
        ans.append(nums[i])
        per(cnt+1)
        ans.pop()


n, r = map(int, input().split())
nums = list(range(1, n+1))
ans = []
per()
