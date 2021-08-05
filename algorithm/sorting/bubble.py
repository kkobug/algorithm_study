def bubble(num_list):
    for i in range(len(num_list)-1):
        for j in range(len(num_list)-1):
            if num_list[j] > num_list[j+1]:
                num_list[j] ,num_list[j+1] = num_list[j+1] ,num_list[j]
    
    return num_list # 공간복잡도 N

print(bubble([4, 3, 2, 1, 0]))