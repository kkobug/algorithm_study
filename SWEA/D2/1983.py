grade_list = [
    'A+', 'A0', 'A-',
    'B+', 'B0', 'B-',
    'C+', 'C0', 'C-', 'D0'
]

T = int(input())
for t in range(T):
    idx = list(map(int, input().split()))
    score = []
    for i in range(idx[0]):
        stu = list(map(int, input().split(' ')))
        avg = int(stu[0] * 0.35 + stu[1] * 0.45 + stu[2] * 0.20)
        score.append(avg)
    target_score = score[idx[1] - 1]
    counts = [0] * 101
    for i in range(len(score)):
        counts[score[i]] += 1

    cnt = 0
    j = 100
    while j > target_score:
        if counts[j] != 0:
            cnt += 1
            counts[j] -= 1
            continue
        j -= 1

    # cnt = 0
    # for j in range(100, -1, -1):
    #     if j == target_score:
    #         ranking = cnt
    #     elif counts[j] != 0:
    #         cnt += 1
    print(grade_list[cnt // (len(score) // 10)])
