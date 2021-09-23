"""
NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다.
단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 숫자 N이 주어지고, 이후 N개씩 N줄에 걸쳐 10보다 작은 자연수가 주어진다. 3≤N≤10

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 합계를 출력한다.

입력
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8

출력
#1 8
#2 14
#3 9
"""


def get_case(i=0, temp=0):
    global ans

    if temp > ans: return  # 이미 최소값이 아니라면 가지치기 (안하면 시간초과)

    if i == N:
        if ans > temp:
            ans = temp
        return

    for j in range(N):
        if not check[j]:  # 체크 안한거라면
            check[j] = True
            get_case(i+1, temp+nums[i][j])  # 더하면서 체크
            check[j] = False


for tc in range(1, 1+int(input())):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    ans = 10 * N  # 10보다 작은 자연수만 주어지므로 답은 10*N보다 커질 수 없음
    check = [False] * N  # 가능성 체크
    get_case()
    print("#{} {}".format(tc, ans))
