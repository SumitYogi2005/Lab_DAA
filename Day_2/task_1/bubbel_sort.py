def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        print("Pass", i + 1, ":", arr)

        if not swapped:
            break

    return arr


# Main program
arr = [64, 34, 25, 12, 22, 11, 90]

print("Original Array:", arr)
result = bubble_sort(arr)
print("Sorted Array:", result)
