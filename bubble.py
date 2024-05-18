def bubble(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
             if arr[j] > arr[j +1]:
                 arr[j], arr[j+1] = arr[j + 1],arr[j]
    print(arr)

arr = [2,334,2,46,45]
bubble(arr)