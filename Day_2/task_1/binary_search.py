def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        print("Checking index:", mid, "Value:", arr[mid])

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# Main program
arr = [10, 20, 30, 40, 50, 60, 70, 80]

print("Sorted Array:", arr)

# Search for existing element
target = 50
result = binary_search(arr, target)

if result != -1:
    print(target, "found at index:", result)
else:
    print(target, "not found")

print("--------------------")

# Search for non-existing element
target = 45
result = binary_search(arr, target)

if result != -1:
    print(target, "found at index:", result)
else:
    print(target, "not found")
    