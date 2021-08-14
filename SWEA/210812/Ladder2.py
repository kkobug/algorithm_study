# def fast():
#     for t in range(10):
#         tc = int(input())
#         ladder = [list(map(int, input().strip().split())) for _ in range(100)]
#         starting = [s for s in range(100) if ladder[0][s] == 1]
#         minimum = 10000
#         for pos in range(len(starting)):
#             cnt = 0
#             i = 0
#             j = pos
#             while i < 100:
#                 # if 0 <= j - 1 and ladder[i][starting[j] - 1] == 1:
#                 if j != 0 and ladder[i][starting[j] - 1] == 1:
#                     j -= 1
#                     cnt += 1
#                 # elif j + 1 <= len(starting)-1 and ladder[i][starting[j] + 1] == 1:
#                 elif j != len(starting) - 1 and ladder[i][starting[j] + 1] == 1:
#                     j += 1
#                     cnt += 1
#                 i += 1
#             if cnt < minimum:
#                 minimum = cnt
#
#         print(tc, cnt)
#
#
# fast()


for a in range(10):
    T = int(input())
    test_list = list(list(map(int, input().split())) for _ in range(100))

    radder = []

    mini = 10000
    for li in range(len(test_list[0])):  # 사다리 막대를 구함
        if test_list[0][li] == 1:
            radder += [li]

    for sada in range(len(radder)):  # 첫번째 사다리 막대일때
        cur_p = sada
        cnt = 0
        for start_p in range(100):  # 바닥까지이동할때
            if cur_p != 0 and test_list[start_p][radder[cur_p] - 1] == 1:
                cur_p -= 1  # 옆 막대로 이동
                cnt += 1

            elif cur_p != len(radder) - 1 and test_list[start_p][radder[cur_p] + 1] == 1:
                cur_p += 1
                cnt += 1

        if mini > cnt:
            mini = cnt

    print("#{} {}".format(T, cnt))