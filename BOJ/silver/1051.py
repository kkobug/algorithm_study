"""
문제
N*M크기의 직사각형이 있다. 각 칸은 한 자리 숫자가 적혀 있다.
이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오.
이때, 정사각형은 행 또는 열에 평행해야 한다.

입력
첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 수가 주어진다.

출력
첫째 줄에 정답 정사각형의 크기를 출력한다.

예제 입력 1
3 5
42101
22100
22101
예제 출력 1
9
"""
def issquare(N, M):
    i = -1
    cnt = 0
    if N <= M:
        for k in range(N - 1, 0, -1):
            cnt += 1
            for i in range(cnt):
                for j in range(M - k):
                    if nums[i][j] == nums[i + k][j] == nums[i][j + k] == nums[i + k][j + k]:
                        return (k+1)*(k+1)

    else:
        for k in range(M-1, 0, -1):
            cnt += 1
            for i in range(cnt):
                for j in range(N-k):
                    if nums[j][i] == nums[j + k][i] == nums[j][i + k] == nums[j + k][i + k]:
                        return (k+1)*(k+1)

    return 1


N, M = map(int, input().split())
nums = [list(map(int, input())) for _ in range(N)]
print(issquare(N, M))
