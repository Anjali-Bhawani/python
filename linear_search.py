def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

my_list = [5,7,8,9,10]
target = 10

result = linear_search(my_list,target)
print(result)
    