def insertion_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        print("Pass", i, ":", arr)

    return arr


# Main program
arr = [12, 11, 13, 5, 6]

print("Original Array:", arr)
result = insertion_sort(arr)
print("Sorted Array:", result)