def counting_sort(arr, exp):
    n = len(arr)

    output = [0] * n
    count = [0] * 10

    # Count occurrences of each digit
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10

        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy output to original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    arr = arr.copy()

    if any(num < 0 for num in arr):
        raise ValueError("Radix Sort supports non-negative integers only.")

    if not arr:
        return arr

    max_num = max(arr)

    exp = 1

    # Sort according to each digit position
    while max_num // exp > 0:
        counting_sort(arr, exp)

        print("After digit position", exp, ":", arr)

        exp *= 10

    return arr


# Main program
arr = [170, 45, 75, 90, 802, 24, 2, 66]

print("Original Array:", arr)
result = radix_sort(arr)
print("Sorted Array:", result)
