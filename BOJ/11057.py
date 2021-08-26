from sys import stdin as st
"""
문제
오르막 수는 수의 자리가 오름차순을 이루는 수를 말한다. 이때, 인접한 수가 같아도 오름차순으로 친다.

예를 들어, 2234와 3678, 11119는 오르막 수이지만, 2232, 3676, 91111은 오르막 수가 아니다.

수의 길이 N이 주어졌을 때, 오르막 수의 개수를 구하는 프로그램을 작성하시오. 수는 0으로 시작할 수 있다.

입력
첫째 줄에 N (1 ≤ N ≤ 1,000)이 주어진다.

출력
첫째 줄에 길이가 N인 오르막 수의 개수를 10,007로 나눈 나머지를 출력한다.

예제 입력 1
1
예제 출력 1
10
"""

"""
sol1
자리수마다 숫자를 선택가능하고, 중복가능하지만 순서가 정해져있으므로 중복조합의 결과와 같다.
모든 결과를 보여줄 필요는 없고, 계산된 결과만 나타내면 된다.
10개의 숫자 중 n개를 중복선택하는 경우의 수는 10Hn = (9+n)Cn
"""


# def facto(x):
#     for i in range(1, x+1):
#         arr[i] = i * facto(i-1)
#     return arr[x]
#
# N = int(st.readline())
# arr = [1] + [0] * (N+9)
# facto(N+9)
# print(arr[N+9]//(arr[N] * arr[9]) % 10007)


"""
sol2
계산하는건 시간초과가 뜬다.
백트래킹을 이용해 직접 카운트 하자
"""


# def up(i, j):
#     global cnt
#
#     if i == N-1:
#         cnt += 1
#         return
#
#     for k in range(j, 10):
#         if not check[i][j]:
#             check[i][j] = True
#             up(i+1, k)
#             check[i][j] = False
#
#
# N = int(st.readline())
# check = [[False]*10 for _ in range(N)]
# cnt = 0
# up(0, 0)
# print(cnt%10007)


"""
sol3
시간초과 안뜨게 반복문으로 해봄
"""

def iterup(x):
    nums = [1] * 10
    for _ in range(x):
        for i in range(1, 10):
            nums[i] += nums[i-1]
    return nums[9] % 10007


print(iterup(int(st.readline())))
