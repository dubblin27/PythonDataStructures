def mergesort(arr):
    if len(arr) > 2 :
        mid = len(arr) //2
        left = arr[:mid]
        right = arr[mid :]
        # if len(left) == 2 and left[1] < left[0]:
        #     left[0],left[1] = left[1],left[0]
        # if len(right) == 2 and right[1] < right[0]:
        #     right[0],right[1] = right[1],right[0]
        print(left, " l")
        print(right ," r")


        mergesort(left)
        mergesort(right)

        i,j = 0,0
        k = 0

        

arr = [4,3,5,9,2,8,1]
mergesort(arr)