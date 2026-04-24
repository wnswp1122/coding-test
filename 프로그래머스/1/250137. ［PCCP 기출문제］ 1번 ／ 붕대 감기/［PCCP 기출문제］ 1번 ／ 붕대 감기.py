def solution(bandage, health, attacks):
    max_time = attacks[-1][0]
    max_health = health
    cur = 0
    seq_cnt = 0
    for time in range(1,max_time+1):
        if time == attacks[cur][0]:
            health -= attacks[cur][1]
            if health <= 0: return -1
            cur += 1
            seq_cnt = 0
        else:
            health += bandage[1]
            seq_cnt += 1
            if seq_cnt >=  bandage[0]:
                health +=  bandage[2]
                seq_cnt = 0
            if health > max_health:
                health = max_health
    return health  