def what_is_mid():
    N = int(input())
    num_list = list(map(int, input().split()))
    for i in range(len(num_list)):
        for j in range(len(num_list)-1):
            if num_list[j] >= num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list[N//2]

print(what_is_mid())