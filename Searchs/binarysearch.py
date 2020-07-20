def binary_search(sorted_list, length, key):
    start = 0
    end = length -1
    count = 0

    while start <= end:
        count +=1
        mid =int ( (start + end ) /2)
        print("midvalue :" , arr[mid])
        # print(arr[start:end+1])
        if key == sorted_list[mid]:
            print("found : ", key,", position of key : ", mid)
            print("count :", count)
            break 
        elif key < sorted_list[mid] :
            end = mid -1 
            print(arr[start:end+1])
        elif key > sorted_list[mid] :
            start = mid +1 
            print(arr[start:end+1])

arr = list(map(int,input().split()))
n = len(arr)
print("length of array : ", n)
searchnumber = int(input())
arr.sort()
print(arr)
binary_search(arr,n,searchnumber)