def insert(num_list):
    for i in range(1, len(num_list)):
        data = num_list[i]
        j = i
        while j > 0 and num_list[j-1] > data:
            num_list[j] = num_list[j-1]
            j -= 1
        num_list[j] = data
    return num_list # 공간복잡도 N

print(insert([4, 3, 2 , 1, 0]))