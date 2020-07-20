def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else :
        pivot = arr.pop() 
    ele_lesser = []
    ele_greater = []
    for item in arr:
        if item > pivot:
            ele_greater.append(item)
        else:
            ele_lesser.append(item)
    return quick_sort(ele_lesser)  + [pivot] + quick_sort(ele_greater)
arr = list(map(int,input().split()))
print(quick_sort(arr))