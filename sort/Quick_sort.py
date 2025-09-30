def partition(arr,low,high):
    i = low - 1
    pivot = arr[high]

    for j in range(low,high):
        if arr[j] < pivot:
            i +=1

            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = temp

    return i+1

def quick_sort(arr,low,high):

    if low<high:

        pi = partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

    return arr


arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
print("Sorted array:", quick_sort(arr,0,len(arr)-1))