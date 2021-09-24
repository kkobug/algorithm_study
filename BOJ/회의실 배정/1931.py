import pprint

N = int(input())
meet = [list(map(int, input().split())) for _ in range(N)]
meet.sort()

pprint.pprint(meet)