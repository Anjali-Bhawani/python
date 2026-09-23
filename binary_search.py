def binary_search(arr,target):
    high = len(arr)-1
    low = 0

    while low <= high:
        mid = high+low//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
    else:
        return -1


my_list = [87,88,89,90,92,97,99]
target = 97
result = binary_search(my_list,target)
print(result)