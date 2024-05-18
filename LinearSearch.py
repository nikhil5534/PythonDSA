def linear(arr,item):

    for i in range(len(arr)):

        if arr[i] == item:
            return i
    return ('Not Found')
a=[1,4,7,5,43,88,96]
print(linear(a,4))