def solution(schedules, timelogs, startday):
    
    def is_valid(schedule, time):
        schedule = (schedule // 100) * 60 + (schedule % 100)
        time = (time // 100) * 60 + (time % 100)
        return time <= schedule + 10

    result = 0

    for employee in range(len(schedules)):
        day = startday
        ok = True

        for i in range(7):
            if day % 7 == 6 or day % 7 == 0:
                day += 1
                continue

            if not is_valid(schedules[employee], timelogs[employee][i]):
                ok = False
                break

            day += 1

        if ok:
            result += 1

    return result