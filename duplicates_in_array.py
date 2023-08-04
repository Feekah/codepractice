def find_dup(arr):
    counts = {}
    dupl = []

    for i in arr:
        if i in counts:
            counts[i] +=1
        else:
            counts[i] = 1

    for i, count in counts.items():
        if count > 1:
            dupl.append(i)

    return dupl

b = [3,3,6,1,8,3,5,6,9,0,2,3,45,6, 45]
dupl = find_dup(b)
print(dupl)
