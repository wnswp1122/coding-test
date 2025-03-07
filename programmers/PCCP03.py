def solution(points, routes):
    answer = 0
    x = len(routes)
    robot_points = [[0, 0] for _ in range(x)]
    robot_targets = [[0, 0] for _ in range(x)]

    for robot in range(x):
        robot_points[robot] = points[routes[robot][0]-1].copy()
        robot_targets[robot] = points[routes[robot][1]-1].copy()
        del routes[robot][:2]
        routes[robot].append(-1)

    def move(start, end):
        if start[0] == end[0]:
            if start[1] < end[1]:
                start[1] += 1
            else:
                start[1] -= 1
        else:
            if start[0] < end[0]:
                start[0] += 1
            else:
                start[0] -= 1
        return start
    
    def check():
        dup = set()
        for point in robot_points:
            if robot_points.count(point) > 1:   
                dup.add(tuple(point))
        dup.discard((-1,-1))
        return len(dup)

    answer += check()

    while any(row for row in routes):
        for robot in range(x):
            if robot_points[robot] == [-1,-1]: continue
            
            if robot_points[robot] == robot_targets[robot]:
                new_target = points[routes[robot][0]-1]
                del routes[robot][0]
                if len(routes[robot]) == 0: 
                    robot_points[robot] = [-1,-1]
                    continue
                robot_targets[robot] = new_target
            move(robot_points[robot], robot_targets[robot])
        answer += check()    
    return answer
            


#print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]]))