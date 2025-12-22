# linear search
def linear_search(arr, danger):
    for i in range(len(arr)):
        if arr[i] == danger:
            return i
    return -1   # must be indented inside function

arr = [100, 200, 200, 200, 200, 666]
print(linear_search(arr, 666))
#2nd problem
def linear(arr1,target):
    indices =[]
    for i in range(len(arr1)):
        if arr1[i]==target:
            indices.append(i)
    return indices
arr=[1,6,2,6,3,6,4,6,5,6,6]
print
(linear(arr,6))

#3rd problem
def linear2(arr2):
    f = int(input("Enter a number to add to the list: "))
    target2 = int(input("Enter target value: "))
    
    arr2.append(f)  # add user input
    indices1 = []
    
    for i in range(len(arr2)):
        if arr2[i] == target2:
            indices1.append(i)
    
    if len(indices1) > 0:
        return indices1
    else:
        return "Not found"

arr2 = [10, 30, 40, 50, 60]
print(linear2(arr2))

