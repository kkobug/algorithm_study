def get_num():
    st = 1
    ed = X
    mid = (st + ed) // 2
    if 99 <= Z:
        return -1
    else:
        while st < ed:
            mid = (st + ed)//2
            if Z < int(100 * (Y+mid)/(X+mid)):
                st = mid + 1
            else:
                ed = mid

    return mid




X, Y = map(int, input().split())
Z = int(100 * (Y/X))
print(get_num())
