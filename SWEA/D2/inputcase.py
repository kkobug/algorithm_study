def input_num_return_list():
    T = int(input())
    num_list = []
    for t in range(T):
        num_list.append(int(input()))
    return num_list

def input_list_return_list():
    T = int(input())
    num_list = []
    for t in range(T):
        num_list.append(list(map(int, input().strip().split(' '))))
    return num_list

def output(result):
    cnt = 0
    for i in result:
        cnt += 1
        print(f'#{cnt} {i}')
