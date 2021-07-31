def calculator(a, b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)

x = list(map(int, input().split(' ')))
calculator(x[0], x[1])