def gravity():
    """
    상자들이 쌓여있는 방이 있다. 방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때,
    낙차가 가장 큰 상자를 구하여 그 낙차를 리턴 하는 프로그램을 작성하시오.
    중력은 회전이 완료된 후 적용된다.
    상자들은 모두 한쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며 벽에서 떨어져서 쌓인 상자는 없다.
    방의 가로길이는 항상 100이며, 세로 길이도 항상 100이다.
    즉, 상자는 최소 0, 최대 100 높이로 쌓을 수 있다.
    """
    T = int(input())
    for tc in range(1, T + 1):
        drop = 0
        length = int(input())
        box = list(map(int, input().split()))
        for target in range(length):
            block = 0
            for b in box[target + 1:]:
                if b >= box[target]:
                    block += 1
            temp = len(box[target + 1:]) - block
            if drop < temp:
                drop = temp
        print('#{} {}'.format(tc, drop))


gravity()