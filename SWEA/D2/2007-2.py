def how_long():
    maximum_word_length = 10
    T = int(input())
    word_list = []
    for i in range(T):
        word_list.append(input())

    result = []
    for w in range(len(word_list)):
        for i in range(1, maximum_word_length+1):
            if word_list[w][:i] * (2*maximum_word_length//i) == word_list[w][:(2*maximum_word_length//i)*i]:
                result.append(i)
                break
            else:
                continue
    return result

num = 0
for i in how_long():
    num += 1
    print(f'#{num} {i}')