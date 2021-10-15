"""
창용 마을에는 N명의 사람이 살고 있다.
사람은 편의상 1번부터 N번 사람까지 번호가 붙어져 있다고 가정한다.
두 사람은 서로를 알고 있는 관계일 수 있고, 아닐 수 있다.
두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면,
이러한 사람들을 모두 다 묶어서 하나의 무리라고 한다.
창용 마을에 몇 개의 무리가 존재하는지 계산하는 프로그램을 작성하라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 각각 창용 마을에 사는 사람의 수와 서로를 알고 있는 사람의 관계 수를 나타내는
두 정수 N, M(1 ≤ N ≤ 100, 0 ≤ M ≤ N(N-1)/2) 이 공백 하나로 구분되어 주어진다.
이후 M개의 줄에 걸쳐서 서로를 알고 있는 두 사람의 번호가 주어진다.
같은 관계는 반복해서 주어지지 않는다.

[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
무리의 개수를 출력한다.

입력
2
6 5
1 2
2 5
5 1
3 4
4 6
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
출력
#1 2
#2 1
"""
def find_set(x):
    if friends[x] != x:
        friends[x] = find_set(friends[x])
    return friends[x]


for tc in range(int(input())):
    N, M = map(int, input().split())
    friends = list(range(N+1))
    for _ in range(M):
        st, ed = map(int, input().split())
        friends[find_set(ed)] = find_set(st)
    ans = -1
    cnt = [False]*(N+1)
    for i in set(friends):
        k = find_set(i)
        if not cnt[k]:
            cnt[k] = True
            ans += 1
    print(f'#{tc+1} {ans}')