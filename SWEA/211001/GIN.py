def baby_gin():
    """
    0~9 사이의 숫자카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고,
    3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.
    그리고 6장의 카드가 run과 triplet으로만 구성된 경우를 baby-gin으로 부른다.

    6자리의 숫자를 입력을 받아 baby-gin 여부를 판단하는 프로그램을 작성하라.
    베이비진이 맞다면 1을 아니라면 0을 출력하여라...

    입력
    첫줄에는 테스트케이스 개수가 주어지고, 이후 6장의 카드가 주어진다.

    출력
    #(테케번호) (정답) 형식으로 출력할것.
    """
    T = int(input())

    for tc in range(1, T + 1):
        walk, triplet = 0, 0
        GIN = list(map(int, input().strip()))

        # 최대값 찾기
        max_GIN = GIN[0]
        for m in GIN:
            if m > max_GIN:
                max_GIN = m
        gin_data = [0] * (max_GIN + 3)

        # 카운팅
        for cnt in GIN:
            gin_data[cnt] += 1

        # 검사
        i = 0
        while i <= max_GIN + 1:
            if gin_data[i] >= 1 and gin_data[i + 1] >= 1 and gin_data[i + 2] >= 1:
                walk += 1
                gin_data[i] -= 1
                gin_data[i + 1] -= 1
                gin_data[i + 2] -= 1
                continue
            elif gin_data[i] >= 3:
                triplet += 1
                gin_data[i] -= 3
                continue
            i += 1
        if walk + triplet >= 2:
            print('#{} {}'.format(tc, 1))
        else:
            print('#{} {}'.format(tc, 0))


baby_gin()