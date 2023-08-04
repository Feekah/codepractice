def lns(arr):
    s = arr[0]
    l = arr[0]
    i = 1
    for i in arr:
        if i > l:
            l = i
        elif i < s:
            s = i
    return l, s

arr = [-8,5,1,8,59,1007,3,2,9]
largest, smallest = lns(arr)
print(largest, smallest)
        
