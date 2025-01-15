def solution(video_len, pos, op_start, op_end, commands):
    video_sec = time_to_sec(video_len)
    pos_sec = time_to_sec(pos)
    start_sec = time_to_sec(op_start)
    end_sec = time_to_sec(op_end)

    for i in commands:
        pos_sec = op_skip(pos_sec,start_sec,end_sec)
        if(i == "next"):
            pos_sec = next(pos_sec,video_sec)
        else: pos_sec = prev(pos_sec)
    pos_sec = op_skip(pos_sec,start_sec,end_sec)

    answer = sec_to_time(pos_sec)
    return answer


def time_to_sec(time):
    return int(time[0])*600 + int(time[1])*60 + int(time[3])*10 + int(time[4])

def sec_to_time(sec):
    return str(int(sec / 60)).zfill(2) + ":" + str(sec%60).zfill(2)

def prev(pos_sec):
    if (pos_sec < 10): return 0
    else: return pos_sec - 10
    
def next(pos_sec,video_sec):
    if(video_sec - pos_sec < 10): return video_sec
    else: return pos_sec + 10

def op_skip(pos_sec,start_sec,end_sec):
    if(start_sec <= pos_sec and pos_sec <= end_sec): return end_sec
    else: return pos_sec

print(solution("34:33","13:00","00:55","02:55",["next", "prev"]))
