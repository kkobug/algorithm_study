def each_sum():
    N = int(input())
    result = 0
    while N > 0:
        result += N % 10
        N = N // 10
    return result

print(each_sum())