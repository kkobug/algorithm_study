def our_max(a, b):
    if a > b: return a
    return b


def max_sum():
    for tc in range(1, 11):
        T = int(input())
        arr = [list(map(int, input().split())) for a in range(100)]
        ans = arr[0][0]
        row, col, dia, r_dia = 0, 0, 0, 0
        for i in range(100):
            for j in range(100):
                row += arr[i][j]
                col += arr[j][i]
                if i == j:
                    dia += arr[i][j]
                if i + j == 99:
                    r_dia += arr[i][j]
            if our_max(row, col) > ans:
                ans = our_max(row, col)
            row, col = 0, 0
        if our_max(dia, r_dia) > ans:
            ans = our_max(dia, r_dia)

        print("#{} {}".format(T, ans))


max_sum()
