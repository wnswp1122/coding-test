def solution(m, musicinfo):
    m = replace_sharp(m)
    answer = (-1, None)
    for music in musicinfo:
        info = music.split(',')
        time = h_to_m(info[1]) - h_to_m(info[0])
        song_name = info[2]
        chords = replace_sharp(info[3])
        played = (chords * (time // len(chords) + 1))[:time]
        
        if m in played:
            if answer[0] < time:
                answer = (time, song_name)
                
    return answer[1]

def h_to_m(time_str):
    h, m = map(int, time_str.split(":"))
    return h * 60 + m

def replace_sharp(melody):
    return melody.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
