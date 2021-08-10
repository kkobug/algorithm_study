def prefix_sum():
    """
    N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
    M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.

    [입력]
    첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
    다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
    다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

    [출력]
    각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
    """
    T = int(input())
    for tc in range(1, T + 1):
        len_sum = list(map(int, input().strip().split()))
        numbers = list(map(int, input().strip().split()))
        sum_min, sum_max = 1000000, 0

        # 초기값 설정, 주어진 조건은 1이상의 정수이므로 필요없음
        # for i in range(len_sum[1]):
        #     sum_min += numbers[i]
        #     sum_max += numbers[i]

        # 2중 for문 sol
        for i in range(0, len_sum[0] - (len_sum[1] - 1)):
            temp = 0
            for j in range(len_sum[1]):  # 슬라이싱으로 for j in numbers[i:i+len_sum[1]]: 해도됨
                temp += numbers[i + j]   # 그러면 여기는 temp += j
            if sum_min > temp:
                sum_min = temp
            if sum_max < temp:
                sum_max = temp

        # 1중 for문으로 풀려면 초기구간합 구해놓고 다음 구간에서
        # 빠지는값 빼고 들어오는값 더하는 식으로 계산
        ### Sliding Window ###
        # for i in range(M, N):
        #     temp = temp + numbers[i] - numbers[i - M]


        print(sum_min, sum_max)
        print("#{} {}".format(tc, sum_max - sum_min))


prefix_sum()
