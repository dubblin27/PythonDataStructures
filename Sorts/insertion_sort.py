# 5 3 4 1 2 

# 5           3 4 1 2 
# 3 5         4 1 2 
# 3 4 5       1 2 
# 1 3 4 5     2

# 1 2 3 4 5
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        print(key)
        j = i-1
        while j >= 0 and key < arr [j] :
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
        print(arr)
    return arr
        
arr = list(map(int,input().split()))
print(insertion_sort(arr))

