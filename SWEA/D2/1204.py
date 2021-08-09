def most_num():
    T = int(input())
    num_test = []
    num_list = []
    for i in range(T):
        num_test.append(int(input()))
        num_list.append(list(map(int, input().split(' '))))
    
    result = []
    for n in num_list:
        temp = [0, ]*100
        for j in n:
            temp[j-1] += 1
        result.append(temp.index(max(temp[::-1]))+1)
    
    for c in range(len(result)):
        print(f'#{num_test[c]} {result[c]}')

most_num()