def selection(num_list):
    for i in range(len(num_list)-1):
        temp = i
        for j in range(i+1, len(num_list)):
            if num_list[temp] > num_list[j]:
                temp = j
        num_list[i], num_list[temp] = num_list[temp], num_list[i]

    return num_list # 공간복잡도 N

print(selection([4, 3, 2, 1, 0]))