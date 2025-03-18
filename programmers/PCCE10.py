def solution(mats, park):
    mats.sort(reverse = True)
    row = len(park[0])
    col = len(park)
    for i in mats:
        for c in range(col - i + 1):
            for r in range(row - i + 1):
                if(park[c][r] == "-1"):
                    if(check(i,park,r,c) == True): return i
    return -1


def check(size, park, r, c):
    for i in range(size):
        for j in range(size):
            if(park[c+i][r+j] != "-1"): 
                return False
    return True


mats = [5,3,2]
park = [["A", "A", "-1", "B", "B", "B", "B", "-1"],
        ["A", "A", "-1", "B", "B", "B", "B", "-1"],
        ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
        ["D", "D", "-1", "-1", "-1", "-1", "-1", "-1"], 
        ["D", "D", "-1", "-1", "-1", "E", "-1", "F"],
        ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
        ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
        ]
print(solution(mats,park))