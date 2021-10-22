"""
* 대각선 방향으로 탐색하며
1. 중복이 있을 경우 가지치기
2. 범위를 벗어나면 가지치기
3. 대각선이 마름모를 이루지 않으면(즉, 1 <= d1 and 1 <= d2) 가지치기
유사문제 : 게리맨더링

[제약사항]
1. 시간제한 : 최대 50개 테스트 케이스를 모두 통과하는 데 C/C++/Java 모두 3초
2. 디저트 카페가 모여있는 지역의 한 변의 길이 N은 4 이상 20 이하의 정수이다. (4 ≤ N ≤ 20)
3. 디저트 종류를 나타나는 수는 1 이상 100 이하의 정수이다.

[입력]
입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고, 그 다음 줄부터 T개의 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 디저트 카페가 모여있는 지역의 한 변의 길이 N이 주어진다.
그 다음 N 줄에는 N * N 크기의 디저트 카페에서 팔고 있는 디저트 종류에 대한 정보가 주어진다.

[출력]
테스트 케이스 개수만큼 T개의 줄에 각각의 테스트 케이스에 대한 답을 출력한다.
각 줄은 "#t"로 시작하고 공백을 하나 둔 다음 정답을 출력한다. (t는 1부터 시작하는 테스트 케이스의 번호이다)
출력해야 할 정답은 가능한 경우 중 디저트를 가장 많이 먹을 때의 디저트 수 이다.
만약, 디저트를 먹을 수 없는 경우 정답은 -1이다.

입력
2
4
9 8 9 8
4 6 9 4
8 7 7 8
4 5 3 5
5
8 2 9 6 6
1 9 3 3 4
8 2 3 3 6
4 3 4 4 9
7 4 6 3 5
출력
#1 6
#2 -1
"""
def tour(i, j, d1, d2, C):
    r, c = i, j
    try:  # 인덱스를 벗어나면 무조건 -1 반환시키기 위해 try-except 처리
        for d in range(1, 1+d1):  # 왼쪽 아래로 내려가기
            r += 1
            c -= 1
            if cafe[r][c] in C:  # 같은 카페 있으면 이번 투어는 실패했으므로 -1 반환
                return -1
            C.append(cafe[r][c])
        for d in range(1, 1+d2):  # 오른쪽 아래로 내려가기
            r += 1
            c += 1
            if cafe[r][c] in C:
                return -1
            C.append(cafe[r][c])
        for d in range(1, 1+d1):  # 오른쪽 위로 올라가기
            r -= 1
            c += 1
            if cafe[r][c] in C:
                return -1
            C.append(cafe[r][c])
        for d in range(1, 1+d2):  # 왼쪽 위로 올라가기
            r -= 1
            c -= 1
            if (r, c) == (i, j):  # 출발지로 성공적으로 돌아왔으면 투어한 만큼 반환
                return len(C)
            if cafe[r][c] in C:
                return -1
            C.append(cafe[r][c])
    except:
        return -1
    return len(C)


for tc in range(int(input())):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    ans = -1  # 카페를 못가면 -1로 출력하라 했으므로 -1로 선언
    for r in range(N-2):
        for c in range(1, N-1):
            for _d1 in range(1, 1+c):  # 왼쪽으로 갈 때의 대각선 거리 (가능한 최대 거리는 현재 열만큼)
                for _d2 in range(1, N-c):  # 오른쪽으로 갈 때의 대각선 거리 (가능한 최대 거리는 최대열 - 현재열)
                    temp = tour(r, c, _d1, _d2, [cafe[r][c]])
                    ans = max(ans, temp)
    print(f'#{tc+1} {ans}')
