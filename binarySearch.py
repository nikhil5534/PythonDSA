def binary(arr, l, h, item):
    if l <= h:
        mid = (l + h)//2
        if arr[mid] == item:
            return print(mid)
        elif arr[mid] > item:
            return binary(arr, l, mid-1, item)
        else:
            return binary(arr, mid+1, h, item)
    else:
        return -1

a=[1,4,7,5,43,88,96]

binary(a,0, b, 4)