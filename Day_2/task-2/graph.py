        if right < size and arr[right] > arr[largest]:
            largest = right
        if largest != root:
            arr[root], arr[largest] = arr[largest], arr[root]
            heapify(size, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)
    return arr


algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort,
}

# Keep the quadratic algorithms at modest sizes to avoid long runs.
sizes = [100, 200, 500, 1000]
input_types = ["Random", "Already Sorted", "Reverse Sorted"]
results = []

random.seed(42)

for n in sizes:
    random_data = random.sample(range(n * 10), n)
    test_inputs = {
        "Random": random_data,
        "Already Sorted": sorted(random_data),
        "Reverse Sorted": sorted(random_data, reverse=True),
    }

    for algorithm_name, algorithm in algorithms.items():
        for input_name, data in test_inputs.items():
            start = time.perf_counter()
            sorted_result = algorithm(data)
            elapsed = time.perf_counter() - start

            # Confirm correctness before recording the result.
            assert sorted_result == sorted(data)

            results.append({
                "Algorithm": algorithm_name,
                "Input Type": input_name,
                "Input Size": n,
                "Time (seconds)": elapsed,
            })

# Save raw measurements to CSV.
csv_file = "sorting_timings.csv"
with open(csv_file, "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["Algorithm", "Input Type", "Input Size", "Time (seconds)"]
    )
    writer.writeheader()
    writer.writerows(results)

# Graph 1: all algorithms on random input.
plt.figure(figsize=(10, 6))
for algorithm_name in algorithms:
    rows = [
        row for row in results
        if row["Algorithm"] == algorithm_name and row["Input Type"] == "Random"
    ]
    rows.sort(key=lambda row: row["Input Size"])
    x = [row["Input Size"] for row in rows]
    y = [row["Time (seconds)"] for row in rows]
    plt.plot(x, y, marker="o", label=algorithm_name)

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithm Comparison – Random Input")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("random_input_comparison.png", dpi=300)
plt.close()

# Graph 2: all algorithms on already-sorted input.
plt.figure(figsize=(10, 6))
for algorithm_name in algorithms:
    rows = [
        row for row in results
        if row["Algorithm"] == algorithm_name
        and row["Input Type"] == "Already Sorted"
    ]
    rows.sort(key=lambda row: row["Input Size"])
    x = [row["Input Size"] for row in rows]
    y = [row["Time (seconds)"] for row in rows]
    plt.plot(x, y, marker="o", label=algorithm_name)

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithm Comparison – Already-Sorted Input")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("sorted_input_comparison.png", dpi=300)
plt.close()

print("Files created:")
print("1. random_input_comparison.png")
print("2. sorted_input_comparison.png")
print("3. sorting_timings.csv")
print("All sorting results were verified.")
