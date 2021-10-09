def get_num(X):
    for i in range(len(T)):
        for j in range(2):
            T[i] = str((int(T[i])+1)%3)
            int_T = int(''.join(T), 3)
            if X == int_T:
                return True
        T[i] = str((int(T[i]) + 1) % 3)


for tc in range(int(input())):
    B = list(input())
    T = list(input())

    for i in range(len(B)):
        B[i] = str(1-int(B[i]))
        int_B = int(''.join(B), 2)
        if get_num(int_B):
            break
        B[i] = str(1-int(B[i]))
    print(f'#{tc+1} {int_B}')
