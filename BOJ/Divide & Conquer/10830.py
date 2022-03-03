"""
https://www.acmicpc.net/problem/10830
"""
N, B = map(int, input().split())
matrix = []
for i in range(N):
    val = map(int, input().split())
    matrix.append([])
    for j in val:
        matrix[i].append(j%1000)

def multiple(matrix_A, matrix_B):
    M = len(matrix_A)
    ret = []
    for i in range(M):
        ret.append([])
        for j in range(M):
            val = 0
            for k in range(M):
                val += matrix_A[i][k] * matrix_B[k][j]
            val %= 1000
            ret[i].append(val)
    return ret

def square(n):
    if n == 1:
        return matrix
    elif n % 2:
        check = square(n//2)
        return multiple(multiple(check, check), matrix)
    elif not n % 2:
        check = square(n//2)
        return multiple(check, check)

ans = square(B)
for i in range(N):
    print(*ans[i])
