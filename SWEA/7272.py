alpha = {
    'B': 2, 'A': 1, 'D': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1,
    'C': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
    'L': 0, 'M': 0, 'N': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0,
    'X': 0, 'Y': 0, 'Z': 0
}


for tc in range(1, 1+int(input())):
    a, b = input().split()
    ans = True

    if len(a) != len(b):
        print("#{} DIFF".format(tc))
        continue

    for i in range(len(a)):
        if alpha[a[i]] == alpha[b[i]]:
            ans = True
        else:
            ans = False
            break

    if ans:
        print("#{} SAME".format(tc))
    else:
        print("#{} DIFF".format(tc))
