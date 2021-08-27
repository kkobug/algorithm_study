from sys import stdin as st

melon = int(st.readline())
ans = 0
arr = [[], [], [], [], []]

for i in range(6):
    d, dist = map(int, st.readline().split())
    arr[d].append(dist)

if len(arr[1]) == len(arr[3]):
    if len(arr[1]) == 1:
        ans = arr[1][0]*arr[3][0] - min(arr[2])*min(arr[4])
    else:
        ans = arr[2][0]*arr[4][0] - min(arr[1])*min(arr[3])
else:
    if len(arr[2]) == 1:
        ans = arr[2][0]*arr[3][0] - min(arr[1])*min(arr[4])
    else:
        ans = arr[1][0]*arr[4][0] - min(arr[2])*min(arr[3])

print(ans * melon)