"""
https://www.acmicpc.net/problem/4195
"""
from sys import stdin
input = stdin.readline

def find(x):
    if x == parent[x]:
        return x
    else:
        parent_x = find(parent[x])
        parent[x] = parent_x
        return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    
    if root_x != root_y:
        parent[root_y] = root_x
        cnt[root_x] += cnt[root_y]

def create(f):
    if not parent.get(f):
        parent[f] = f
        cnt[f] = 1

for tc in range(int(input())):
    F = int(input())
    parent = dict()
    cnt = dict()
    
    for _ in range(F):
        friend_A, friend_B = input().split()
        
        create(friend_A)
        create(friend_B)
        
        union(friend_A, friend_B)
        print(cnt[find(friend_A)])
