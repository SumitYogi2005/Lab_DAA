import random
import time


# 1. Bubble Sort
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


# 2. Selection Sort
def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# 3. Insertion Sort
def insertion_sort(arr):
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# 4. Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# 5. Quick Sort
def quick_sort(arr):
    arr = arr.copy()

    # Pivot strategy: Last element
    # Iterative implementation avoids recursion depth errors.

    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()

        if low >= high:
            continue

        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        pi = i + 1
        arr[pi], arr[high] = arr[high], arr[pi]

        stack.append((low, pi - 1))
        stack.append((pi + 1, high))

    return arr


# 6. Heap Sort
def heap_sort(arr):
    arr = arr.copy()
    n = len(arr)

    def heapify(size, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < size and arr[left] > arr[largest]:
            largest = left

        if right < size and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(size, largest)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)

    return arr


# List of sorting algorithms
algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort
}


# Input sizes
sizes = [100, 200, 500, 1000]

# Input types
input_types = ["Random", "Sorted", "Reverse Sorted"]

print("\nSORTING ALGORITHM PERFORMANCE COMPARISON")
print("=" * 90)

print("{:<18} {:<15} {:<10} {:<15}".format(
    "Algorithm", "Input Type", "Size", "Time (seconds)"
))

print("-" * 90)


# Testing each input size
for n in sizes:

    # Generate random array
    random_arr = random.sample(range(n * 10), n)

    # Generate sorted and reverse sorted arrays
    sorted_arr = sorted(random_arr)
    reverse_arr = sorted_arr[::-1]

    # Store all input types
    test_data = {
        "Random": random_arr,
        "Sorted": sorted_arr,
        "Reverse Sorted": reverse_arr
    }

    # Test all six sorting algorithms
    for name, algorithm in algorithms.items():

        for input_name, data in test_data.items():

            # Measure execution time
            start = time.perf_counter()

            result = algorithm(data)

            end = time.perf_counter()

            execution_time = end - start

            # Verify sorting correctness
            assert result == sorted(data)

            # Print results
            print("{:<18} {:<15} {:<10} {:<15.8f}".format(
                name,
                input_name,
                n,
                execution_time
            ))

    print("-" * 90)


print("\nPerformance testing completed successfully!")