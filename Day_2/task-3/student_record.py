import time


# ------------------------------------------------
# 1. Student Records
# ------------------------------------------------

students = [
    {"roll": 105, "name": "Rahul", "marks": 85},
    {"roll": 102, "name": "Aman", "marks": 92},
    {"roll": 108, "name": "Priya", "marks": 78},
    {"roll": 101, "name": "Karan", "marks": 88},
    {"roll": 106, "name": "Sneha", "marks": 95},
    {"roll": 103, "name": "Rohit", "marks": 72},
    {"roll": 107, "name": "Anjali", "marks": 90},
    {"roll": 104, "name": "Vikas", "marks": 80}
]


# ------------------------------------------------
# 2. Bubble Sort
# ------------------------------------------------

def bubble_sort(data, key):
    arr = data.copy()
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if arr[j][key] > arr[j + 1][key]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


# ------------------------------------------------
# 3. Selection Sort
# ------------------------------------------------

def selection_sort(data, key):
    arr = data.copy()
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j][key] < arr[min_index][key]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# ------------------------------------------------
# 4. Insertion Sort
# ------------------------------------------------

def insertion_sort(data, key):
    arr = data.copy()

    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1

        while j >= 0 and arr[j][key] > current[key]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current

    return arr


# ------------------------------------------------
# 5. Merge Sort
# ------------------------------------------------

def merge_sort(data, key):
    if len(data) <= 1:
        return data.copy()

    mid = len(data) // 2

    left = merge_sort(data[:mid], key)
    right = merge_sort(data[mid:], key)

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# ------------------------------------------------
# 6. Quick Sort
# ------------------------------------------------

def quick_sort(data, key):
    arr = data.copy()

    # Pivot strategy: Last element
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()

        if low >= high:
            continue

        pivot = arr[high][key]
        i = low - 1

        for j in range(low, high):
            if arr[j][key] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        pi = i + 1
        arr[pi], arr[high] = arr[high], arr[pi]

        stack.append((low, pi - 1))
        stack.append((pi + 1, high))

    return arr


# ------------------------------------------------
# 7. Heap Sort
# ------------------------------------------------

def heap_sort(data, key):
    arr = data.copy()
    n = len(arr)

    def heapify(size, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < size and arr[left][key] > arr[largest][key]:
            largest = left

        if right < size and arr[right][key] > arr[largest][key]:
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


# ------------------------------------------------
# 8. Sorting Algorithm Menu
# ------------------------------------------------

algorithms = {
    "1": ("Bubble Sort", bubble_sort),
    "2": ("Selection Sort", selection_sort),
    "3": ("Insertion Sort", insertion_sort),
    "4": ("Merge Sort", merge_sort),
    "5": ("Quick Sort", quick_sort),
    "6": ("Heap Sort", heap_sort)
}


# ------------------------------------------------
# 9. Display Student Records
# ------------------------------------------------

def display_students(data):
    print("\n" + "-" * 48)
    print("{:<12} {:<18} {:<10}".format(
        "Roll No.", "Name", "Marks"
    ))
    print("-" * 48)

    for student in data:
        print("{:<12} {:<18} {:<10}".format(
            student["roll"],
            student["name"],
            student["marks"]
        ))

    print("-" * 48)


# ------------------------------------------------
# 10. Binary Search
# ------------------------------------------------

def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid]["roll"] == target:
            return mid

        elif data[mid]["roll"] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# ------------------------------------------------
# 11. Compare Sorting Algorithm Performance
# ------------------------------------------------

def compare_performance(data, key):

    print("\nSORTING PERFORMANCE COMPARISON")
    print("=" * 55)

    results = []

    # Repeat sorting to get more reliable timing
    repetitions = 1000

    for name, algorithm in algorithms.values():

        start = time.perf_counter()

        for _ in range(repetitions):
            sorted_data = algorithm(data, key)

        end = time.perf_counter()

        avg_time = (end - start) / repetitions

        results.append((name, avg_time))

        print("{:<18} {:.8f} seconds".format(
            name, avg_time
        ))

    # Find fastest and slowest algorithms
    fastest = min(results, key=lambda x: x[1])
    slowest = max(results, key=lambda x: x[1])

    difference = slowest[1] - fastest[1]

    print("\nPERFORMANCE REPORT")
    print("-" * 40)

    print("Fastest Algorithm:", fastest[0])
    print("Fastest Time:", fastest[1], "seconds")

    print("\nSlowest Algorithm:", slowest[0])
    print("Slowest Time:", slowest[1], "seconds")

    print("\nTime Difference:", difference, "seconds")

    print("-" * 40)


# ------------------------------------------------
# 12. Main Menu
# ------------------------------------------------

def main():

    global students

    while True:

        print("\n===== STUDENT RECORD MANAGEMENT =====")
        print("1. Display Student Records")
        print("2. Sort Student Records")
        print("3. Search Student by Roll Number")
        print("4. Compare Sorting Algorithms")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        # Display records
        if choice == "1":
            display_students(students)

        # Sort records
        elif choice == "2":

            print("\nSort Records By:")
            print("1. Roll Number")
            print("2. Name")
            print("3. Marks")

            sort_choice = input("Enter choice: ")

            keys = {
                "1": "roll",
                "2": "name",
                "3": "marks"
            }

            if sort_choice not in keys:
                print("Invalid sorting choice!")
                continue

            key = keys[sort_choice]

            print("\nSelect Sorting Algorithm:")

            for number, (name, _) in algorithms.items():
                print(number + ".", name)

            algo_choice = input("Enter choice: ")

            if algo_choice not in algorithms:
                print("Invalid algorithm choice!")
                continue

            name, algorithm = algorithms[algo_choice]

            students = algorithm(students, key)

            print("\nRecords sorted using", name)
            display_students(students)

        # Search by roll number
        elif choice == "3":

            # Ensure records are sorted by roll number
            students = merge_sort(students, "roll")

            try:
                roll = int(input("Enter Roll Number to search: "))
            except ValueError:
                print("Please enter a valid roll number!")
                continue

            index = binary_search(students, roll)

            if index != -1:
                print("\nStudent Found!")
                display_students([students[index]])
            else:
                print("\nStudent record not found!")

        # Compare performance
        elif choice == "4":

            print("\nSelect field for performance comparison:")
            print("1. Roll Number")
            print("2. Name")
            print("3. Marks")

            compare_choice = input("Enter choice: ")

            keys = {
                "1": "roll",
                "2": "name",
                "3": "marks"
            }

            if compare_choice not in keys:
                print("Invalid choice!")
                continue

            key = keys[compare_choice]

            compare_performance(students, key)

        # Exit
        elif choice == "5":
            print("\nThank you for using Student Record Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


# ------------------------------------------------
# 13. Execute Main Program
# ------------------------------------------------

if __name__ == "__main__":
    main()