"""
문제
3차원 공간에 점 N개가 있다. 가장 가까운 점의 거리를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 수 N이 주어진다. N은 150,000보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 각 점의 좌표가 주어진다. 좌표의 절댓값은 1000000보다 작거나 같은 정수이다. 중복되는 점은 한 개로 가정하고, 적어도 2개의 서로 다른 점이 있다.

출력
첫째 줄에 가장 가까운 점의 거리의 제곱을 출력한다. 둘째 줄에는 그러한 거리를 가지는 서로 다른 점의 쌍이 총 몇 개 있는지 개수를 출력한다.
"""

N = int(input())
dots = [list(map(int, input().split())) for _ in range(N)]
d = (dots[0][0]-dots[1][0])**2 + (dots[0][1]-dots[1][1])**2 + (dots[0][2]-dots[1][2])**2
cnt = 0
for i in range(N-1):
    for j in range(i+1, N):
        nd = (dots[i][0]-dots[j][0])**2 + (dots[i][1]-dots[j][1])**2 + (dots[i][2]-dots[j][2])**2
        if d > nd:
            cnt = 0
            d = nd
        elif d == nd:
            cnt += 1
print(d)
print(cnt)