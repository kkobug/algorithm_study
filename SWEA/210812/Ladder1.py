def buy_icecream():
    for t in range(10):
        tc = int(input())
        arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
        idx_2 = 0
        for find in range(101):
            if arr[99][find] == 2:
                idx_2 = find

        i, j = 99, idx_2
        while i > 0:
            if arr[i][j-1]:
                while arr[i][j-1]:
                    j -= 1
            elif arr[i][j+1]:
                while arr[i][j+1]:
                    j += 1
            i -= 1
        print("#{} {}".format(tc, j-1))


buy_icecream()
