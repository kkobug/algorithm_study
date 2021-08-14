text = "This is a book~!"
need = "is"


def moonza(n, t):
    N = len(t)
    M = len(n)
    i, j = 0, 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1


moonza(need, text)
