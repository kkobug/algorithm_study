def pascal(num_list):
    # 초기값---------------------------------------
    if num_list == []:
        return [1]
    
    # 파스칼 수열 만들기----------------------------
    new_list = [1]
    for i in range(len(num_list)-1):
        new_list.append(num_list[i]+num_list[i+1])
    new_list.append(1)
    return new_list

def triangle(num):
    # 삼각형으로 출력--------------------------------
    init = []
    for n in range(num, 0, -1):
        print(f"{' '.join(map(str,pascal(init)))}")
        init = pascal(init)

# 입력값---------------------------------------------
T = int(input())
num_case = []
for i in range(T):
    num_case.append(int(input()))

cnt = 0
for j in range(T):
    cnt += 1
    print(f'#{cnt}')
    triangle(num_case[j])
