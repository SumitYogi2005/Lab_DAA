def heap_sort(arr):
    arr = arr.copy()
    n = len(arr)

    def heapify(n, i):
        largest = i

        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]

            heapify(n, largest)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    print("Max Heap:", arr)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        heapify(i, 0)

        print("Pass:", arr)

    return arr


# Main program
arr = [12, 11, 13, 5, 6, 7]

print("Original Array:", arr)
result = heap_sort(arr)
print("Sorted Array:", result)