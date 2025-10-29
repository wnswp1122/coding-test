def cal_count(X):
    dp_dict = {0: {1}}
    visited = {1}
    count = 0
    
    while True:
        if X in dp_dict[count]:
            return count
        
        dp_dict[count + 1] = set()
        for i in dp_dict[count]:
            for nxt in (i + 1, i * 2, i * 3):
                if nxt <= X and nxt not in visited:
                    dp_dict[count + 1].add(nxt)
                    visited.add(nxt)
        count += 1



X = int(input())
print(cal_count(X))
