# Simplified Search Engine using Binary Search and Hashing


# ------------------------------------------
# 1. Dictionary of words and document IDs
# ------------------------------------------

documents = {
    "algorithm": 101,
    "array": 102,
    "binary": 103,
    "computer": 104,
    "database": 105,
    "data": 106,
    "development": 107,
    "function": 108,
    "graph": 109,
    "hashing": 110,
    "index": 111,
    "java": 112,
    "keyword": 113,
    "linked": 114,
    "machine": 115,
    "network": 116,
    "object": 117,
    "program": 118,
    "python": 119,
    "query": 120,
    "recursion": 121,
    "search": 122,
    "sorting": 123,
    "stack": 124,
    "structure": 125,
    "tree": 126,
    "variable": 127,
    "website": 128,
    "software": 129,
    "compiler": 130
}


# ------------------------------------------
# 2. Binary Search
# ------------------------------------------

def binary_search(words, target):

    low = 0
    high = len(words) - 1
    comparisons = 0

    while low <= high:

        mid = (low + high) // 2
        comparisons += 1

        if words[mid][0] == target:
            return words[mid][1], comparisons

        elif words[mid][0] < target:
            low = mid + 1

        else:
            high = mid - 1

    return None, comparisons


# ------------------------------------------
# 3. Custom Hash Function
# ------------------------------------------

def hash_function(word, size):

    hash_value = 0

    for character in word:
        hash_value = (hash_value * 31 + ord(character)) % size

    return hash_value


# ------------------------------------------
# 4. Hash Table - Separate Chaining
# ------------------------------------------

class ChainingHashTable:

    def __init__(self, size):

        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, word, doc_id):

        index = hash_function(word, self.size)

        # Add word to the bucket
        self.table[index].append((word, doc_id))

    def search(self, target):

        index = hash_function(target, self.size)
        comparisons = 0

        # Search inside the bucket
        for word, doc_id in self.table[index]:

            comparisons += 1

            if word == target:
                return doc_id, comparisons

        return None, comparisons


# ------------------------------------------
# 5. Hash Table - Linear Probing
# ------------------------------------------

class ProbingHashTable:

    def __init__(self, size):

        self.size = size
        self.table = [None] * size

    def insert(self, word, doc_id):

        index = hash_function(word, self.size)

        # Find an empty slot
        for i in range(self.size):

            position = (index + i) % self.size

            if self.table[position] is None:
                self.table[position] = (word, doc_id)
                return

            elif self.table[position][0] == word:
                self.table[position] = (word, doc_id)
                return

        raise OverflowError("Hash table is full!")

    def search(self, target):

        index = hash_function(target, self.size)
        probes = 0

        # Search using linear probing
        for i in range(self.size):

            position = (index + i) % self.size
            probes += 1

            if self.table[position] is None:
                return None, probes

            if self.table[position][0] == target:
                return self.table[position][1], probes

        return None, probes


# ------------------------------------------
# 6. Create Search Structures
# ------------------------------------------

# Sorted list for Binary Search
sorted_words = sorted(documents.items())

# Create hash tables
table_size = 37

chaining_table = ChainingHashTable(table_size)
probing_table = ProbingHashTable(table_size)

# Insert all words into both hash tables
for word, doc_id in documents.items():

    chaining_table.insert(word, doc_id)
    probing_table.insert(word, doc_id)


# ------------------------------------------
# 7. Search and Compare All Methods
# ------------------------------------------

def search_word(target):

    target = target.strip().lower()

    print("\nSEARCHING FOR:", target)
    print("=" * 55)

    # Method 1: Binary Search
    result1, count1 = binary_search(sorted_words, target)

    # Method 2: Separate Chaining
    result2, count2 = chaining_table.search(target)

    # Method 3: Linear Probing
    result3, count3 = probing_table.search(target)

    # Display Binary Search result
    print("\n1. BINARY SEARCH")

    if result1 is not None:
        print("Word Found!")
        print("Document ID:", result1)
    else:
        print("Word Not Found!")

    print("Comparisons:", count1)

    # Display Chaining result
    print("\n2. HASH TABLE - SEPARATE CHAINING")

    if result2 is not None:
        print("Word Found!")
        print("Document ID:", result2)
    else:
        print("Word Not Found!")

    print("Comparisons:", count2)

    # Display Linear Probing result
    print("\n3. HASH TABLE - LINEAR PROBING")

    if result3 is not None:
        print("Word Found!")
        print("Document ID:", result3)
    else:
        print("Word Not Found!")

    print("Probes:", count3)

    # Comparison table
    print("\nPERFORMANCE COMPARISON")
    print("-" * 55)

    print("{:<28} {:<15}".format("Method", "Operations"))
    print("-" * 43)

    print("{:<28} {:<15}".format("Binary Search", count1))
    print("{:<28} {:<15}".format("Separate Chaining", count2))
    print("{:<28} {:<15}".format("Linear Probing", count3))

    print("-" * 55)


# ------------------------------------------
# 8. Main Menu
# ------------------------------------------

def main():

    print("======================================")
    print("       SIMPLIFIED SEARCH ENGINE")
    print("======================================")

    print("Total Words in Dictionary:", len(documents))

    while True:

        print("\n1. Search for a Word")
        print("2. Display All Words")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            word = input("Enter word to search: ")

            if word.strip() == "":
                print("Please enter a valid word!")
                continue

            search_word(word)

        elif choice == "2":

            print("\nWORD DICTIONARY")
            print("-" * 35)

            for word, doc_id in sorted_words:
                print(word, ":", doc_id)

        elif choice == "3":

            print("\nThank you for using Search Engine!")
            break

        else:

            print("Invalid choice! Try again.")


# ------------------------------------------
# 9. Execute Program
# ------------------------------------------

if __name__ == "__main__":
    main()