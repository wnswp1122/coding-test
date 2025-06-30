dwarf_arr = []
for i in range(9):
    dwarf_arr.append(int(input()))

dwarf_arr.sort()
target = sum(dwarf_arr) - 100

for i in range(9):
    for j in range(i+1,9):
        if target == dwarf_arr[i] + dwarf_arr[j]:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(dwarf_arr[k])
            exit(0)
                


        
