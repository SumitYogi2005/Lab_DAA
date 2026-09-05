def quick_sort(arr):
    arr = arr.copy()

    def partition(low, high):
        # Pivot selection: Last element
        pivot = arr[high]

        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        print("After partition:", arr)

        return i + 1

    def sort(low, high):
        if low < high:
            pi = partition(low, high)

            sort(low, pi - 1)
            sort(pi + 1, high)

    sort(0, len(arr) - 1)

    return arr


# Main program
arr = [10, 7, 8, 9, 1, 5]

print("Original Array:", arr)
result = quick_sort(arr)
print("Sorted Array:", result)