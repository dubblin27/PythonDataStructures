def qk(arr):
    if len(arr) <=1 :
        return arr
    else :
        pivot = arr.pop()
    ele_less = []
    ele_gre = []

    for item in arr:
        if pivot > item :
            ele_less.append(item)
        else:
            ele_gre.append(item)
    return qk(ele_less) + [pivot] + qk(ele_gre)

arr = list(map(int,input().split()))
print(qk(arr))