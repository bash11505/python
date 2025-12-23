#Binary search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid      
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1    


arr = [10, 20, 30, 40, 50, 66, 70]
target = 66

result = binary_search(arr, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
    #2ns problem
def binary_search(arr, danger):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == danger:
            return mid
        elif arr[mid] < danger:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = list(map(int, input("Enter danger elements (sorted): ").split()))
danger = int(input("Enter the danger number to search: "))

result = binary_search(arr, danger)

if result != -1:
    print("Danger element found at index:", result)
else:
    print("Danger element not found")
