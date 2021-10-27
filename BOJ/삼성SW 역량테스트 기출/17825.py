"""
https://www.acmicpc.net/problem/17825
"""
def yut(dice_idx):
    global ans
    if dice_idx == 10:
        ans = max(ans, sum(point))
        return

    k = dice[dice_idx]
    for i in range(4):
        if 40 < position[i]:
            continue
        short = shortcut[i]
        if shortcut[i]:
            if shortcut[i] == 10:
                for now in range(4):
                    if position[i] == 10 + now*3:
                        if k < 4-now:
                            next_position = position[i] + 3*k
                        else:
                            next_position = 25 + 5*(k-4+now)
                            short = 25

            if shortcut[i] == 20:
                for now in range(3):
                    if position[i] == 20 + now*2:
                        if k < 3-now:
                            next_position = position[i] + 2*k
                        else:
                            next_position = 25 + 5*(k-3+now)
                            short = 25

            if shortcut[i] == 25:
                next_position = position[i] + 5*k

            if shortcut[i] == 30:
                if position[i] == 30:
                    if k == 1:
                        next_position = 28
                    elif k < 4:
                        next_position = position[i] - k-1
                    else:
                        next_position = 25 + 5 * (k - 4)
                        short = 25
                for now in range(3):
                    if position[i] == 28 - now:
                        if k < 3-now:
                            next_position = position[i] - k
                        else:
                            next_position = 25 + 5*(k-3+now)
                            short = 25
            if shortcut[i] == 40:
                next_position = 99

        else:
            next_position = position[i] + 2 * k
            if next_position in [10, 20, 25, 30]:
                short = next_position

        if 40 <= next_position:
            short = 40

        if next_position < 41 and next_position in position:
            for _i in range(4):
                if _i == i:
                    continue
                if next_position == position[_i]:
                    break
            if short == shortcut[_i]:
                continue

        temp = point[i]
        pos_temp = position[i]
        short_temp = shortcut[i]

        if next_position < 41:
            point[i] += next_position
        position[i] = next_position
        shortcut[i] = short
        yut(dice_idx+1)

        point[i] = temp
        position[i] = pos_temp
        shortcut[i] = short_temp


dice = list(map(int, input().split()))
point = [0] * 4
position = [0] * 4
shortcut = [False] * 4
ans = 0
yut(0)
print(ans)