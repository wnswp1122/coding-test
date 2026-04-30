import math

def solution(signals):
    lcm = 1
    for g, y, r in signals:
        cycle = g + y + r
        lcm = (lcm * cycle) // math.gcd(lcm, cycle)

    for t in range(1, lcm + 1):
        is_all_yellow = True

        for g, y, r in signals:
            cycle_length = g + y + r
            current_pos = (t - 1) % cycle_length

            if not (g <= current_pos < g + y):
                is_all_yellow = False
                break

        if is_all_yellow:
            return t

    return -1