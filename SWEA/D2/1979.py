def where():
    T = int(input())
    for tc in range(1, T+1):
        NK = list(map(int, input().split())) # N은 전체 K는 글자수
        quiz_horizon = []
        base = '0'*(NK[0]+2)
        quiz_horizon.append(base)
        key = '0' + '1' * NK[1] + '0'
        cnt = 0
        for n in range(NK[0]):
            quiz_horizon.append('0'+''.join(input().split())+'0')
        quiz_horizon.append(base)
        horizon = ''.join(quiz_horizon)
        cnt += horizon.count(key)

        quiz_vertical = []
        for n in range(len(quiz_horizon)):
            quiz_vertical.append([])
        for i in range(len(quiz_horizon)):
            for j in range(len(quiz_horizon)):
                quiz_vertical[i].append(quiz_horizon[j][i])
            quiz_vertical[i] = ''.join(quiz_vertical[i])

        vertical = ''.join(quiz_vertical)
        cnt += vertical.count(key)

        print('#{} {}'.format(tc, cnt))


where()