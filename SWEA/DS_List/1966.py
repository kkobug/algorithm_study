def bubble_sort():
    T = int(input())
    for tc in range(1, T + 1):
        length = int(input())
        numbers = list(map(int, input().split()))
        for i in range(length - 1, 0, -1):
            for j in range(i):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        result = ' '.join(list(map(str, numbers)))
        print('#{} {}'.format(tc, result))

bubble_sort()