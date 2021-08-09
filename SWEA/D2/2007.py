def how_long():
    T = int(input())
    word_list = []
    for i in range(T):
        word_list.append(input())

    result = []
    for w in range(len(word_list)):
        cnt = 0
        # 10부터 내려오면서 반복되는 구간 찾기
        for j in range(10,0,-1):
            if word_list[w][0:j] == word_list[w][j:2*j]:
                cnt = j
                result.append(cnt)
                break

        # 1부터 올라가며 반복구간 있는지 찾기
        for i in range(1, 6):
            if word_list[w][:i] * (10//i) == word_list[w][:cnt]:
                result[w] = i
                break
            else:
                continue
    return result
        # 더생각해보기: 첫번째 vs 2번째 vs 마지막

num = 0
for i in how_long():
    num += 1
    print(f'#{num} {i}')
