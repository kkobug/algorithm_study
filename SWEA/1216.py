def hoi2():
    """
    "기러기" 또는 "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
    주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.

    [제약사항]
    각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.
    글자 판은 무조건 정사각형으로 주어진다.
    ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.
    가로, 세로 각각에 대해서 직선으로만 판단한다. 즉, 아래 예에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다.

    [입력]
    각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
    총 10개의 테스트케이스가 주어진다.
    [출력]
    #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 길이를 출력한다.
    """
    for t in range(10):
        tc = int(input())
        words = [list(input()) for _ in range(100)]
        cnt = 1
        for trans in range(2):
            for i in range(99):
                for j in range(99):
                    for w in range(100 - j, cnt, -1):
                        if words[i][j:j + w] == words[i][j + w - 1:j - 1:-1]:
                            if w > cnt:
                                cnt = w
                                break

            for x in range(100):
                for y in range(100):
                    if x > y:
                        words[x][y], words[y][x] = words[y][x], words[x][y]

        print("#{} {}".format(tc, cnt))


hoi2()