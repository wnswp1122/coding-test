import math

def solution(friends, gifts):
    n = len(friends)
    a= [ [0 for col in range(n)] for row in range(n) ]
    for g in gifts:
        record = g.split(" ")
        for i in range(n):
            if(record[0] == friends[i]):
                row = i
            elif(record[1] == friends[i]):
                col = i
        a[row][col] += 1

    for i in range(n):
        for j in range(n):
            if(i == j):
                a[i][i] += sum(a[i]) - a[i][i]
            else:
                a[i][i] -= a[j][i]

    answer = [0 for i in range(n)]
    k = 0
    for i in range(n):
        for j in range(k,n):
            if(a[i][j] > a[j][i]):
                answer[i] += 1
            elif(a[i][j] < a[j][i]):
                answer[j] += 1
            else:
                if(a[i][i] > a[j][j]):
                    answer[i] += 1
                elif(a[i][i] < a[j][j]):
                    answer[j] += 1
        k += 1

    return max(answer)
        



friends = ["a", "b", "c"]
gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]
print(solution(friends,gifts))