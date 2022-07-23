from datetime import date


def solution(a, b):
    num_to_day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    day = date.weekday(date(2016, a, b))
    answer = num_to_day[day]
    return answer


print(solution(5, 24))
