#selection sort min index
arr = list(map(int,input("enter elements:").split()))
n=len(arr)
for i in range(n-1):
    min_index=i
    
    for j in range(i + 1, n):
        if arr[j]<arr[min_index]:
            min_index=j
    arr[i],arr[min_index] = arr[min_index],arr[i]
print("sorted array:",arr)
#max index
arr2=list(map(int,input("enter elements:").split()))
n=len(arr2)
for i in range(n-1):
    max_index=i

    for j in range(i+1,n):
        if arr2[j]>arr2[max_index]:
            max_index=j
    arr2[i],arr2[max_index]=arr2[max_index],arr2[i]
print("sorted arra:",arr2)
#3rd programme
arr3 = list(map(int, input("Enter elements: ").split()))
n = len(arr3)
swap_count = 0

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if arr3[j] < arr3[min_index]:
            min_index = j

    if min_index != i:
        arr3[i], arr3[min_index] = arr3[min_index], arr3[i]
        swap_count += 1

print("Sorted array:", arr3)
print("Number of swaps:", swap_count)
