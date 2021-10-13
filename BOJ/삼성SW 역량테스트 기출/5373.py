"""
https://www.acmicpc.net/problem/5373
단순 구현
각 면끼리 회전하는 것과
한 면 내에서 회전하는 것을 구현하여 해결
"""
def spin_L(X):
    temp = X[0][0]
    X[0][0] = X[0][2]
    X[0][2] = X[2][2]
    X[2][2] = X[2][0]
    X[2][0] = temp

    temp = X[0][1]
    X[0][1] = X[1][2]
    X[1][2] = X[2][1]
    X[2][1] = X[1][0]
    X[1][0] = temp

def spin_R(X):
    temp = X[0][0]
    X[0][0] = X[2][0]
    X[2][0] = X[2][2]
    X[2][2] = X[0][2]
    X[0][2] = temp

    temp = X[0][1]
    X[0][1] = X[1][0]
    X[1][0] = X[2][1]
    X[2][1] = X[1][2]
    X[1][2] = temp

for _ in range(int(input())):
    _U = [['w']*3 for _ in range(3)]
    _D = [['y']*3 for _ in range(3)]
    _F = [['r']*3 for _ in range(3)]
    _B = [['o']*3 for _ in range(3)]
    _L = [['g']*3 for _ in range(3)]
    _R = [['b']*3 for _ in range(3)]
    N = int(input())
    command = list(input().split())

    for C in command:
        if C[0] == 'U':
            temp = _F[0][:]
            if C[1] == '-':
                _F[0] = _L[0][:]
                _L[0] = _B[0][:]
                _B[0] = _R[0][:]
                _R[0] = temp[:]
                spin_L(_U)
            else:
                _F[0] = _R[0][:]
                _R[0] = _B[0][:]
                _B[0] = _L[0][:]
                _L[0] = temp[:]
                spin_R(_U)

        elif C[0] == 'D':
            temp = _F[2][:]
            if C[1] == '-':
                _F[2] = _R[2][:]
                _R[2] = _B[2][:]
                _B[2] = _L[2][:]
                _L[2] = temp[:]
                spin_L(_D)
            else:
                _F[2] = _L[2][:]
                _L[2] = _B[2][:]
                _B[2] = _R[2][:]
                _R[2] = temp[:]
                spin_R(_D)

        elif C[0] == 'R':
            temp = [_U[0][2], _U[1][2], _U[2][2]]
            if C[1] == '-':
                for i in range(3):
                    _U[i][2] = _B[2-i][0]
                    _B[2-i][0] = _D[i][2]
                    _D[i][2] = _F[i][2]
                    _F[i][2] = temp[i]
                spin_L(_R)
            else:
                for i in range(3):
                    _U[i][2] = _F[i][2]
                    _F[i][2] = _D[i][2]
                    _D[i][2] = _B[2-i][0]
                    _B[2-i][0] = temp[i]
                spin_R(_R)

        elif C[0] == 'L':
            temp = [_U[0][0], _U[1][0], _U[2][0]]
            if C[1] == '-':
                for i in range(3):
                    _U[i][0] = _F[i][0]
                    _F[i][0] = _D[i][0]
                    _D[i][0] = _B[2-i][2]
                    _B[2-i][2] = temp[i]
                spin_L(_L)
            else:
                for i in range(3):
                    _U[i][0] = _B[2-i][2]
                    _B[2-i][2] = _D[i][0]
                    _D[i][0] = _F[i][0]
                    _F[i][0] = temp[i]
                spin_R(_L)

        elif C[0] == 'F':
            temp = _U[2][:]
            if C[1] == '-':
                _U[2] = [_R[0][0], _R[1][0], _R[2][0]]
                _R[2][0], _R[1][0], _R[0][0] = _D[0][:]
                _D[0] = [_L[0][2], _L[1][2], _L[2][2]]
                _L[2][2], _L[1][2], _L[0][2] = temp[:]
                spin_L(_F)
            else:
                _U[2] = [_L[2][2], _L[1][2], _L[0][2]]
                _L[0][2], _L[1][2], _L[2][2] = _D[0][:]
                _D[0] = [_R[2][0], _R[1][0], _R[0][0]]
                _R[0][0], _R[1][0], _R[2][0] = temp[:]
                spin_R(_F)

        elif C[0] == 'B':
            temp = _U[0][:]
            if C[1] == '-':
                _U[0] = [_L[2][0], _L[1][0], _L[0][0]]
                _L[0][0], _L[1][0], _L[2][0] = _D[2][:]
                _D[2] = [_R[2][2], _R[1][2], _R[0][2]]
                _R[0][2], _R[1][2], _R[2][2] = temp[:]
                spin_L(_B)
            else:
                _U[0] = [_R[0][2], _R[1][2], _R[2][2]]
                _R[2][2], _R[1][2], _R[0][2] = _D[2][:]
                _D[2] = [_L[0][0], _L[1][0], _L[2][0]]
                _L[2][0], _L[1][0], _L[0][0] = temp[:]
                spin_R(_B)
    for i in range(3):
        print(''.join(_U[i]))
