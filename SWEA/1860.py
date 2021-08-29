for tc in range(1, 1+int(input())):
    N, M, K = map(int, input().split())
    ppl = sorted(list(map(int, input().split())))
    sale = [0] * (ppl[-1] + 1)
    eat = fish = 0
    ans = "Possible"

    temp = 0
    for i in range(1, ppl[-1] + 1):
        if i % M == 0:
            temp += K
        sale[i] = temp

    temp = 0
    for j in sorted(list(set(ppl))):
        temp += ppl.count(j)
        sale[j] -= temp
        if sale[j] < 0:
            ans = "Impossible"
            break

    print("#{} {}".format(tc, ans))

"""
def check():
    for i in range(n):
        bread = (customer[i] // m) * k - (i + 1)
        if bread < 0:
            return 'Impossible'
    return 'Possible'


for tc in range(1, int(input()) + 1):
    n, m, k = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort()

    print('#{} {}'.format(tc, check()))
"""