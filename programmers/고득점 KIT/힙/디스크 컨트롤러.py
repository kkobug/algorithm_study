"""
https://school.programmers.co.kr/learn/courses/30/lessons/42627
if 작업대에 작업이 있다:
    1. 작업대에서 다음 작업을 꺼낸다
    2. 작업에 걸린 시간만큼 전체 소요 시간에 더해준다
    3. 다음 작업에 걸리는 시간만큼 시간을 보낸다
    4. 완료한 작업 카운트를 1 늘려준다
else:
    1. 작업 시간을 1 늘린다
변경된 시간보다 일찍 들어온 작업들을 모두 작업대에 넣어준다
"""
from heapq import heappop, heappush


def solution(jobs):
    jobs.sort()
    time_now, time_total = -1, 0
    job_cnt, job_idx, job_finished_cnt = len(jobs), 0, 0
    works = []
    while job_finished_cnt < job_cnt:
        if works:
            need_time, started_time = heappop(works)
            time_total += time_now + need_time - started_time
            time_now += need_time
            job_finished_cnt += 1
        else:
            time_now += 1
        while job_idx < job_cnt and jobs[job_idx][0] <= time_now:
            heappush(works, (jobs[job_idx][1], jobs[job_idx][0]))
            job_idx += 1
    return time_total // job_cnt


print(solution([[0, 3], [1, 9], [2, 6]]))
