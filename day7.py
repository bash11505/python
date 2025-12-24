#1st programme
arr=[5,1,3,8,9]
n=len(arr)

for i in range(n):
    swapped = False

    for j in range(0 ,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped = True
        
    if not swapped:
        break
print("sorted array is:",arr)
#progrmmme
arr2 = [int(n) for n in input("Enter elements: ").split()]
print("Input received:", arr2)

n = len(arr2)

for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if arr2[j] > arr2[j + 1]:
            arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]
            swapped = True
    if not swapped:
        break

print("Sorted array is:", arr2)

