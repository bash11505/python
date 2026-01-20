#2 pointers method
arr=[2,3,4,7,8]
left = 0
right = len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left += 1
    right -= 1
print(arr)


#2nd programme
arr = [2, 4, 6, 8, 10]
target = 12

left = 0
right = len(arr) - 1

while left < right:
    s = arr[left] + arr[right]

    if s == target:
        print(arr[left], arr[right])
        break
    elif s < target:
        left += 1
    else:
        right -= 1
print("no pair found")
