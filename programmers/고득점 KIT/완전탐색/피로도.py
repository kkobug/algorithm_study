"""
https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""
def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    visit = [False] * n

    def search_dungeon(order):
        now_k, cnt = k, 0
        for o in order:
            if dungeons[o][0] <= now_k:
                now_k -= dungeons[o][1]
                cnt += 1
        return cnt

    def set_order(cnt, result):
        nonlocal answer
        if cnt == n:
            answer = max(answer, search_dungeon(result))
            return

        for ni in range(n):
            if visit[ni]:
                continue
            visit[ni] = True
            result.append(ni)
            set_order(cnt+1, result)
            visit[ni] = False
            result.pop()

    set_order(0, [])
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
